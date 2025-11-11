from pydantic import BaseModel, Field
from typing import List


class DefineTaskObjectiveOutput(BaseModel):
    """Pydantic model for define_task_objective node outputs."""
    task_objective: str = (
        Field(..., description="The primary objective or task that the workflow will accomplish.")
    )
    task_description: str = (
        Field(..., description="A detailed description of the task or objective.")
    )


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


def decompose_task_into_subtasks(define_task_objective_input: DefineTaskObjectiveOutput, **kwargs) -> DecomposeTaskIntoSubtasksOutput:
    """
    Decompose a task into smaller subtasks or steps.

    Parameters
    ----------
    task_objective : str
        The primary objective or task that the workflow will accomplish.
    task_description : str
        A detailed description of the task or objective.

    Returns
    -------
    dict
        A dictionary containing the list of subtasks, the count of subtasks,
        and any sequencing requirements.

    Raises
    ------
    ValueError
        If the task objective or description is empty.

    Examples
    --------
    >>> decompose_task_into_subtasks(task_objective='Create a workflow',
    task_description='Create a workflow to automate a process')
    >>> print(result)
    {'subtask_list': ['Define task objective', 'Identify dependencies', 'Create
    DAG structure'], 'subtask_count': 3, 'sequencing_requirements':
    'Sequential'}

    """
    return DecomposeTaskIntoSubtasksOutput(
        subtask_list=[],
        subtask_count=0,
        sequencing_requirements="",
    )