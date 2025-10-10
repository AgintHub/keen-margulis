from ._finalize_workflow.parse_cycles_from_string import parse_cycles_from_string
from ._finalize_workflow.parse_missing_dependencies_from_string import parse_missing_dependencies_from_string
from ._finalize_workflow.remove_cycles_from_dag import remove_cycles_from_dag
from ._finalize_workflow.generate_cycle_removal_warnings import generate_cycle_removal_warnings
from ._finalize_workflow.resolve_missing_dependencies import resolve_missing_dependencies
from ._finalize_workflow.generate_dependency_warnings import generate_dependency_warnings
from ._finalize_workflow.topological_sort_tasks import topological_sort_tasks
from ._finalize_workflow.generate_dag_representation import generate_dag_representation
from ._finalize_workflow.check_final_dag_validity import check_final_dag_validity
from ._finalize_workflow.generate_summary import generate_summary
from ._finalize_workflow.serialize_task_list import serialize_task_list
from ._finalize_workflow.serialize_dependencies_list import serialize_dependencies_list
from ._finalize_workflow.serialize_cycles_list import serialize_cycles_list
from ._finalize_workflow.serialize_warnings_list import serialize_warnings_list

from pydantic import BaseModel, Field


class ValidateDagOutput(BaseModel):
    """Pydantic model for validate_dag node outputs."""
    is_valid: bool = (
        Field(..., description = (
            "Indicates whether the DAG passes all validation checks.")
        )
    )
    node_count: int = (
        Field(..., description="Total number of nodes present in the DAG.")
    )
    edge_count: int = (
        Field(..., description="Total number of directed edges in the DAG.")
    )
    cycles_detected: str = (
        Field(..., description = (
            "List of cycle identifiers or descriptions found in the DAG (empty if none).")
        )
    )
    missing_dependencies: str = (
        Field(..., description = (
            "List of node names that reference non\u2011existent dependencies (empty if none).")
        )
    )
    errors: str = (
        Field(..., description = (
            "Detailed error messages for any validation failures.")
        )
    )


class FinalizeWorkflowOutput(BaseModel):
    """Pydantic model for finalize_workflow node outputs."""
    dag_representation: str = (
        Field(..., description = (
            "String representation of the finalized DAG, e.g., serialized adjacency list or other format.")
        )
    )
    is_valid: bool = (
        Field(..., description = (
            "Whether the finalized DAG is valid and acyclic.")
        )
    )
    adjustments_made: bool = (
        Field(..., description = (
            "Whether any adjustments were made to the DAG during finalization.")
        )
    )
    adjusted_task_order: str = (
        Field(..., description = (
            "Ordered list of task identifiers in the finalized DAG.")
        )
    )
    missing_dependencies: str = (
        Field(..., description = (
            "List of task identifiers that have missing or unresolved dependencies.")
        )
    )
    cycles_detected: str = (
        Field(..., description="List of detected cycles in the DAG, if any.")
    )
    warnings: str = (
        Field(..., description="Any warnings or notes about potential issues.")
    )
    summary: str = (
        Field(..., description = (
            "Short textual summary of the finalized workflow.")
        )
    )


def finalize_workflow(validate_dag_input: ValidateDagOutput, **kwargs) -> FinalizeWorkflowOutput:
    """
    Finalize a workflow DAG by validating its structure, resolving missing
    dependencies, removing cycles, and ordering tasks.

    Parameters
    ----------
    task_ids : List[str]
        Unique identifiers of all tasks in the DAG.
    edge_sources : List[str]
        Source task identifiers for each directed edge.
    edge_destinations : List[str]
        Destination task identifiers for each directed edge.
    is_valid : bool
        Result of the validation step (True if the DAG passed all checks).
    node_count : int
        Total number of nodes in the DAG.
    edge_count : int
        Total number of directed edges in the DAG.
    cycles_detected : List[str]
        List of cycle identifiers found during validation.
    missing_dependencies : List[str]
        List of node names that reference non‑existent dependencies.
    errors : List[str]
        Detailed error messages from the validation step.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the finalized DAG representation and
        metadata: dag_representation (str), is_valid (bool),
        adjustments_made (bool), adjusted_task_order (List[str]),
        missing_dependencies (List[str]), cycles_detected (List[str]),
        warnings (List[str]), and summary (str).

    Raises
    ------
    ValueError
        If any required input lists are empty or lengths of edge_sources and
        edge_destinations mismatch.

    Examples
    --------
    >>> dag = finalize_workflow(

    ...     task_ids=['A', 'B', 'C'],

    ...     edge_sources=['A', 'B'],

    ...     edge_destinations=['B', 'C'],

    ...     is_valid=True,

    ...     node_count=3,

    ...     edge_count=2,

    ...     cycles_detected=[],

    ...     missing_dependencies=[],

    ...     errors=[]

    >>> )
    {'dag_representation': 'A -> B -> C', 'is_valid': True, 'adjustments_made':
    False, 'adjusted_task_order': ['A', 'B', 'C'], 'missing_dependencies': [],
    'cycles_detected': [], 'warnings': [], 'summary': 'DAG finalized
    successfully.'}

    >>> dag = finalize_workflow(

    ...     task_ids=['A', 'B', 'C'],

    ...     edge_sources=['A', 'B', 'C'],

    ...     edge_destinations=['B', 'C', 'A'],

    ...     is_valid=False,

    ...     node_count=3,

    ...     edge_count=3,

    ...     cycles_detected=['A->B->C->A'],

    ...     missing_dependencies=[],

    ...     errors=['Cycle detected']

    >>> )
    {'dag_representation': 'A -> B -> C', 'is_valid': False, 'adjustments_made':
    True, 'adjusted_task_order': ['A', 'B', 'C'], 'missing_dependencies': [],
    'cycles_detected': ['A->B->C->A'], 'warnings': ['Cycle removed:
    A->B->C->A'], 'summary': 'DAG finalized with cycle removal.'}

    """
    parsed_cycles: list = parse_cycles_from_string(cycles_str=validate_dag_input.cycles_detected)
    parsed_missing_deps: list = parse_missing_dependencies_from_string(deps_str=validate_dag_input.missing_dependencies)
    
    adjustments_made: bool = False
    warnings: list = []
    
    if not validate_dag_input.is_valid:
        if parsed_cycles:
            remove_cycles_from_dag(cycles=parsed_cycles)
            warnings.extend(generate_cycle_removal_warnings(cycles=parsed_cycles))
            adjustments_made = True
        
        if parsed_missing_deps:
            resolve_missing_dependencies(missing_deps=parsed_missing_deps)
            warnings.extend(generate_dependency_warnings(missing_deps=parsed_missing_deps))
            adjustments_made = True
    
    ordered_tasks: list = topological_sort_tasks(node_count=validate_dag_input.node_count, edge_count=validate_dag_input.edge_count)
    dag_representation: str = generate_dag_representation(task_order=ordered_tasks)
    final_validity: bool = check_final_dag_validity(is_originally_valid=validate_dag_input.is_valid, adjustments_made=adjustments_made)
    summary: str = generate_summary(is_valid=final_validity, adjustments_made=adjustments_made, cycles_removed=bool(parsed_cycles))
    
    return FinalizeWorkflowOutput(
        dag_representation=dag_representation,
        is_valid=final_validity,
        adjustments_made=adjustments_made,
        adjusted_task_order=serialize_task_list(tasks=ordered_tasks),
        missing_dependencies=serialize_dependencies_list(deps=parsed_missing_deps),
        cycles_detected=serialize_cycles_list(cycles=parsed_cycles),
        warnings=serialize_warnings_list(warnings=warnings),
        summary=summary
    )