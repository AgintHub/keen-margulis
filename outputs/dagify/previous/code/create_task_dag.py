from ._create_task_dag.parse_dependency_strings import parse_dependency_strings
from ._create_task_dag.validate_task_references import validate_task_references
from ._create_task_dag.extract_edge_sources import extract_edge_sources
from ._create_task_dag.extract_edge_destinations import extract_edge_destinations
from ._create_task_dag.check_dag_acyclicity import check_dag_acyclicity
from ._create_task_dag.format_task_list import format_task_list
from ._create_task_dag.format_edge_list import format_edge_list

from pydantic import BaseModel, Field
from typing import List


class IdentifyTaskDependenciesOutput(BaseModel):
    """Pydantic model for identify_task_dependencies node outputs."""
    tasks: List[str] = Field(..., description="List of identified task names.")
    dependencies: List[str] = (
        Field(..., description = (
            "List of dependency relationships in the format 'TaskA depends on TaskB'.")
        )
    )
    dependency_exists: bool = (
        Field(..., description = (
            "Indicates whether any dependencies were identified.")
        )
    )


class CreateTaskDagOutput(BaseModel):
    """Pydantic model for create_task_dag node outputs."""
    task_ids: str = (
        Field(..., description = (
            "List of unique task identifiers used in the DAG")
        )
    )
    edge_sources: str = (
        Field(..., description = (
            "List of source task identifiers for each directed edge in the DAG")
        )
    )
    edge_destinations: str = (
        Field(..., description = (
            "List of destination task identifiers for each directed edge in the DAG")
        )
    )
    is_valid: bool = (
        Field(..., description = (
            "Indicates whether the constructed DAG is acyclic and complete")
        )
    )


def create_task_dag(identify_task_dependencies_input: IdentifyTaskDependenciesOutput, **kwargs) -> CreateTaskDagOutput:
    """
    Constructs a DAG from given tasks and dependency relations.

    Parameters
    ----------
    tasks : List[str]
        A list of task identifiers that will become the DAG nodes.
    dependencies : List[str]
        Each string represents a dependency in the format 'TaskA depends on
        TaskB'.

    Returns
    -------
    dict
        A dictionary with four keys: task_ids (List[str]), edge_sources
        (List[str]), edge_destinations (List[str]), and is_valid (bool).

    Raises
    ------
    ValueError
        Raised when a dependency refers to a task not present in the `tasks`
        list.
    ValueError
        Raised when a dependency string does not match the expected 'TaskA
        depends on TaskB' pattern.

    Examples
    --------
    >>> tasks = ['A', 'B', 'C']
    >>> dependencies = ['B depends on A', 'C depends on B']
    >>> result = create_task_dag(tasks, dependencies)
    >>> print(result)
    {'task_ids': ['A', 'B', 'C'], 'edge_sources': ['A', 'B'],
    'edge_destinations': ['B', 'C'], 'is_valid': True}

    >>> tasks = ['A', 'B']
    >>> dependencies = ['A depends on B', 'B depends on A']
    >>> result = create_task_dag(tasks, dependencies)
    >>> print(result)
    {'task_ids': ['A', 'B'], 'edge_sources': ['B', 'A'], 'edge_destinations':
    ['A', 'B'], 'is_valid': False}

    """
    tasks = identify_task_dependencies_input.tasks
    dependencies = identify_task_dependencies_input.dependencies
    
    parsed_dependencies: List[tuple] = parse_dependency_strings(dependencies=dependencies)
    
    validate_task_references(tasks=tasks, parsed_dependencies=parsed_dependencies)
    
    edge_sources: List[str] = extract_edge_sources(parsed_dependencies=parsed_dependencies)
    edge_destinations: List[str] = extract_edge_destinations(parsed_dependencies=parsed_dependencies)
    
    is_acyclic: bool = check_dag_acyclicity(tasks=tasks, edge_sources=edge_sources, edge_destinations=edge_destinations)
    
    task_ids_str: str = format_task_list(tasks=tasks)
    edge_sources_str: str = format_edge_list(edges=edge_sources)
    edge_destinations_str: str = format_edge_list(edges=edge_destinations)
    
    return CreateTaskDagOutput(
        task_ids=task_ids_str,
        edge_sources=edge_sources_str,
        edge_destinations=edge_destinations_str,
        is_valid=is_acyclic
    )