from pydantic import BaseModel, Field
from typing import List


class CreateDagStructureOutput(BaseModel):
    """Pydantic model for create_dag_structure node outputs."""
    dag_nodes: List[str] = (
        Field(..., description="List of node names in the DAG")
    )
    dag_edges: List[str] = (
        Field(..., description="List of edges in the DAG, represented as 'node1->node2'")
    )
    root_nodes: List[str] = (
        Field(..., description="List of root node names in the DAG")
    )
    is_valid_dag: bool = (
        Field(..., description="Whether the constructed DAG is valid")
    )


class DefineNodePromptsAndDescriptionsOutput(BaseModel):
    """Pydantic model for define_node_prompts_and_descriptions node outputs."""
    node_names: List[str] = (
        Field(..., description="List of all node names in the DAG.")
    )
    node_prompts: List[str] = (
        Field(..., description="List of prompts corresponding to each node name.")
    )
    node_descriptions: List[str] = (
        Field(..., description="List of descriptions corresponding to each node name.")
    )


def define_node_prompts_and_descriptions(create_dag_structure_input: CreateDagStructureOutput, **kwargs) -> DefineNodePromptsAndDescriptionsOutput:
    """
    Generate node prompts and descriptions from the DAG structure.

    Parameters
    ----------
    dag_nodes : List[str]
        List of node names from the DAG structure.
    dag_edges : List[str]
        List of edges in the DAG, represented as 'node1->node2'.
    root_nodes : List[str]
        List of root node names in the DAG.
    is_valid_dag : bool
        Whether the constructed DAG is valid.

    Returns
    -------
    dict
        A dictionary containing lists of node names, prompts, and
        descriptions.

    Raises
    ------
    ValueError
        If the input DAG structure is invalid or empty.

    Examples
    --------
    >>> node_names = ['A', 'B', 'C']
    >>> node_prompts = ['Task A', 'Task B', 'Task C']
    >>> node_descriptions = ['Description A', 'Description B', 'Description C']
    >>> result = define_node_prompts_and_descriptions(node_names, node_prompts,
    node_descriptions)
    {'node_names': ['A', 'B', 'C'], 'node_prompts': ['Task A', 'Task B', 'Task
    C'], 'node_descriptions': ['Description A', 'Description B', 'Description
    C']}

    """
    return DefineNodePromptsAndDescriptionsOutput(
        node_names=[],
        node_prompts=[],
        node_descriptions=[],
    )