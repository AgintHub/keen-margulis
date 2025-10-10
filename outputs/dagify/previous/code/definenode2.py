from ._definenode2.validate_workflow_inputs import validate_workflow_inputs
from ._definenode2.generate_node_name import generate_node_name
from ._definenode2.create_node_description import create_node_description
from ._definenode2.define_output_structure import define_output_structure

from pydantic import BaseModel, Field
from typing import List


class InitializeworkflowOutput(BaseModel):
    """Pydantic model for initializeworkflow node outputs."""
    workflow_id: str = (
        Field(..., description="Unique identifier for the workflow")
    )
    workflow_name: str = Field(..., description="Name of the workflow")


class Definenode2Output(BaseModel):
    """Pydantic model for definenode2 node outputs."""
    node2_name: str = Field(..., description="Name of the second node")
    node2_description: str = (
        Field(..., description="Description of the second node")
    )
    node2_output_structure: List[str] = (
        Field(..., description="Output structure of the second node")
    )


def definenode2(initializeworkflow_input: InitializeworkflowOutput, **kwargs) -> Definenode2Output:
    """
    Defines the second node in the workflow with required details.

    Parameters
    ----------
    workflow_id : str
        Unique identifier for the workflow from the parent node
        'initializeworkflow'.
    workflow_name : str
        Name of the workflow from the parent node 'initializeworkflow'.

    Returns
    -------
    Tuple[str, str, List[str]]
        A tuple containing the name, description, and output structure of
        the second node.

    Raises
    ------
    ValueError
        If the workflow_id or workflow_name is invalid or missing.

    Examples
    --------
    >>> workflow_id = 'wf_123'
    >>> workflow_name = 'Super Cool Workflow'
    >>> node2_name = 'Node 2'
    >>> node2_description = 'This is the second node.'
    >>> node2_output_structure = ['output1', 'output2']
    >>> definenode2(workflow_id, workflow_name, node2_name, node2_description,
    node2_output_structure)
    ('Node 2', 'This is the second node.', ['output1', 'output2'])

    """
    validated_workflow: bool = validate_workflow_inputs(workflow_id=initializeworkflow_input.workflow_id, workflow_name=initializeworkflow_input.workflow_name)
    if not validated_workflow:
        raise ValueError("Invalid workflow_id or workflow_name")
    
    node2_name: str = generate_node_name(workflow_context=initializeworkflow_input, node_position=2)
    node2_description: str = create_node_description(workflow_name=initializeworkflow_input.workflow_name, node_name=node2_name)
    node2_output_structure: List[str] = define_output_structure(workflow_id=initializeworkflow_input.workflow_id, node_type="second_node")
    
    return Definenode2Output(
        node2_name=node2_name,
        node2_description=node2_description,
        node2_output_structure=node2_output_structure,
    )