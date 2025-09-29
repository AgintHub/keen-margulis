from ._reflectonprayer.validate_prayer_inputs import validate_prayer_inputs
from ._reflectonprayer.analyze_prayer_content import analyze_prayer_content
from ._reflectonprayer.assess_connection_impact import assess_connection_impact
from ._reflectonprayer.extract_insights import extract_insights
from ._reflectonprayer.determine_emotional_response import determine_emotional_response

from pydantic import BaseModel, Field
from typing import List


class InvokeprayerOutput(BaseModel):
    """Pydantic model for invokeprayer node outputs."""
    prayer_invocation: str = (
        Field(..., description="The actual invocation or words used in the prayer.")
    )
    connection_status: str = (
        Field(..., description="The status or feeling of connection during the prayer.")
    )


class ReflectonprayerOutput(BaseModel):
    """Pydantic model for reflectonprayer node outputs."""
    insights_gained: List[str] = (
        Field(..., description="List of insights or understandings gained from the prayer.")
    )
    emotional_response: str = (
        Field(..., description="The emotional response or feeling after the prayer.")
    )


def reflectonprayer(invokeprayer_input: InvokeprayerOutput, **kwargs) -> ReflectonprayerOutput:
    """
    Reflects on the prayer experience to identify insights gained and emotional
    responses.

    Parameters
    ----------
    prayer_invocation : str
        The actual invocation or words used in the prayer, received from the
        'invokeprayer' node.
    connection_status : str
        The status or feeling of connection during the prayer, received from
        the 'invokeprayer' node.

    Returns
    -------
    Tuple[List[str], str]
        A tuple containing a list of insights gained and an emotional
        response after the prayer.

    Raises
    ------
    ValueError
        If the 'prayer_invocation' or 'connection_status' is not provided or
        is empty.

    Examples
    --------
    >>> reflectonprayer(prayer_invocation='I pray for peace and love.',
    connection_status='connected')
    >>> # Expected output: (['Understanding the power of prayer', 'Feeling inner
    peace'], 'grateful')
    (['Understanding the power of prayer', 'Feeling inner peace'], 'grateful')

    >>> reflectonprayer(prayer_invocation='I seek guidance.',
    connection_status='somewhat connected')
    >>> # Expected output: (['Seeking guidance is a form of prayer', 'Feeling
    hopeful'], 'hopeful')
    (['Seeking guidance is a form of prayer', 'Feeling hopeful'], 'hopeful')

    """
    validate_prayer_inputs(prayer_invocation=invokeprayer_input.prayer_invocation, connection_status=invokeprayer_input.connection_status)
    
    analyzed_prayer: dict = analyze_prayer_content(prayer_invocation=invokeprayer_input.prayer_invocation)
    connection_impact: dict = assess_connection_impact(connection_status=invokeprayer_input.connection_status)
    
    insights: List[str] = extract_insights(prayer_analysis=analyzed_prayer, connection_impact=connection_impact)
    emotional_state: str = determine_emotional_response(prayer_analysis=analyzed_prayer, connection_status=invokeprayer_input.connection_status)
    
    return ReflectonprayerOutput(
        insights_gained=insights,
        emotional_response=emotional_state
    )