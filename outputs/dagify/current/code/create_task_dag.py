from pydantic import BaseModel, Field
from typing import List


class IdentifyTaskDependenciesOutput(BaseModel):
    """Pydantic model for identify_task_dependencies node outputs."""
    task_names: List[str] = (
        Field(..., description="List of all task names identified from decomposition.")
    )
    dependency_pairs: List[str] = (
        Field(..., description="List of dependency relationships in the format 'TaskA -> TaskB' indicating TaskA must be completed before TaskB can start.")
    )
    dependency_count: int = (
        Field(..., description="Total number of dependency relationships identified.")
    )


class CreateTaskDagOutput(BaseModel):
    """Pydantic model for create_task_dag node outputs."""
    dag_nodes: List[str] = (
        Field(..., description="Ordered list of task identifiers in the DAG.")
    )
    dag_edges: List[str] = (
        Field(..., description="List of edges representing dependencies, formatted as 'source->target'.")
    )
    is_acyclic: bool = (
        Field(..., description="Indicates whether the constructed DAG is acyclic.")
    )


def create_task_dag(identify_task_dependencies_input: IdentifyTaskDependenciesOutput, **kwargs) -> CreateTaskDagOutput:
    """
    Constructs a Directed Acyclic Graph (DAG) of tasks from dependency
    information, returning an ordered list of tasks, the edge list, and an
    acyclicity flag.

    Parameters
    ----------
    task_names : List[str]
        All task identifiers identified from decomposition.
    dependency_pairs : List[str]
        Dependency relationships in the format 'TaskA -> TaskB', indicating
        TaskA must complete before TaskB.
    dependency_count : int
        Total number of dependency relationships identified.

    Returns
    -------
    Tuple[List[str], List[str], bool]
        A tuple containing the ordered list of tasks, the formatted edge
        list, and a boolean indicating if the DAG is acyclic.

    Raises
    ------
    ValueError
        If the provided dependencies contain a cycle or if input lists are
        inconsistent.

    Examples
    --------
    >>> dag_nodes, dag_edges, is_acyclic = create_task_dag(     ['A', 'B', 'C'],
    ['A -> B', 'B -> C'],     2 )
    >>> print(dag_nodes, dag_edges, is_acyclic)
    (['A', 'B', 'C'], ['A->B', 'B->C'], True)

    >>> try:
    ...     create_task_dag(['A', 'B'], ['A -> B', 'B -> A'], 2)
    >>> except ValueError as e:
    ...     print(e)
    "Cycle detected in task dependencies: ['A -> B', 'B -> A']"

    """
    return CreateTaskDagOutput(
        dag_nodes=[],
        dag_edges=[],
        is_acyclic=False,
    )