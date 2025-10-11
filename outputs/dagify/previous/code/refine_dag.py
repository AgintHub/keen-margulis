from pydantic import BaseModel, Field
from typing import List


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


class RefineDagOutput(BaseModel):
    """Pydantic model for refine_dag node outputs."""
    dag_edges: List[str] = (
        Field(..., description="List of directed edges in the refined DAG, formatted as \"TaskA->TaskB\".")
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
    Optimizes a DAG for maximum concurrency while preserving acyclicity.

    Parameters
    ----------
    dag_nodes : List[str]
        Ordered list of task identifiers in the DAG.
    dag_edges : List[str]
        List of edges representing dependencies, formatted as
        "TaskA->TaskB".
    is_acyclic : bool
        Indicates whether the input DAG is acyclic.

    Returns
    -------
    Tuple[List[str], bool, bool, int]
        A tuple containing (refined_dag_edges, is_acyclic, is_concurrent,
        max_concurrency).

    Raises
    ------
    ValueError
        Raised if dag_edges is empty or if the input graph is cyclic.

    Examples
    --------
    >>> dag_nodes = ['A', 'B', 'C'],
    >>> dag_edges = ['A->B', 'B->C'],
    >>> is_acyclic = True,
    >>> refined = refine_dag(dag_nodes, dag_edges, is_acyclic),
    >>> print(refined)
    (['A->B', 'B->C'], True, False, 1)

    >>> dag_nodes = ['A', 'B', 'C'],
    >>> dag_edges = ['A->C'],
    >>> is_acyclic = True,
    >>> refined = refine_dag(dag_nodes, dag_edges, is_acyclic),
    >>> print(refined)
    (['A->C'], True, True, 2)

    """
    return RefineDagOutput(
        dag_edges=[],
        is_acyclic=False,
        is_concurrent=False,
        max_concurrency=0,
    )