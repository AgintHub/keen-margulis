from ._identify_dependencies.validate_task_list import validate_task_list
from ._identify_dependencies.analyze_task_relationships import analyze_task_relationships
from ._identify_dependencies.format_dependency_map import format_dependency_map

from pydantic import BaseModel, Field
from typing import List


class DecomposeObjectiveOutput(BaseModel):
    """Pydantic model for decompose_objective node outputs."""
    task_list: List[str] = (
        Field(..., description="List of decomposed tasks or steps")
    )


class IdentifyDependenciesOutput(BaseModel):
    """Pydantic model for identify_dependencies node outputs."""
    dependency_map: List[str] = (
        Field(..., description="List representing the dependency map between tasks")
    )


def identify_dependencies(decompose_objective_input: DecomposeObjectiveOutput, **kwargs) -> IdentifyDependenciesOutput:
    """
    Identify dependencies between decomposed tasks.

    Parameters
    ----------
    task_list : List[str]
        List of decomposed tasks or steps from the 'decompose_objective'
        node.

    Returns
    -------
    List[str]
        List representing the dependency map between tasks.

    Raises
    ------
    ValueError
        If the task_list is empty or malformed.

    Examples
    --------
    >>> task_list = ['task1', 'task2', 'task3']
    >>> dependency_map = identify_dependencies(task_list)
    ['task1->task2', 'task2->task3']

    >>> task_list = ['init', 'process', 'finalize']
    >>> dependency_map = identify_dependencies(task_list)
    ['init->process', 'process->finalize']

    """
    task_list = decompose_objective_input.task_list
    
    validated_tasks: List[str] = validate_task_list(task_list=task_list)
    
    task_relationships: List[tuple] = analyze_task_relationships(tasks=validated_tasks)
    
    dependency_pairs: List[str] = format_dependency_map(relationships=task_relationships)
    
    return IdentifyDependenciesOutput(dependency_map=dependency_pairs)