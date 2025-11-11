from ._finalize_workflow.retrieve_current_dag_structure import retrieve_current_dag_structure
from ._finalize_workflow.ensure_all_nodes_connected import ensure_all_nodes_connected
from ._finalize_workflow.optimize_dag_performance import optimize_dag_performance
from ._finalize_workflow.generate_final_dag_representation import generate_final_dag_representation

from pydantic import BaseModel, Field


class ValidateDagOutput(BaseModel):
    """Pydantic model for validate_dag node outputs."""
    validation_result: bool = (
        Field(..., description="Whether the DAG is valid and acyclic")
    )


class FinalizeWorkflowOutput(BaseModel):
    """Pydantic model for finalize_workflow node outputs."""
    final_dag: str = Field(..., description="The finalized workflow DAG")


def finalize_workflow(validate_dag_input: ValidateDagOutput, **kwargs) -> FinalizeWorkflowOutput:
    """
    Finalize the workflow DAG based on validation results.

    Parameters
    ----------
    validation_result : bool
        The validation result from the validate_dag node indicating whether
        the DAG is valid and acyclic.

    Returns
    -------
    str
        The finalized workflow DAG as a string representation.

    Raises
    ------
    ValueError
        If the validation result is False, indicating the DAG is not valid
        or contains cycles.

    Examples
    --------
    >>> finalize_workflow(validation_result=True)
    'valid_dag_structure'

    >>> finalize_workflow(validation_result=False)
    ValueError: 'DAG is not valid or contains cycles'

    """
    if not validate_dag_input.validation_result:
        raise ValueError("DAG is not valid or contains cycles")
    
    dag_structure: str = retrieve_current_dag_structure()
    connected_dag: str = ensure_all_nodes_connected(dag_structure=dag_structure)
    optimized_dag: str = optimize_dag_performance(dag=connected_dag)
    final_dag_string: str = generate_final_dag_representation(dag=optimized_dag)
    
    return FinalizeWorkflowOutput(final_dag=final_dag_string)