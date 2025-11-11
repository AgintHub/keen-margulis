from ._construct_dag.validate_inputs import validate_inputs
from ._construct_dag.parse_dependency_map import parse_dependency_map
from ._construct_dag.extract_task_list import extract_task_list
from ._construct_dag.validate_dag_consistency import validate_dag_consistency
from ._construct_dag.build_dag_edges import build_dag_edges
from ._construct_dag.format_digraph import format_digraph

from pydantic import BaseModel, Field
from typing import List


class IdentifyDependenciesOutput(BaseModel):
    """Pydantic model for identify_dependencies node outputs."""
    dependency_map: List[str] = (
        Field(..., description = (
            "List representing the dependency map between tasks")
        )
    )


class DefineNodeOutputsOutput(BaseModel):
    """Pydantic model for define_node_outputs node outputs."""
    node_outputs: List[str] = (
        Field(..., description = (
            "List containing output structures for each node")
        )
    )


class ConstructDagOutput(BaseModel):
    """Pydantic model for construct_dag node outputs."""
    dag_structure: str = (
        Field(..., description="The constructed workflow DAG structure")
    )


def construct_dag(identify_dependencies_input: IdentifyDependenciesOutput, define_node_outputs_input: DefineNodeOutputsOutput, **kwargs) -> ConstructDagOutput:
    """
    Constructs the workflow DAG using the task list, dependency map, and node
    outputs.

    Parameters
    ----------
    task_list : List[str]
        List of decomposed tasks or steps derived from the objective.
    dependency_map : List[str]
        List representing the dependency map between tasks.
    node_outputs : List[str]
        List containing output structures for each node.

    Returns
    -------
    str
        The constructed workflow DAG structure represented as a string.

    Raises
    ------
    ValueError
        If the task list, dependency map, or node outputs are inconsistent
        or malformed.

    Examples
    --------
    >>> task_list = ['task1', 'task2', 'task3']
    >>> dependency_map = [('task1', 'task2'), ('task2', 'task3')]
    >>> node_outputs = [{'task1': 'output1'}, {'task2': 'output2'}, {'task3':
    'output3'}]
    >>> dag_structure = construct_dag(task_list, dependency_map, node_outputs)
    digraph G { task1 -> task2; task2 -> task3; }

    >>> task_list = ['A', 'B', 'C']
    >>> dependency_map = [('A', 'B'), ('B', 'C')]
    >>> node_outputs = [{'A': 'resultA'}, {'B': 'resultB'}, {'C': 'resultC'}]
    >>> dag_structure = construct_dag(task_list, dependency_map, node_outputs)
    digraph G { A -> B; B -> C; }

    """
    dependency_map = identify_dependencies_input.dependency_map
    node_outputs = define_node_outputs_input.node_outputs
    
    validate_inputs(dependency_map=dependency_map, node_outputs=node_outputs)
    
    parsed_dependencies: List[tuple] = parse_dependency_map(dependency_map=dependency_map)
    task_list: List[str] = extract_task_list(dependency_map=dependency_map, node_outputs=node_outputs)
    
    validate_dag_consistency(task_list=task_list, dependencies=parsed_dependencies, node_outputs=node_outputs)
    
    dag_edges: List[str] = build_dag_edges(dependencies=parsed_dependencies)
    dag_structure: str = format_digraph(edges=dag_edges)
    
    return ConstructDagOutput(dag_structure=dag_structure)