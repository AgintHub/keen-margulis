from ._define_objective.clean_and_normalize_input import clean_and_normalize_input
from ._define_objective.extract_objective_from_input import extract_objective_from_input
from ._define_objective.validate_objective_format import validate_objective_format

from pydantic import BaseModel, Field


class DefineObjectiveOutput(BaseModel):
    """Pydantic model for define_objective node outputs."""
    objective: str = (
        Field(..., description="The defined objective or task description")
    )


def define_objective(general_input: str, **kwargs) -> DefineObjectiveOutput:
    """
    Defines the objective or task description for the workflow.

    Returns
    -------
    str
        The defined objective or task description.

    Raises
    ------
    ValueError
        If the objective is not provided or is empty.

    Examples
    --------
    >>> define_objective()
    "Create a workflow to process customer orders"

    >>> define_objective()
    "Design a data pipeline for real-time analytics"

    """
    if not general_input or general_input.strip() == "":
        raise ValueError("If the objective is not provided or is empty.")
    
    processed_input: str = clean_and_normalize_input(input_text=general_input)
    objective_definition: str = extract_objective_from_input(processed_input=processed_input)
    validated_objective: str = validate_objective_format(objective=objective_definition)
    
    return DefineObjectiveOutput(objective=validated_objective)