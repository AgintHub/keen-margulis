from ._finalizeworkflow.generate_workflow_id import generate_workflow_id
from ._finalizeworkflow.create_workflow_url import create_workflow_url
from ._finalizeworkflow.confirm_workflow_creation import confirm_workflow_creation
from ._finalizeworkflow.determine_final_status import determine_final_status

from pydantic import BaseModel, Field


class ValidateworkflowOutput(BaseModel):
    """Pydantic model for validateworkflow node outputs."""
    validation_result: bool = (
        Field(..., description="Result of the workflow validation")
    )
    validation_message: str = (
        Field(..., description="Message indicating the outcome of the validation")
    )


class FinalizeworkflowOutput(BaseModel):
    """Pydantic model for finalizeworkflow node outputs."""
    workflow_status: str = Field(..., description="Status of the workflow")
    workflow_url: str = (
        Field(..., description="URL or identifier for accessing the workflow")
    )


def finalizeworkflow(validateworkflow_input: ValidateworkflowOutput, **kwargs) -> FinalizeworkflowOutput:
    """
    Finalize the workflow creation process based on the validation result.

    Parameters
    ----------
    validation_result : bool
        Result of the workflow validation from the validateworkflow node.
    validation_message : str
        Message indicating the outcome of the validation from the
        validateworkflow node.

    Returns
    -------
    Tuple[str, str]
        A tuple containing the status of the workflow and the URL or
        identifier for accessing the workflow.

    Raises
    ------
    ValueError
        If the validation result is False, indicating the workflow is not
        valid.

    Examples
    --------
    >>> validation_result = True
    >>> validation_message = 'Workflow is valid and functional.'
    >>> workflow_status, workflow_url = finalizeworkflow(validation_result,
    validation_message)
    ('success', 'https://example.com/workflow/123')

    >>> validation_result = False
    >>> validation_message = 'Workflow contains errors.'
    >>> try:
    ...     workflow_status, workflow_url = finalizeworkflow(validation_result,
    validation_message)
    >>> except ValueError as e:
    ...     print(e)
    'Workflow is not valid.'

    """
    if not validateworkflow_input.validation_result:
        raise ValueError("Workflow is not valid.")
    
    workflow_id: str = generate_workflow_id()
    workflow_url: str = create_workflow_url(workflow_id=workflow_id)
    confirm_workflow_creation(workflow_id=workflow_id, validation_message=validateworkflow_input.validation_message)
    final_status: str = determine_final_status(validation_result=validateworkflow_input.validation_result)
    
    return FinalizeworkflowOutput(
        workflow_status=final_status,
        workflow_url=workflow_url
    )