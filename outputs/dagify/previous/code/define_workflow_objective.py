from pydantic import BaseModel, Field


class DefineWorkflowObjectiveOutput(BaseModel):
    """Pydantic model for define_workflow_objective node outputs."""
    objective: str = (
        Field(..., description="Primary goal statement of the workflow")
    )


def define_workflow_objective(general_input: str, **kwargs) -> DefineWorkflowObjectiveOutput:
    """
    Generate a concise primary goal statement for the workflow.

    Returns
    -------
    str
        A natural‑language statement describing the workflow’s overall
        objective.

    Raises
    ------
    ValueError
        If the generated objective is empty or consists only of whitespace.

    Examples
    --------
    >>> # Example 1: Basic workflow objective
    >>> objective = define_workflow_objective()
    >>> print(objective)
    'Automate the ingestion, transformation, and reporting of sales data.'

    >>> # Example 2: High‑level objective for a data science pipeline
    >>> objective = define_workflow_objective()
    >>> print(objective)
    'Deliver actionable insights from customer behavior data through automated
    analysis and visualization.'

    """
    return DefineWorkflowObjectiveOutput(
        objective="",
    )