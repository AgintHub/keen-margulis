from ._create_dag_structure.parse_dependency_string import parse_dependency_string
from ._create_dag_structure.extract_unique_nodes import extract_unique_nodes
from ._create_dag_structure.format_edges_for_output import format_edges_for_output
from ._create_dag_structure.detect_cycles_in_graph import detect_cycles_in_graph
from ._create_dag_structure.find_root_nodes import find_root_nodes
from ._create_dag_structure.validate_dag_structure import validate_dag_structure

from pydantic import BaseModel, Field
from typing import List


class IdentifyDependenciesBetweenSubtasksOutput(BaseModel):
    """Pydantic model for identify_dependencies_between_subtasks node outputs."""
    dependencies_exist: bool = (
        Field(..., description="Whether dependencies exist between subtasks")
    )
    dependency_list: str = (
        Field(..., description = (
            "List of dependencies between subtasks, where each dependency is represented as 'subtask_id_1 -> subtask_id_2'")
        )
    )


class CreateDagStructureOutput(BaseModel):
    """Pydantic model for create_dag_structure node outputs."""
    dag_nodes: List[str] = (
        Field(..., description="List of node names in the DAG")
    )
    dag_edges: List[str] = (
        Field(..., description = (
            "List of edges in the DAG, represented as 'node1->node2'")
        )
    )
    root_nodes: List[str] = (
        Field(..., description="List of root node names in the DAG")
    )
    is_valid_dag: bool = (
        Field(..., description="Whether the constructed DAG is valid")
    )


def create_dag_structure(identify_dependencies_between_subtasks_input: IdentifyDependenciesBetweenSubtasksOutput, **kwargs) -> CreateDagStructureOutput:
    """
    Creates a DAG structure based on subtasks and their dependencies.

    Parameters
    ----------
    subtasks : List[str]
        List of subtask names.
    dependencies : List[str]
        List of dependencies between subtasks, where each dependency is
        represented as 'subtask_id_1 -> subtask_id_2'.

    Returns
    -------
    {dag_nodes: List[str], dag_edges: List[str], root_nodes: List[str], is_valid_dag: bool}
        A dictionary containing the DAG nodes, edges, root nodes, and a flag
        indicating whether the DAG is valid.

    Raises
    ------
    ValueError
        If the dependencies form a cycle, making it impossible to create a
        valid DAG.

    Examples
    --------
    >>> subtasks = ['A', 'B', 'C']
    >>> dependencies = ['A -> B', 'B -> C']
    >>> create_dag_structure(subtasks, dependencies)
    {'dag_nodes': ['A', 'B', 'C'], 'dag_edges': ['A->B', 'B->C'], 'root_nodes':
    ['A'], 'is_valid_dag': True}

    """
    parsed_dependencies: List[tuple] = parse_dependency_string(dependency_string=identify_dependencies_between_subtasks_input.dependency_list)
    
    all_nodes: List[str] = extract_unique_nodes(dependencies=parsed_dependencies)
    
    formatted_edges: List[str] = format_edges_for_output(dependencies=parsed_dependencies)
    
    has_cycle: bool = detect_cycles_in_graph(nodes=all_nodes, dependencies=parsed_dependencies)
    
    if has_cycle:
        raise ValueError("Dependencies form a cycle, making it impossible to create a valid DAG")
    
    root_node_list: List[str] = find_root_nodes(nodes=all_nodes, dependencies=parsed_dependencies)
    
    is_valid: bool = validate_dag_structure(nodes=all_nodes, edges=formatted_edges, roots=root_node_list)
    
    return CreateDagStructureOutput(
        dag_nodes=all_nodes,
        dag_edges=formatted_edges,
        root_nodes=root_node_list,
        is_valid_dag=is_valid
    )