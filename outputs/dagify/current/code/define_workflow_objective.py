from ._define_workflow_objective.validate_input_string import validate_input_string
from ._define_workflow_objective.clean_and_normalize_input import clean_and_normalize_input
from ._define_workflow_objective.generate_objective_statement import generate_objective_statement
from ._define_workflow_objective.create_output_model import create_output_model

import logging
from typing import Any
from pydantic import BaseModel, Field


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
    validated_input: str = validate_input_string(input_value=general_input)
    cleaned_input: str = clean_and_normalize_input(raw_input=validated_input)
    objective_statement: str = generate_objective_statement(cleaned_description=cleaned_input)
    output_model: DefineWorkflowObjectiveOutput = create_output_model(objective=objective_statement)
    return output_model