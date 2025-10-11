from ._decompose_objective_into_tasks.validate_input_type_and_content import validate_input_type_and_content
from ._decompose_objective_into_tasks.sanitize_and_normalize_text import sanitize_and_normalize_text
from ._decompose_objective_into_tasks.enhance_objective_clarity import enhance_objective_clarity
from ._decompose_objective_into_tasks.apply_workflow_formatting_standards import apply_workflow_formatting_standards

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
    validated_input: str = validate_input_type_and_content(input_value=general_input)
    cleaned_objective: str = sanitize_and_normalize_text(text=validated_input)
    enhanced_objective: str = enhance_objective_clarity(objective=cleaned_objective)
    final_objective: str = apply_workflow_formatting_standards(objective=enhanced_objective)
    return DefineWorkflowObjectiveOutput(objective=final_objective)