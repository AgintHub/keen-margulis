from pydantic import BaseModel, Field
from typing import List


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


class FinalizeWorkflowOutput(BaseModel):
    """Pydantic model for finalize_workflow node outputs."""
    dag_is_complete: bool = (
        Field(..., description="Whether the DAG is fully defined and ready")
    )
    dag_is_concurrent: bool = (
        Field(..., description="Whether the DAG has maximized concurrency")
    )
    dag_is_acyclic: bool = (
        Field(..., description="Whether the DAG contains no cycles")
    )
    adjusted_node_list: str = (
        Field(..., description="List of node names that were adjusted during finalization")
    )
    dag_summary: str = (
        Field(..., description="Human-readable summary of the finalized DAG")
    )


def finalize_workflow(refine_dag_input: RefineDagOutput, **kwargs) -> FinalizeWorkflowOutput:
    """
    Finalize and validate a workflow DAG, ensuring it is complete, concurrent,
    and acyclic.

    Parameters
    ----------
    dag_edges : List[str]
        Directed edges of the refined DAG, formatted as 'TaskA->TaskB'.
    is_acyclic : bool
        True if the refined DAG contains no cycles.
    is_concurrent : bool
        True if the refined DAG already supports maximum concurrency.
    max_concurrency : int
        Maximum number of tasks that can run concurrently in the refined
        DAG.

    Returns
    -------
    dict
        A dictionary with keys `dag_is_complete`, `dag_is_concurrent`,
        `dag_is_acyclic`, `adjusted_node_list`, and `dag_summary`.

    Raises
    ------
    ValueError
        If `dag_edges` is empty or malformed.
    RuntimeError
        If the DAG cannot be made acyclic or fully concurrent after
        adjustments.

    Examples
    --------
    >>> result = finalize_workflow(dag_edges=['A->B', 'B->C'], is_acyclic=True,
    is_concurrent=False, max_concurrency=2)
    >>> print(result)
    {'dag_is_complete': True, 'dag_is_concurrent': True, 'dag_is_acyclic': True,
    'adjusted_node_list': ['B'], 'dag_summary': 'DAG has 3 nodes and 2 edges.
    Concurrency adjusted to 2.'}

    >>> try:
    ...     finalize_workflow(dag_edges=[], is_acyclic=True, is_concurrent=True,
    max_concurrency=1)
    >>> except ValueError as e:
    ...     print(e)
    'dag_edges list is empty or contains malformed entries.'

    """
    return FinalizeWorkflowOutput(
        dag_is_complete=False,
        dag_is_concurrent=False,
        dag_is_acyclic=False,
        adjusted_node_list="",
        dag_summary="",
    )