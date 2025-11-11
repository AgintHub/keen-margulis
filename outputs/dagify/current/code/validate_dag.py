from ._validate_dag.parse_dag_structure import parse_dag_structure
from ._validate_dag.validate_dag_format import validate_dag_format
from ._validate_dag.build_graph_from_edges import build_graph_from_edges
from ._validate_dag.check_dag_acyclicity import check_dag_acyclicity
from ._validate_dag.validate_dag_wellformedness import validate_dag_wellformedness

from pydantic import BaseModel, Field


class ConstructDagOutput(BaseModel):
    """Pydantic model for construct_dag node outputs."""
    dag_structure: str = (
        Field(..., description="The constructed workflow DAG structure")
    )


class ValidateDagOutput(BaseModel):
    """Pydantic model for validate_dag node outputs."""
    validation_result: bool = (
        Field(..., description="Whether the DAG is valid and acyclic")
    )


def validate_dag(construct_dag_input: ConstructDagOutput, **kwargs) -> ValidateDagOutput:
    """
    Validate the constructed workflow DAG for correctness and acyclicity.

    Parameters
    ----------
    dag_structure : str
        The constructed workflow DAG structure from the construct_dag node.

    Returns
    -------
    bool
        Whether the DAG is valid and acyclic.

    Raises
    ------
    ValueError
        If the DAG structure is malformed or contains cycles.

    Examples
    --------
    >>> validate_dag('A->B;B->C')
    True

    >>> validate_dag('A->B;B->A')
    False

    """
    dag_structure = construct_dag_input.dag_structure
    
    parsed_edges = parse_dag_structure(dag_structure=dag_structure)
    
    validate_dag_format(parsed_edges=parsed_edges)
    
    graph_representation = build_graph_from_edges(edges=parsed_edges)
    
    is_acyclic: bool = check_dag_acyclicity(graph=graph_representation)
    
    is_well_formed: bool = validate_dag_wellformedness(graph=graph_representation)
    
    is_valid = is_acyclic and is_well_formed
    
    return ValidateDagOutput(validation_result=is_valid)