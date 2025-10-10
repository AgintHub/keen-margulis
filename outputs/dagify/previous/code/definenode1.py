from ._definenode1.validate_workflow_inputs import validate_workflow_inputs
from ._definenode1.generate_node_name import generate_node_name
from ._definenode1.create_node_description import create_node_description
from ._definenode1.define_output_structure import define_output_structure

from pydantic import BaseModel, Field
from typing import List


class InitializeworkflowOutput(BaseModel):
    """Pydantic model for initializeworkflow node outputs."""
    workflow_id: str = (
        Field(..., description="Unique identifier for the workflow")
    )
    workflow_name: str = Field(..., description="Name of the workflow")


class Definenode1Output(BaseModel):
    """Pydantic model for definenode1 node outputs."""
    node1_name: str = Field(..., description="Name of the first node")
    node1_description: str = (
        Field(..., description="Description of the first node")
    )
    node1_output_structure: List[str] = (
        Field(..., description="Output structure of the first node")
    )


def definenode1(initializeworkflow_input: InitializeworkflowOutput, **kwargs) -> Definenode1Output:
    """
    Defines the first node in the workflow with the required details.

    Parameters
    ----------
    workflow_id : str
        Unique identifier for the workflow obtained from the parent node
        'initializeworkflow'.
    workflow_name : str
        Name of the workflow obtained from the parent node
        'initializeworkflow'.

    Returns
    -------
    Tuple[str, str, List[str]]
        A tuple containing the name, description, and output structure of
        the first node.

    Raises
    ------
    ValueError
        If the workflow_id or workflow_name is empty or not provided.

    Examples
    --------
    >>> definenode1(workflow_id='wf_123', workflow_name='My Workflow')
    ...   node1_name = 'Node 1'
    ...   node1_description = 'This is the first node.'
    ...   node1_output_structure = ['output1', 'output2']
    ...   return node1_name, node1_description, node1_output_structure
    ('Node 1', 'This is the first node.', ['output1', 'output2'])

    """
    validate_workflow_inputs(workflow_id=initializeworkflow_input.workflow_id, workflow_name=initializeworkflow_input.workflow_name)
    
    node_name: str = generate_node_name(workflow_name=initializeworkflow_input.workflow_name)
    node_description: str = create_node_description(workflow_id=initializeworkflow_input.workflow_id, workflow_name=initializeworkflow_input.workflow_name)
    output_structure: List[str] = define_output_structure(workflow_context=initializeworkflow_input)
    
    return Definenode1Output(
        node1_name=node_name,
        node1_description=node_description,
        node1_output_structure=output_structure
    )