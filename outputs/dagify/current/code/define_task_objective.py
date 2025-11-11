from ._define_task_objective.validate_user_input import validate_user_input
from ._define_task_objective.extract_task_objective import extract_task_objective
from ._define_task_objective.generate_task_description import generate_task_description

from pydantic import BaseModel, Field


class DefineTaskObjectiveOutput(BaseModel):
    """Pydantic model for define_task_objective node outputs."""
    task_objective: str = (
        Field(..., description = (
            "The primary objective or task that the workflow will accomplish.")
        )
    )
    task_description: str = (
        Field(..., description = (
            "A detailed description of the task or objective.")
        )
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
    validated_input: str = validate_user_input(input_text=general_input)
    parsed_objective: str = extract_task_objective(user_input=validated_input)
    generated_description: str = generate_task_description(objective=parsed_objective, context=validated_input)
    return DefineTaskObjectiveOutput(
        task_objective=parsed_objective,
        task_description=generated_description
    )