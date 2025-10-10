from pydantic import BaseModel, Field
from typing import List


class DefineWorkflowObjectiveOutput(BaseModel):
    """Pydantic model for define_workflow_objective node outputs."""
    workflow_objective: str = (
        Field(..., description="The primary goal of the workflow expressed as a concise statement.")
    )


class DecomposeObjectiveIntoTasksOutput(BaseModel):
    """Pydantic model for decompose_objective_into_tasks node outputs."""
    tasks: List[str] = (
        Field(..., description="List of task descriptions that represent the decomposed workflow objective")
    )
    task_count: int = (
        Field(..., description="Number of tasks identified in the decomposition")
    )


def decompose_objective_into_tasks(define_workflow_objective_input: DefineWorkflowObjectiveOutput, **kwargs) -> DecomposeObjectiveIntoTasksOutput:
    """
    Breaks down a workflow objective into discrete tasks.

    Parameters
    ----------
    workflow_objective : str
        A concise statement describing the primary goal of the workflow.

    Returns
    -------
    Tuple[List[str], int]
        A tuple containing (1) a list of task descriptions and (2) the count
        of tasks.

    Raises
    ------
    ValueError
        Raised when `workflow_objective` is empty or consists only of
        whitespace.

    Examples
    --------
    >>> tasks, count = decompose_objective_into_tasks('Build a machine learning
    pipeline for predicting house prices')
    (['Collect and clean data', 'Split dataset', 'Select model', 'Train model',
    'Evaluate model', 'Deploy model'], 6)

    >>> tasks, count = decompose_objective_into_tasks('Write a report')
    (['Plan report structure', 'Collect data', 'Write draft', 'Revise',
    'Finalize'], 5)

    """
    return DecomposeObjectiveIntoTasksOutput(
        tasks=[],
        task_count=0,
    )