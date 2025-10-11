import logging
from collections import defaultdict, deque
from typing import Dict, Set
from pydantic import BaseModel, Field


class CreateTaskDagOutput(BaseModel):
    dag_nodes: list[str] = (
        Field(..., description="Ordered list of task identifiers in the DAG.")
    )
    dag_edges: list[str] = (
        Field(..., description="List of edges representing dependencies, formatted as 'source->target'.")
    )
    is_acyclic: bool = (
        Field(..., description="Indicates whether the constructed DAG is acyclic.")
    )

class RefineDagOutput(BaseModel):
    dag_edges: list[str] = (
        Field(..., description="List of directed edges in the refined DAG, formatted as 'TaskA->TaskB'.")
    )
    is_acyclic: bool = (
        Field(..., description="Indicates whether the refined DAG contains any cycles.")
    )
    is_concurrent: bool = (
        Field(..., description="Indicates whether the DAG has been adjusted to allow concurrent execution of independent tasks.")
    )
    max_concurrency: int = (
        Field(..., description="Maximum number of tasks that can run concurrently in the refined DAG.")
    )

def refine_dag(create_task_dag_input: CreateTaskDagOutput, **kwargs) -> RefineDagOutput:
    """
    Compute level‑based execution plan and concurrency statistics for a task
    DAG.

    Parameters
    ----------
    create_task_dag_input : CreateTaskDagOutput
        Output from the create_task_dag node containing nodes, edges, and
        acyclicity flag.

    Returns
    -------
    RefineDagOutput
        Refined DAG with reordered edges and concurrency metrics.

    Raises
    ------
    ValueError
        Raised when the input DAG is empty, malformed, or contains cycles.

    Examples
    --------
    >>> dag = CreateTaskDagOutput(dag_nodes=['A', 'B', 'C'], dag_edges=['A->C'],
    is_acyclic=True)
    >>> result = refine_dag(dag)
    >>> print(result.dag_edges, result.is_acyclic, result.is_concurrent,
    result.max_concurrency)
    ['A->C'] True True 2

    """
    logger = logging.getLogger(__name__)
    dag_nodes = create_task_dag_input.dag_nodes
    dag_edges = create_task_dag_input.dag_edges
    if not dag_edges:
        raise ValueError("dag_edges list cannot be empty")
    node_set: Set[str] = set(dag_nodes)
    for edge in dag_edges:
        parts = edge.split('->')
        if len(parts) != 2:
            raise ValueError(f"Invalid edge format: {edge}")
        src, tgt = parts[0].strip(), parts[1].strip()
        if src not in node_set or tgt not in node_set:
            raise ValueError(f"Edge references unknown nodes: {edge}")
    adj: Dict[str, Set[str]] = defaultdict(set)
    indegree: Dict[str, int] = {node: 0 for node in dag_nodes}
    for edge in dag_edges:
        src, tgt = edge.split('->')
        src, tgt = src.strip(), tgt.strip()
        if tgt in adj[src]:
            continue
        adj[src].add(tgt)
        indegree[tgt] += 1
    queue: deque = deque([node for node in dag_nodes if indegree[node] == 0])
    if not queue:
        raise ValueError("No source nodes found; possible cycle.")
    sorted_nodes: list[str] = []
    levels: list[list[str]] = []
    while queue:
        level_size = len(queue)
        current_level: list[str] = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)
            sorted_nodes.append(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        levels.append(current_level)
    if len(sorted_nodes) != len(dag_nodes):
        raise ValueError("Cycle detected during topological sort.")
    max_concurrency = max(len(lvl) for lvl in levels)
    is_concurrent = max_concurrency > 1
    node_index = {node: idx for idx, node in enumerate(sorted_nodes)}
    sorted_edges = sorted(dag_edges, key=lambda e: (node_index[e.split('->')[0].strip()], node_index[e.split('->')[1].strip()]))
    return RefineDagOutput(
        dag_edges=sorted_edges,
        is_acyclic=True,
        is_concurrent=is_concurrent,
        max_concurrency=max_concurrency
    )