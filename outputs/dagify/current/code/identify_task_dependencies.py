from ._identify_task_dependencies.normalize_task_names import normalize_task_names
from ._identify_task_dependencies.normalize_task_descriptions import normalize_task_descriptions
from ._identify_task_dependencies.detect_semantic_relationships import detect_semantic_relationships
from ._identify_task_dependencies.detect_keyword_dependencies import detect_keyword_dependencies
from ._identify_task_dependencies.merge_dependency_sources import merge_dependency_sources
from ._identify_task_dependencies.filter_duplicate_dependencies import filter_duplicate_dependencies
from ._identify_task_dependencies.format_dependency_pairs import format_dependency_pairs

import logging
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
    
    normalized_tasks: List[str] = normalize_task_names(task_names=task_names)
    normalized_descriptions: List[str] = normalize_task_descriptions(descriptions=task_descriptions)
    
    semantic_matches: List[tuple] = detect_semantic_relationships(task_names=normalized_tasks, descriptions=normalized_descriptions)
    
    keyword_matches: List[tuple] = detect_keyword_dependencies(task_names=normalized_tasks, descriptions=normalized_descriptions)
    
    merged_dependencies: List[tuple] = merge_dependency_sources(semantic_matches=semantic_matches, keyword_matches=keyword_matches)
    
    filtered_dependencies: List[tuple] = filter_duplicate_dependencies(dependencies=merged_dependencies)
    
    dependency_pairs: List[str] = format_dependency_pairs(dependencies=filtered_dependencies)
    
    return IdentifyTaskDependenciesOutput(
        task_names=task_names,
        dependency_pairs=dependency_pairs,
        dependency_count=len(dependency_pairs)
    )