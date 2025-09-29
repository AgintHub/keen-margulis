from ._concludeprayer.validate_inputs import validate_inputs
from ._concludeprayer.generate_gratitude_expression import generate_gratitude_expression
from ._concludeprayer.assess_prayer_closure import assess_prayer_closure

from pydantic import BaseModel, Field
from typing import List


class ReflectonprayerOutput(BaseModel):
    """Pydantic model for reflectonprayer node outputs."""
    insights_gained: List[str] = (
        Field(..., description="List of insights or understandings gained from the prayer.")
    )
    emotional_response: str = (
        Field(..., description="The emotional response or feeling after the prayer.")
    )


class ConcludeprayerOutput(BaseModel):
    """Pydantic model for concludeprayer node outputs."""
    gratitude_expression: str = (
        Field(..., description="Expression of gratitude at the end of the prayer.")
    )
    closure_status: bool = (
        Field(..., description="Whether the prayer was concluded satisfactorily.")
    )


def concludeprayer(reflectonprayer_input: ReflectonprayerOutput, **kwargs) -> ConcludeprayerOutput:
    """
    Concludes the prayer process by formulating a gratitude expression and
    assessing the closure status based on the reflection insights.

    Parameters
    ----------
    insights_gained : List[str]
        List of insights gained from the prayer reflection.
    emotional_response : str
        Emotional response or feeling after the prayer.

    Returns
    -------
    Tuple[str, bool]
        A tuple containing the gratitude expression and the closure status.

    Raises
    ------
    ValueError
        If insights_gained is empty or emotional_response is not a valid
        emotional state.

    Examples
    --------
    >>> insights_gained = ['felt peace', 'grateful']
    >>> emotional_response = 'calm'
    >>> gratitude_expression, closure_status = conclude_prayer(insights_gained,
    emotional_response)
    ('Thank you for the peace and gratitude I felt.', True)

    >>> insights_gained = []
    >>> emotional_response = 'unsettled'
    >>> gratitude_expression, closure_status = conclude_prayer(insights_gained,
    emotional_response)
    ('Unable to conclude prayer satisfactorily.', False)

    """
    validate_inputs(insights=reflectonprayer_input.insights_gained, emotional_response=reflectonprayer_input.emotional_response)
    
    gratitude_text: str = generate_gratitude_expression(insights=reflectonprayer_input.insights_gained, emotional_state=reflectonprayer_input.emotional_response)
    
    closure_satisfied: bool = assess_prayer_closure(insights=reflectonprayer_input.insights_gained, emotional_response=reflectonprayer_input.emotional_response)
    
    return ConcludeprayerOutput(
        gratitude_expression=gratitude_text,
        closure_status=closure_satisfied
    )