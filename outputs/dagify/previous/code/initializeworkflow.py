from ._initializeworkflow.generate_unique_workflow_id import generate_unique_workflow_id
from ._initializeworkflow.generate_workflow_name import generate_workflow_name
from ._initializeworkflow.validate_workflow_parameters import validate_workflow_parameters

from pydantic import BaseModel, Field


class InitializeworkflowOutput(BaseModel):
    """Pydantic model for initializeworkflow node outputs."""
    workflow_id: str = (
        Field(..., description="Unique identifier for the workflow")
    )
    workflow_name: str = Field(..., description="Name of the workflow")


def initializeworkflow(general_input: str, **kwargs) -> InitializeworkflowOutput:
    """
    Initialize the workflow with the required inputs and settings.

    Returns
    -------
    dict[str, str]
        A dictionary containing the workflow_id and workflow_name.

    Raises
    ------
    RuntimeError
        If the workflow initialization fails.

    Examples
    --------
    >>> initialize_workflow()
    {'workflow_id': 'wf_123', 'workflow_name': 'Super Cool Workflow'}

    """
    unique_id: str = generate_unique_workflow_id()
    workflow_name: str = generate_workflow_name(input_data=general_input, kwargs=kwargs)
    validate_workflow_parameters(workflow_id=unique_id, workflow_name=workflow_name)
    return InitializeworkflowOutput(
        workflow_id=unique_id,
        workflow_name=workflow_name,
    )