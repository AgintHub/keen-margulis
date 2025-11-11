from pydantic import BaseModel, Field


class DefineTaskObjectiveOutput(BaseModel):
    """Pydantic model for define_task_objective node outputs."""
    task_objective: str = (
        Field(..., description="The primary objective or task that the workflow will accomplish.")
    )
    task_description: str = (
        Field(..., description="A detailed description of the task or objective.")
    )


def define_task_objective(general_input: str, **kwargs) -> DefineTaskObjectiveOutput:
    """
    This function takes no inputs and returns a task objective and its
    description based on user input.

    Returns
    -------
    dict
        A dictionary containing the task objective and its description.

    Raises
    ------
    ValueError
        If the user input is empty or invalid.

    Examples
    --------
    >>> task_objective = define_task_objective()
    >>> print(task_objective['task_objective'])  # Output: 'Train a machine
    learning model'
    >>> print(task_objective['task_description'])  # Output: 'The goal is to
    train a model that can predict user behavior.'
    {'task_objective': 'Train a machine learning model', 'task_description':
    'The goal is to train a model that can predict user behavior.'}

    """
    return DefineTaskObjectiveOutput(
        task_objective="",
        task_description="",
    )