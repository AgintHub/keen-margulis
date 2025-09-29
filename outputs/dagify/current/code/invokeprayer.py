from ._invokeprayer.prepare_intention_text import prepare_intention_text
from ._invokeprayer.generate_prayer_invocation import generate_prayer_invocation
from ._invokeprayer.assess_prayer_connection import assess_prayer_connection

from pydantic import BaseModel, Field


class PrepareforprayerOutput(BaseModel):
    """Pydantic model for prepareforprayer node outputs."""
    prayer_intention: str = (
        Field(..., description="The intention or focus of the prayer.")
    )
    is_ready: bool = (
        Field(..., description="Whether the person is ready to pray.")
    )


class InvokeprayerOutput(BaseModel):
    """Pydantic model for invokeprayer node outputs."""
    prayer_invocation: str = (
        Field(..., description="The actual invocation or words used in the prayer.")
    )
    connection_status: str = (
        Field(..., description="The status or feeling of connection during the prayer.")
    )


def invokeprayer(prepareforprayer_input: PrepareforprayerOutput, **kwargs) -> InvokeprayerOutput:
    """
    Invokes a prayer based on the prepared intention and returns the prayer
    invocation and connection status.

    Parameters
    ----------
    prayer_intention : str
        The intention or focus of the prayer, as prepared in the previous
        step.
    is_ready : bool
        Whether the person is ready to pray, indicating their preparedness.

    Returns
    -------
    Tuple[str, str]
        A tuple containing the prayer invocation (str) and the connection
        status (str).

    Raises
    ------
    ValueError
        If the prayer intention is empty or if the person is not ready to
        pray.

    Examples
    --------
    >>> invokeprayer(prayer_intention='Seeking guidance', is_ready=True)
    ('Dear higher power, guide me...', 'Connected')

    >>> invokeprayer(prayer_intention='', is_ready=False)
    ValueError: Prayer intention cannot be empty and person must be ready to
    pray.

    """
    if not prepareforprayer_input.prayer_intention or not prepareforprayer_input.is_ready:
        raise ValueError("Prayer intention cannot be empty and person must be ready to pray.")
    
    prepared_intention: str = prepare_intention_text(intention=prepareforprayer_input.prayer_intention)
    prayer_words: str = generate_prayer_invocation(intention=prepared_intention)
    connection_feeling: str = assess_prayer_connection(invocation=prayer_words, readiness=prepareforprayer_input.is_ready)
    
    return InvokeprayerOutput(
        prayer_invocation=prayer_words,
        connection_status=connection_feeling,
    )