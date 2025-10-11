import logging
from typing import Any
from pydantic import BaseModel, Field, ValidationError


logger = logging.getLogger(__name__)

class DefineWorkflowObjectiveOutput(BaseModel):
    objective: str = (
        Field(..., description="Primary goal statement of the workflow")
    )

def define_workflow_objective(general_input: str, **kwargs: Any) -> DefineWorkflowObjectiveOutput:
    """
    Defines the workflow’s primary objective statement.

    Parameters
    ----------
    general_input : str
        High‑level description or context used to generate the objective.

    Returns
    -------
    DefineWorkflowObjectiveOutput
        Object containing the primary goal sentence.

    Raises
    ------
    ValueError
        If the input is empty or consists only of whitespace.

    Examples
    --------
    >>> output = define_workflow_objective("automate data ingestion and
    reporting")
    >>> print(output.objective)
    "The primary objective of this workflow is to automate data ingestion and
    reporting."

    """
    if not isinstance(general_input, str):
        logger.error("general_input must be a string")
        raise ValueError("general_input must be a string")
    cleaned = general_input.strip()
    if not cleaned:
        logger.error("general_input is empty or whitespace only")
        raise ValueError("general_input must be a non-empty string")
    objective = f"The primary objective of this workflow is to {cleaned}."
    try:
        return DefineWorkflowObjectiveOutput(objective=objective)
    except ValidationError as ve:
        logger.error("Validation error when creating output: %s", ve)
        raise