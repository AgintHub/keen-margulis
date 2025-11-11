from ._define_node_outputs.validate_task_list import validate_task_list
from ._define_node_outputs.determine_output_type import determine_output_type
from ._define_node_outputs.create_output_structure import create_output_structure

from pydantic import BaseModel, Field
from typing import List


class DecomposeObjectiveOutput(BaseModel):
    """Pydantic model for decompose_objective node outputs."""
    task_list: List[str] = (
        Field(..., description="List of decomposed tasks or steps")
    )


class DefineNodeOutputsOutput(BaseModel):
    """Pydantic model for define_node_outputs node outputs."""
    node_outputs: List[str] = (
        Field(..., description="List containing output structures for each node")
    )


def define_node_outputs(decompose_objective_input: DecomposeObjectiveOutput, **kwargs) -> DefineNodeOutputsOutput:
    """
    Defines the output structure for each node based on the decomposed tasks.

    Parameters
    ----------
    task_list : List[str]
        List of decomposed tasks or steps from the decompose_objective node.

    Returns
    -------
    List[str]
        A list of output structures for each node in the workflow DAG.

    Raises
    ------
    ValueError
        If the task_list is empty or not a list.

    Examples
    --------
    >>> task_list = ['task1', 'task2']
    >>> node_outputs = define_node_outputs(task_list)
    ['{"task": "task1", "output_type": "str"}', '{"task": "task2",
    "output_type": "int"}']

    >>> task_list = ['data_ingestion', 'data_processing']
    >>> node_outputs = define_node_outputs(task_list)
    ['{"task": "data_ingestion", "output_type": "DataFrame"}', '{"task":
    "data_processing", "output_type": "DataFrame"}']

    """
    task_list: List[str] = decompose_objective_input.task_list
    
    validated_tasks: List[str] = validate_task_list(task_list=task_list)
    
    output_structures: List[str] = []
    for task in validated_tasks:
        output_type: str = determine_output_type(task=task)
        structure: str = create_output_structure(task=task, output_type=output_type)
        output_structures.append(structure)
    
    return DefineNodeOutputsOutput(node_outputs=output_structures)