import logging
from collections import defaultdict, deque
from typing import Set, List


log = logging.getLogger(__name__)


def _parse_edge(edge: str) -> tuple[str, str]:
    """
    Creates a DAG from dependency pairs and returns an execution order.

    Parameters
    ----------
    identify_task_dependencies_input : IdentifyTaskDependenciesOutput
        Output from the identify_task_dependencies node containing task
        names and dependency pairs.
    kwargs : dict
        Additional keyword arguments for future extensions.

    Returns
    -------
    CreateTaskDagOutput
        Dataclass containing the ordered task list, edge list, and
        acyclicity flag.

    Raises
    ------
    ValueError
        If input validation fails or a cycle is detected in the dependency
        graph.

    Examples
    --------
    >>> from your_module import create_task_dag, IdentifyTaskDependenciesOutput
    >>> input_data = IdentifyTaskDependenciesOutput(
    ...     task_names=["A", "B", "C"],
    ...     dependency_pairs=["A -> B", "B -> C"],
    ...     dependency_count=2
    >>> )
    >>> output = create_task_dag(input_data)
    >>> print(output.dag_nodes, output.dag_edges, output.is_acyclic)
    ["A", "B", "C"] ['A->B', 'B->C'] True

    """
    parts = [p.strip() for p in edge.split('->')]
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError(f"Invalid dependency format: '{edge}'. Expected 'TaskA -> TaskB'")
    return parts[0], parts[1]


def create_task_dag(identify_task_dependencies_input: IdentifyTaskDependenciesOutput, **kwargs) -> CreateTaskDagOutput:
    """
    Constructs a Directed Acyclic Graph (DAG) from dependency pairs and returns an execution order.
    """
    task_names = identify_task_dependencies_input.task_names
    dependency_pairs = identify_task_dependencies_input.dependency_pairs
    dependency_count = identify_task_dependencies_input.dependency_count

    if not isinstance(task_names, list) or not all(isinstance(t, str) and t for t in task_names):
        raise ValueError("task_names must be a list of non-empty strings")
    if not isinstance(dependency_pairs, list) or not all(isinstance(d, str) and d for d in dependency_pairs):
        raise ValueError("dependency_pairs must be a list of non-empty strings")
    if dependency_count != len(dependency_pairs):
        raise ValueError("dependency_count does not match the number of dependency_pairs")

    task_set: Set[str] = set(task_names)
    adjacency: defaultdict[str, Set[str]] = defaultdict(set)
    indegree: defaultdict[str, int] = defaultdict(int)

    for pair in dependency_pairs:
        src, dst = _parse_edge(pair)
        if src == dst:
            raise ValueError(f"Self‑dependency detected: '{src}' -> '{dst}'")
        if src not in task_set or dst not in task_set:
            raise ValueError(f"Dependency references unknown task: '{pair}'")
        if dst not in adjacency[src]:
            adjacency[src].add(dst)
            indegree[dst] += 1
            if src not in indegree:
                indegree[src] += 0

    zero_indegree = deque([t for t in task_names if indegree[t] == 0])
    topo_order: List[str] = []
    while zero_indegree:
        node = zero_indegree.popleft()
        topo_order.append(node)
        for neighbor in adjacency[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    is_acyclic = len(topo_order) == len(task_names)
    if not is_acyclic:
        cycle_nodes = [t for t in task_names if indegree[t] > 0]
        raise ValueError(f"Cycle detected in task dependencies involving: {cycle_nodes}")

    dag_edges = [f"{src}->{dst}" for src in adjacency for dst in adjacency[src]]

    return CreateTaskDagOutput(
        dag_nodes=topo_order,
        dag_edges=dag_edges,
        is_acyclic=is_acyclic
    )