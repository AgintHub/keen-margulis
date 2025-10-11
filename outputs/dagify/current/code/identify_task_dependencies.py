import logging
import re
from typing import List

from pydantic import BaseModel  # noqa: E0611


class DecomposeObjectiveIntoTasksOutput(BaseModel):
    task_names: List[str]
    task_descriptions: List[str]
    num_tasks: int

class IdentifyTaskDependenciesOutput(BaseModel):
    task_names: List[str]
    dependency_pairs: List[str]
    dependency_count: int

def identify_task_dependencies(decompose_objective_into_tasks_input: DecomposeObjectiveIntoTasksOutput, **kwargs) -> IdentifyTaskDependenciesOutput:
    """
    Detects precedence relationships among decomposed tasks using text‑matching
    heuristics.

    Parameters
    ----------
    decompose_objective_into_tasks_input : DecomposeObjectiveIntoTasksOutput
        Pydantic model containing task names and their descriptions.

    Returns
    -------
    IdentifyTaskDependenciesOutput
        Model with the original task list, a list of dependency pairs, and
        their count.

    Raises
    ------
    ValueError
        If input lists are empty or mis‑aligned.

    Examples
    --------
    >>> from typing import List
    >>> class DecomposeObjectiveIntoTasksOutput(BaseModel):
    ...     task_names: List[str]
    ...     task_descriptions: List[str]
    ...     num_tasks: int
    >>> class IdentifyTaskDependenciesOutput(BaseModel):
    ...     task_names: List[str]
    ...     dependency_pairs: List[str]
    ...     dependency_count: int
    >>> input_data = DecomposeObjectiveIntoTasksOutput(**{
    ...     'task_names': ['Collect Data', 'Clean Data', 'Analyze Data'],
    ...     'task_descriptions': ['Gather raw data', 'Remove noise from
    collected data', 'Run statistical models on cleaned data'],
    ...     'num_tasks': 3
    >>> })
    >>> output = identify_task_dependencies(input_data)
    >>> print(output.dependency_pairs)
    ['Collect Data -> Clean Data', 'Clean Data -> Analyze Data']

    """
    logger = logging.getLogger(__name__)
    task_names = decompose_objective_into_tasks_input.task_names
    task_descriptions = decompose_objective_into_tasks_input.task_descriptions
    if not task_names or not task_descriptions:
        logger.error("Task lists cannot be empty")
        raise ValueError("Task lists cannot be empty")
    if len(task_names) != len(task_descriptions):
        logger.error("Task names and descriptions list lengths differ")
        raise ValueError("Task names and descriptions list lengths differ")
    dependencies: List[str] = []
    for i, (name_a, desc_a) in enumerate(zip(task_names, task_descriptions)):
        for j, (name_b, desc_b) in enumerate(zip(task_names, task_descriptions)):
            if i == j:
                continue
            if re.search(rf"\\b{re.escape(name_b)}\\b", desc_a, re.IGNORECASE):
                pair = f"{name_a} -> {name_b}"
                if pair not in dependencies:
                    dependencies.append(pair)
    return IdentifyTaskDependenciesOutput(
        task_names=task_names,
        dependency_pairs=dependencies,
        dependency_count=len(dependencies)
    )