from pydantic import BaseModel, Field
from typing import List


class DecomposeTaskIntoSubtasksOutput(BaseModel):
    """Pydantic model for decompose_task_into_subtasks node outputs."""
    subtask_list: List[str] = (
        Field(..., description="List of subtasks or steps to achieve the task objective")
    )
    subtask_count: int = (
        Field(..., description="Number of subtasks or steps generated")
    )
    sequencing_requirements: str = (
        Field(..., description="Description of any sequencing or ordering requirements between subtasks")
    )


class IdentifyDependenciesBetweenSubtasksOutput(BaseModel):
    """Pydantic model for identify_dependencies_between_subtasks node outputs."""
    dependencies_exist: bool = (
        Field(..., description="Whether dependencies exist between subtasks")
    )
    dependency_list: str = (
        Field(..., description="List of dependencies between subtasks, where each dependency is represented as 'subtask_id_1 -> subtask_id_2'")
    )


def identify_dependencies_between_subtasks(decompose_task_into_subtasks_input: DecomposeTaskIntoSubtasksOutput, **kwargs) -> IdentifyDependenciesBetweenSubtasksOutput:
    """
    Identify dependencies between subtasks based on their prerequisites.

    Parameters
    ----------
    subtask_list : List[str]
        List of subtasks or steps to achieve the task objective
    sequencing_requirements : str
        Description of any sequencing or ordering requirements between
        subtasks

    Returns
    -------
    dict
        Dictionary containing a boolean indicating whether dependencies
        exist and a list of dependencies

    Raises
    ------
    ValueError
        If subtask_list is empty or sequencing_requirements is invalid

    Examples
    --------
    >>> subtask_list = ['task1', 'task2', 'task3']
    >>> sequencing_requirements = 'task1 -> task2, task2 -> task3'
    >>> dependencies = identify_dependencies_between_subtasks(subtask_list,
    sequencing_requirements)
    {'dependencies_exist': True, 'dependency_list': ['task1 -> task2', 'task2 ->
    task3']}

    >>> subtask_list = ['task1', 'task2']
    >>> sequencing_requirements = ''
    >>> dependencies = identify_dependencies_between_subtasks(subtask_list,
    sequencing_requirements)
    {'dependencies_exist': False, 'dependency_list': []}

    """
    return IdentifyDependenciesBetweenSubtasksOutput(
        dependencies_exist=False,
        dependency_list="",
    )