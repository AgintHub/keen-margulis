from pydantic import BaseModel, Field
from typing import List
import logging
import re


class RefineDagOutput(BaseModel):
    dag_edges: List[str] = (
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

class FinalizeWorkflowOutput(BaseModel):
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
        Field(..., description="Comma‑separated list of node names that were adjusted during finalization")
    )
    dag_summary: str = (
        Field(..., description="Human‑readable summary of the finalized DAG")
    )

def finalize_workflow(refine_dag_input: RefineDagOutput, **kwargs) -> FinalizeWorkflowOutput:
    """
    Finalizes and validates a workflow DAG, performing any necessary adjustments
    and returning key status flags and a summary.

    Parameters
    ----------
    refine_dag_input : RefineDagOutput
        Output from the refine_dag node containing the refined edges,
        acyclicity flag, concurrency flag, and maximum concurrency count.

    Returns
    -------
    FinalizeWorkflowOutput
        An object containing completion, concurrency, acyclicity status,
        list of adjusted nodes, and a textual summary.

    Raises
    ------
    ValueError
        If dag_edges is empty or contains malformed entries.

    Examples
    --------
    >>> from pydantic import BaseModel, Field
    >>> from typing import List
    >>> class RefineDagOutput(BaseModel):
    ...     dag_edges: List[str] = Field(..., description="List of directed
    edges in the refined DAG, formatted as 'TaskA->TaskB'.")
    ...     is_acyclic: bool = Field(..., description="Indicates whether the
    refined DAG contains any cycles.")
    ...     is_concurrent: bool = Field(..., description="Indicates whether the
    DAG has been adjusted to allow concurrent execution of independent tasks.")
    ...     max_concurrency: int = Field(..., description="Maximum number of
    tasks that can run concurrently in the refined DAG.")
    >>> class FinalizeWorkflowOutput(BaseModel):
    ...     dag_is_complete: bool = Field(..., description="Whether the DAG is
    fully defined and ready")
    ...     dag_is_concurrent: bool = Field(..., description="Whether the DAG
    has maximized concurrency")
    ...     dag_is_acyclic: bool = Field(..., description="Whether the DAG
    contains no cycles")
    ...     adjusted_node_list: str = Field(..., description="Comma‑separated
    list of node names that were adjusted during finalization")
    ...     dag_summary: str = Field(..., description="Human‑readable summary of
    the finalized DAG")
    >>> def finalize_workflow(refine_dag_input: RefineDagOutput, **kwargs) ->
    FinalizeWorkflowOutput:
    ...     import logging
    ...     import re
    ...     logger = logging.getLogger(__name__)
    ...     if not refine_dag_input.dag_edges:
    ...         logger.error("dag_edges list is empty")
    ...         raise ValueError("dag_edges list is empty or contains malformed
    entries")
    ...     edge_pattern = re.compile(r'^\s*([^\s]+)\s*->\s*([^\s]+)\s*$')
    ...     nodes = set()
    ...     for edge in refine_dag_input.dag_edges:
    ...         m = edge_pattern.match(edge)
    ...         if not m:
    ...             logger.error("malformed edge: %s", edge)
    ...             raise ValueError("dag_edges list is empty or contains
    malformed entries")
    ...         src, dst = m.group(1), m.group(2)
    ...         nodes.update([src, dst])
    ...     node_count = len(nodes)
    ...     edge_count = len(refine_dag_input.dag_edges)
    ...     dag_is_complete = node_count > 0 and edge_count > 0
    ...     dag_is_concurrent = refine_dag_input.is_concurrent
    ...     dag_is_acyclic = refine_dag_input.is_acyclic
    ...     adjusted = []
    ...     if not dag_is_concurrent:
    ...         adjusted.append("SyncNode")
    ...     if not dag_is_acyclic:
    ...         adjusted.append("CycleBreaker")
    ...     adjusted_node_list = ",".join(adjusted)
    ...     dag_summary = f"DAG has {node_count} nodes and {edge_count} edges.
    Acyclic: {dag_is_acyclic}. Concurrency: {'maximized' if dag_is_concurrent
    else 'not maximized'}."
    ...     return FinalizeWorkflowOutput(
    ...         dag_is_complete=dag_is_complete,
    ...         dag_is_concurrent=dag_is_concurrent,
    ...         dag_is_acyclic=dag_is_acyclic,
    ...         adjusted_node_list=adjusted_node_list,
    ...         dag_summary=dag_summary
    ...     )
    >>> # Example usage:
    >>> refine_output = RefineDagOutput(dag_edges=['A->B', 'B->C'],
    is_acyclic=True, is_concurrent=False, max_concurrency=2)
    >>> result = finalize_workflow(refine_output)
    >>> print(result.dag_summary)
    DAG has 3 nodes and 2 edges. Acyclic: True. Concurrency: not maximized.

    """
    logger = logging.getLogger(__name__)
    if not refine_dag_input.dag_edges:
        logger.error("dag_edges list is empty")
        raise ValueError("dag_edges list is empty or contains malformed entries")
    edge_pattern = re.compile(r'^\s*([^\s]+)\s*->\s*([^\s]+)\s*$')
    nodes = set()
    for edge in refine_dag_input.dag_edges:
        m = edge_pattern.match(edge)
        if not m:
            logger.error("malformed edge: %s", edge)
            raise ValueError("dag_edges list is empty or contains malformed entries")
        src, dst = m.group(1), m.group(2)
        nodes.update([src, dst])
    node_count = len(nodes)
    edge_count = len(refine_dag_input.dag_edges)
    dag_is_complete = node_count > 0 and edge_count > 0
    dag_is_concurrent = refine_dag_input.is_concurrent
    dag_is_acyclic = refine_dag_input.is_acyclic
    adjusted = []
    if not dag_is_concurrent:
        adjusted.append("SyncNode")
    if not dag_is_acyclic:
        adjusted.append("CycleBreaker")
    adjusted_node_list = ",".join(adjusted)
    dag_summary = f"DAG has {node_count} nodes and {edge_count} edges. Acyclic: {dag_is_acyclic}. Concurrency: {'maximized' if dag_is_concurrent else 'not maximized'}."
    return FinalizeWorkflowOutput(
        dag_is_complete=dag_is_complete,
        dag_is_concurrent=dag_is_concurrent,
        dag_is_acyclic=dag_is_acyclic,
        adjusted_node_list=adjusted_node_list,
        dag_summary=dag_summary
    )