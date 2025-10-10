from ._connectnodes.validate_node_names import validate_node_names
from ._connectnodes.check_cyclic_dependency import check_cyclic_dependency
from ._connectnodes.establish_dag_connection import establish_dag_connection

from pydantic import BaseModel, Field
from typing import List


class Definenode1Output(BaseModel):
    """Pydantic model for definenode1 node outputs."""
    node1_name: str = Field(..., description="Name of the first node")
    node1_description: str = (
        Field(..., description="Description of the first node")
    )
    node1_output_structure: List[str] = (
        Field(..., description="Output structure of the first node")
    )


class Definenode2Output(BaseModel):
    """Pydantic model for definenode2 node outputs."""
    node2_name: str = Field(..., description="Name of the second node")
    node2_description: str = (
        Field(..., description="Description of the second node")
    )
    node2_output_structure: List[str] = (
        Field(..., description="Output structure of the second node")
    )


class ConnectnodesOutput(BaseModel):
    """Pydantic model for connectnodes node outputs."""
    connected_nodes: List[str] = (
        Field(..., description="List of connected node names")
    )


def connectnodes(definenode1_input: Definenode1Output, definenode2_input: Definenode2Output, **kwargs) -> ConnectnodesOutput:
    """
    Connects the defined nodes in the workflow.

    Parameters
    ----------
    node1_name : str
        Name of the first node from definenode1 output.
    node2_name : str
        Name of the second node from definenode2 output.

    Returns
    -------
    List[str]
        A list containing the names of the connected nodes.

    Raises
    ------
    ValueError
        If either node1_name or node2_name is empty or not a string.
    ConnectionError
        If the nodes cannot be connected due to a cyclic dependency.

    Examples
    --------
    >>> node1 = 'node_a'
    >>> node2 = 'node_b'
    >>> connect_nodes(node1, node2)
    ['node_a', 'node_b']

    >>> node1 = 'data_processing'
    >>> node2 = 'data_analysis'
    >>> connect_nodes(node1, node2)
    ['data_processing', 'data_analysis']

    """
    node1_name: str = definenode1_input.node1_name
    node2_name: str = definenode2_input.node2_name
    
    validate_node_names(node1_name=node1_name, node2_name=node2_name)
    
    check_cyclic_dependency(node1_name=node1_name, node2_name=node2_name)
    
    connection_result: List[str] = establish_dag_connection(node1=node1_name, node2=node2_name)
    
    return ConnectnodesOutput(connected_nodes=connection_result)