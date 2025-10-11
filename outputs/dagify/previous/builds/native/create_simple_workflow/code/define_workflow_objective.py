from ._define_workflow_objective.parse_user_input import parse_user_input
from ._define_workflow_objective.extract_requirements import extract_requirements
from ._define_workflow_objective.identify_domain import identify_domain
from ._define_workflow_objective.generate_objective_statement import generate_objective_statement
from ._define_workflow_objective.validate_objective_length import validate_objective_length
from ._define_workflow_objective.refine_objective_clarity import refine_objective_clarity

from ._define_workflow_objective.parse_user_input import parse_user_input
from ._define_workflow_objective.extract_requirements import extract_requirements
from ._define_workflow_objective.identify_domain import identify_domain
from ._define_workflow_objective.generate_objective_statement import generate_objective_statement
from ._define_workflow_objective.validate_objective_length import validate_objective_length
from ._define_workflow_objective.refine_objective_clarity import refine_objective_clarity

from pydantic import BaseModel, Field


class DefineWorkflowObjectiveOutput(BaseModel):
    """Pydantic model for define_workflow_objective node outputs."""
    workflow_objective: str = (
        Field(..., description = (
            "The primary goal of the workflow expressed as a concise statement.")
        )
    )


def define_workflow_objective(general_input: str, **kwargs) -> DefineWorkflowObjectiveOutput:
    """
    Generate a concise objective statement for the workflow based on the user’s
    intent.

    Returns
    -------
    str
        Concise objective of the workflow.

    Raises
    ------
    ValueError
        If the generated objective is empty or exceeds an acceptable length.

    Examples
    --------
    >>> objective = define_workflow_objective()
    'Implement an automated data ingestion pipeline for real‑time analytics'

    >>> objective = define_workflow_objective()
    'Develop a user‑friendly mobile application for inventory management'

    """
    parsed_user_intent: dict = parse_user_input(input_text=general_input)
    key_requirements: list = extract_requirements(parsed_intent=parsed_user_intent)
    domain_context: str = identify_domain(requirements=key_requirements)
    raw_objective: str = generate_objective_statement(requirements=key_requirements, domain=domain_context)
    validated_objective: str = validate_objective_length(objective=raw_objective)
    if not validated_objective:
        raise ValueError("Generated objective is empty")
    final_objective: str = refine_objective_clarity(objective=validated_objective)
    return DefineWorkflowObjectiveOutput(
        workflow_objective=final_objective,
    )