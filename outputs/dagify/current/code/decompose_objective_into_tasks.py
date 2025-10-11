import logging
from pydantic import BaseModel, Field


logger = logging.getLogger(__name__)

class DefineWorkflowObjectiveOutput(BaseModel):
    objective: str = (
        Field(..., description="Primary goal statement of the workflow")
    )

def define_workflow_objective(general_input: str, **kwargs) -> DefineWorkflowObjectiveOutput:
    """
    Return a validated objective string.

    Parameters
    ----------
    general_input : str
        Human‑readable description of the desired workflow.

    Returns
    -------
    DefineWorkflowObjectiveOutput
        A pydantic model containing the validated objective.

    Raises
    ------
    ValueError
        If the input is empty, non‑string, or only whitespace.

    Examples
    --------
    >>> from your_package import define_workflow_objective
    >>> objective_output = define_workflow_objective("Automate the ingestion,
    transformation, and reporting of sales data.")
    >>> print(objective_output.objective)
    "Automate the ingestion, transformation, and reporting of sales data."

    """
    if not isinstance(general_input, str) or not general_input.strip():
        logger.error("Input objective is empty or not a string")
        raise ValueError("Input objective must be a non-empty string")
    objective = general_input.strip()
    return DefineWorkflowObjectiveOutput(objective=objective)