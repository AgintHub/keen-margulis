from ._decompose_objective.validate_objective_input import validate_objective_input
from ._decompose_objective.parse_objective_structure import parse_objective_structure
from ._decompose_objective.generate_task_breakdown import generate_task_breakdown
from ._decompose_objective.refine_and_order_tasks import refine_and_order_tasks

from pydantic import BaseModel, Field
from typing import List


class DefineObjectiveOutput(BaseModel):
    """Pydantic model for define_objective node outputs."""
    objective: str = (
        Field(..., description="The defined objective or task description")
    )


class DecomposeObjectiveOutput(BaseModel):
    """Pydantic model for decompose_objective node outputs."""
    task_list: List[str] = (
        Field(..., description="List of decomposed tasks or steps")
    )


def decompose_objective(define_objective_input: DefineObjectiveOutput, **kwargs) -> DecomposeObjectiveOutput:
    """
    Decomposes the given objective into a list of tasks or steps.

    Parameters
    ----------
    objective : str
        The defined objective or task description obtained from the
        'define_objective' node.

    Returns
    -------
    List[str]
        A list of decomposed tasks or steps derived from the objective.

    Raises
    ------
    ValueError
        If the objective is empty or not a string.

    Examples
    --------
    >>> decompose_objective(objective='Create a workflow DAG')
    ['Define objective', 'Decompose objective', 'Identify dependencies',
    'Construct DAG']

    >>> decompose_objective(objective='Develop a machine learning model')
    ['Collect data', 'Preprocess data', 'Train model', 'Evaluate model']

    """
    objective_text: str = define_objective_input.objective
    
    validated_objective: str = validate_objective_input(objective=objective_text)
    
    parsed_components: List[str] = parse_objective_structure(objective=validated_objective)
    
    decomposed_tasks: List[str] = generate_task_breakdown(components=parsed_components, objective=validated_objective)
    
    refined_tasks: List[str] = refine_and_order_tasks(tasks=decomposed_tasks)
    
    return DecomposeObjectiveOutput(task_list=refined_tasks)