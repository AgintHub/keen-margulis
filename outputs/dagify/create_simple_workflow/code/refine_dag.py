from ._refine_dag.validate_dag_input import validate_dag_input
from ._refine_dag.build_adjacency_graph import build_adjacency_graph
from ._refine_dag.verify_dag_acyclicity import verify_dag_acyclicity
from ._refine_dag.compute_topological_levels import compute_topological_levels
from ._refine_dag.calculate_concurrency_stats import calculate_concurrency_stats
from ._refine_dag.reorder_edges_by_topology import reorder_edges_by_topology

import logging
from typing import Dict
from pydantic import BaseModel, Field


from typing import Any


class CreateTaskDagOutput(BaseModel):
    dag_nodes: list[str] = (
        Field(..., description="Ordered list of task identifiers in the DAG.")
    )
    dag_edges: list[str] = (
        Field(..., description = (
            "List of edges representing dependencies, formatted as 'source->target'.")
        )
    )
    is_acyclic: bool = (
        Field(..., description = (
            "Indicates whether the constructed DAG is acyclic.")
        )
    )

class RefineDagOutput(BaseModel):
    dag_edges: list[str] = (
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
    
    validate_dag_input(dag_nodes=dag_nodes, dag_edges=dag_edges)
    
    adjacency_data: Dict[str, Any] = build_adjacency_graph(dag_nodes=dag_nodes, dag_edges=dag_edges)
    
    is_acyclic_check: bool = verify_dag_acyclicity(adjacency_data=adjacency_data, dag_nodes=dag_nodes)
    if not is_acyclic_check:
        raise ValueError("Cycle detected in DAG")
    
    level_structure: Dict[str, Any] = compute_topological_levels(adjacency_data=adjacency_data, dag_nodes=dag_nodes)
    
    concurrency_metrics: Dict[str, Any] = calculate_concurrency_stats(level_structure=level_structure)
    
    reordered_edges: list[str] = reorder_edges_by_topology(dag_edges=dag_edges, level_structure=level_structure)
    
    return RefineDagOutput(
        dag_edges=reordered_edges,
        is_acyclic=True,
        is_concurrent=concurrency_metrics["is_concurrent"],
        max_concurrency=concurrency_metrics["max_concurrency"]
    )