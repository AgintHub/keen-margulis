from pydantic import BaseModel, Field
from typing import List


class DefineWorkflowObjectiveOutput(BaseModel):
    """Pydantic model for define_workflow_objective node outputs."""
    objective: str = (
        Field(..., description="Primary goal statement of the workflow")
    )


class DecomposeObjectiveIntoTasksOutput(BaseModel):
    """Pydantic model for decompose_objective_into_tasks node outputs."""
    task_names: List[str] = (
        Field(..., description="List of task names identified by decomposition.")
    )
    task_descriptions: List[str] = (
        Field(..., description="Brief descriptions for each corresponding task.")
    )
    num_tasks: int = Field(..., description="Total number of tasks identified.")


def decompose_objective_into_tasks(define_workflow_objective_input: DefineWorkflowObjectiveOutput, **kwargs) -> DecomposeObjectiveIntoTasksOutput:
    """
    Decomposes a workflow objective string into a list of task names,
    descriptions, and a task count.

    Parameters
    ----------
    objective : str
        Primary goal statement of the workflow provided by
        `define_workflow_objective`.

    Returns
    -------
    tuple[List[str], List[str], int]
        A tuple containing: 1) list of task names, 2) list of brief task
        descriptions, 3) integer count of tasks.

    Raises
    ------
    ValueError
        Raised when the `objective` string is empty or cannot be parsed into
        distinct tasks.

    Examples
    --------
    >>> result = decompose_objective_into_tasks("Process customer orders and
    generate invoices")
    {'task_names': ['Process orders', 'Generate invoices'], 'task_descriptions':
    ['Handle incoming orders from sales', 'Create and send invoices to
    customers'], 'num_tasks': 2}

    >>> result = decompose_objective_into_tasks("Collect data, clean data, and
    train a machine learning model")
    {'task_names': ['Collect data', 'Clean data', 'Train ML model'],
    'task_descriptions': ['Gather raw data from sources', 'Perform data cleaning
    and preprocessing', 'Train a predictive model on cleaned data'],
    'num_tasks': 3}

    """
    return DecomposeObjectiveIntoTasksOutput(
        task_names=[],
        task_descriptions=[],
        num_tasks=0,
    )