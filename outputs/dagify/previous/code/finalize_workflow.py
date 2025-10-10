from pydantic import BaseModel, Field


class ValidateDagOutput(BaseModel):
    """Pydantic model for validate_dag node outputs."""
    is_valid: bool = (
        Field(..., description="Indicates whether the DAG passes all validation checks.")
    )
    node_count: int = (
        Field(..., description="Total number of nodes present in the DAG.")
    )
    edge_count: int = (
        Field(..., description="Total number of directed edges in the DAG.")
    )
    cycles_detected: str = (
        Field(..., description="List of cycle identifiers or descriptions found in the DAG (empty if none).")
    )
    missing_dependencies: str = (
        Field(..., description="List of node names that reference non\u2011existent dependencies (empty if none).")
    )
    errors: str = (
        Field(..., description="Detailed error messages for any validation failures.")
    )


class FinalizeWorkflowOutput(BaseModel):
    """Pydantic model for finalize_workflow node outputs."""
    dag_representation: str = (
        Field(..., description="String representation of the finalized DAG, e.g., serialized adjacency list or other format.")
    )
    is_valid: bool = (
        Field(..., description="Whether the finalized DAG is valid and acyclic.")
    )
    adjustments_made: bool = (
        Field(..., description="Whether any adjustments were made to the DAG during finalization.")
    )
    adjusted_task_order: str = (
        Field(..., description="Ordered list of task identifiers in the finalized DAG.")
    )
    missing_dependencies: str = (
        Field(..., description="List of task identifiers that have missing or unresolved dependencies.")
    )
    cycles_detected: str = (
        Field(..., description="List of detected cycles in the DAG, if any.")
    )
    warnings: str = (
        Field(..., description="Any warnings or notes about potential issues.")
    )
    summary: str = (
        Field(..., description="Short textual summary of the finalized workflow.")
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
    return FinalizeWorkflowOutput(
        dag_representation="",
        is_valid=False,
        adjustments_made=False,
        adjusted_task_order="",
        missing_dependencies="",
        cycles_detected="",
        warnings="",
        summary="",
    )