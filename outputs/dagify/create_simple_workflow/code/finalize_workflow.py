from ._finalize_workflow.validate_dag_edges import validate_dag_edges
from ._finalize_workflow.extract_nodes_from_edges import extract_nodes_from_edges
from ._finalize_workflow.check_dag_completeness import check_dag_completeness
from ._finalize_workflow.determine_adjustments import determine_adjustments
from ._finalize_workflow.generate_dag_summary import generate_dag_summary
from ._finalize_workflow.log_finalization_results import log_finalization_results

from pydantic import BaseModel, Field
from typing import List
import logging


class RefineDagOutput(BaseModel):
    dag_edges: List[str] = (
        Field(..., description = (
            "List of directed edges in the refined DAG, formatted as 'TaskA->TaskB'.")
        )
    )
    is_acyclic: bool = (
        Field(..., description = (
            "Indicates whether the refined DAG contains any cycles.")
        )
    )
    is_concurrent: bool = (
        Field(..., description = (
            "Indicates whether the DAG has been adjusted to allow concurrent execution of independent tasks.")
        )
    )
    max_concurrency: int = (
        Field(..., description = (
            "Maximum number of tasks that can run concurrently in the refined DAG.")
        )
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
        Field(..., description = (
            "Comma‑separated list of node names that were adjusted during finalization")
        )
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
    
    validated_edges: List[str] = validate_dag_edges(edges=refine_dag_input.dag_edges, logger=logger)
    
    nodes: set = extract_nodes_from_edges(edges=validated_edges)
    node_count: int = len(nodes)
    edge_count: int = len(validated_edges)
    
    dag_is_complete: bool = check_dag_completeness(node_count=node_count, edge_count=edge_count)
    dag_is_concurrent: bool = refine_dag_input.is_concurrent
    dag_is_acyclic: bool = refine_dag_input.is_acyclic
    
    adjusted_nodes: List[str] = determine_adjustments(is_concurrent=dag_is_concurrent, is_acyclic=dag_is_acyclic)
    adjusted_node_list: str = ",".join(adjusted_nodes)
    
    dag_summary: str = generate_dag_summary(
        node_count=node_count,
        edge_count=edge_count,
        is_acyclic=dag_is_acyclic,
        is_concurrent=dag_is_concurrent
    )
    
    log_finalization_results(logger=logger, summary=dag_summary, adjustments=adjusted_nodes)
    
    return FinalizeWorkflowOutput(
        dag_is_complete=dag_is_complete,
        dag_is_concurrent=dag_is_concurrent,
        dag_is_acyclic=dag_is_acyclic,
        adjusted_node_list=adjusted_node_list,
        dag_summary=dag_summary
    )