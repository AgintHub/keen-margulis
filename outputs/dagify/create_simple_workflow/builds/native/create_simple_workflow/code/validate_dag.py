from pydantic import BaseModel, Field


class CreateTaskDagOutput(BaseModel):
    """Pydantic model for create_task_dag node outputs."""
    task_ids: str = (
        Field(..., description = (
            "List of unique task identifiers used in the DAG")
        )
    )
    edge_sources: str = (
        Field(..., description = (
            "List of source task identifiers for each directed edge in the DAG")
        )
    )
    edge_destinations: str = (
        Field(..., description = (
            "List of destination task identifiers for each directed edge in the DAG")
        )
    )
    is_valid: bool = (
        Field(..., description = (
            "Indicates whether the constructed DAG is acyclic and complete")
        )
    )


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


def validate_dag(create_task_dag_input: CreateTaskDagOutput, **kwargs) -> ValidateDagOutput:
    """
    Validates a Directed Acyclic Graph (DAG) representation for correctness,
    acyclicity, and missing dependencies.

    Parameters
    ----------
    task_ids : List[str]
        List of unique identifiers for all tasks in the workflow.
    edge_sources : List[str]
        List of task identifiers representing the source of each directed
        edge.
    edge_destinations : List[str]
        List of task identifiers representing the destination of each
        directed edge.
    is_valid_input : bool
        (Optional) A flag from `create_task_dag` indicating preliminary
        validity. It is used only as a hint; full validation is performed
        regardless.

    Returns
    -------
    dict
        Dictionary containing validation results: - `is_valid` (bool):
        Overall validity. - `node_count` (int): Number of nodes. -
        `edge_count` (int): Number of directed edges. - `cycles_detected`
        (List[str]): Descriptions of any detected cycles. -
        `missing_dependencies` (List[str]): Tasks that reference undefined
        dependencies. - `errors` (List[str]): Human‑readable error messages
        for all failures.

    Raises
    ------
    ValueError
        If `edge_sources` and `edge_destinations` lists are not of the same
        length.
    ValueError
        If `task_ids` contains duplicate identifiers.

    Examples
    --------
    >>> task_ids = ['A', 'B', 'C']
    >>> edge_sources = ['A', 'B']
    >>> edge_destinations = ['B', 'C']
    >>> result = validate_dag(task_ids, edge_sources, edge_destinations)
    >>> print(result)
    {'is_valid': True, 'node_count': 3, 'edge_count': 2, 'cycles_detected': [],
    'missing_dependencies': [], 'errors': []}

    >>> task_ids = ['A', 'B', 'C']
    >>> edge_sources = ['A', 'B', 'C']
    >>> edge_destinations = ['B', 'C', 'A']
    >>> result = validate_dag(task_ids, edge_sources, edge_destinations)
    >>> print(result)
    {'is_valid': False, 'node_count': 3, 'edge_count': 3, 'cycles_detected': ['A
    -> B -> C -> A'], 'missing_dependencies': [], 'errors': ['Cycle detected: A
    -> B -> C -> A']}

    """
    return ValidateDagOutput(
        is_valid=False,
        node_count=0,
        edge_count=0,
        cycles_detected="",
        missing_dependencies="",
        errors="",
    )