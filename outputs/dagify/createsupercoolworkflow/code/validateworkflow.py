from ._validateworkflow.validate_input_type_and_empty import validate_input_type_and_empty
from ._validateworkflow.validate_node_names_are_strings import validate_node_names_are_strings
from ._validateworkflow.analyze_node_dependencies import analyze_node_dependencies
from ._validateworkflow.check_for_circular_dependencies import check_for_circular_dependencies
from ._validateworkflow.validate_node_connectivity import validate_node_connectivity
from ._validateworkflow.validate_node_schemas import validate_node_schemas
from ._validateworkflow.validate_execution_path import validate_execution_path
from ._validateworkflow.generate_validation_error_message import generate_validation_error_message

from pydantic import BaseModel, Field
from typing import List


class ConnectnodesOutput(BaseModel):
    """Pydantic model for connectnodes node outputs."""
    connected_nodes: List[str] = (
        Field(..., description="List of connected node names")
    )


class ValidateworkflowOutput(BaseModel):
    """Pydantic model for validateworkflow node outputs."""
    validation_result: bool = (
        Field(..., description="Result of the workflow validation")
    )
    validation_message: str = (
        Field(..., description="Message indicating the outcome of the validation")
    )


def validateworkflow(connectnodes_input: ConnectnodesOutput, **kwargs) -> ValidateworkflowOutput:
    """
    Validate the workflow to ensure it is correct and functional.

    Parameters
    ----------
    connected_nodes : List[str]
        List of connected node names from the 'connectnodes' node.

    Returns
    -------
    Tuple[bool, str]
        A tuple containing the validation result (bool) and a message
        indicating the outcome of the validation (str).

    Raises
    ------
    ValueError
        If the input 'connected_nodes' is not a list or is empty.
    TypeError
        If the 'connected_nodes' list contains non-string values.

    Examples
    --------
    >>> connected_nodes = ['node1', 'node2']
    >>> validation_result, validation_message =
    validateworkflow(connected_nodes)
    (True, 'Workflow is valid.')

    >>> connected_nodes = []
    >>> try:
    ...     validation_result, validation_message =
    validateworkflow(connected_nodes)
    >>> except ValueError as e:
    ...     print(e)
    'connected_nodes' cannot be empty.

    """
    connected_nodes: List[str] = connectnodes_input.connected_nodes
    
    validate_input_type_and_empty(connected_nodes=connected_nodes)
    validate_node_names_are_strings(connected_nodes=connected_nodes)
    
    node_dependencies: dict = analyze_node_dependencies(connected_nodes=connected_nodes)
    cycle_check_result: bool = check_for_circular_dependencies(dependencies=node_dependencies)
    
    if not cycle_check_result:
        return ValidateworkflowOutput(
            validation_result=False,
            validation_message="Circular dependencies detected in workflow"
        )
    
    connectivity_valid: bool = validate_node_connectivity(connected_nodes=connected_nodes)
    schema_valid: bool = validate_node_schemas(connected_nodes=connected_nodes)
    execution_path_valid: bool = validate_execution_path(connected_nodes=connected_nodes)
    
    if connectivity_valid and schema_valid and execution_path_valid:
        return ValidateworkflowOutput(
            validation_result=True,
            validation_message="Workflow is valid."
        )
    else:
        error_details: str = generate_validation_error_message(
            connectivity_valid=connectivity_valid,
            schema_valid=schema_valid,
            execution_path_valid=execution_path_valid
        )
        return ValidateworkflowOutput(
            validation_result=False,
            validation_message=error_details
        )