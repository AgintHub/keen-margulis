from ._prepareforprayer.clear_mind import clear_mind
from ._prepareforprayer.focus_on_intention import focus_on_intention
from ._prepareforprayer.validate_intention import validate_intention
from ._prepareforprayer.assess_readiness import assess_readiness
from ._prepareforprayer.verify_readiness_boolean import verify_readiness_boolean

from pydantic import BaseModel, Field


class PrepareforprayerOutput(BaseModel):
    """Pydantic model for prepareforprayer node outputs."""
    prayer_intention: str = (
        Field(..., description="The intention or focus of the prayer.")
    )
    is_ready: bool = (
        Field(..., description="Whether the person is ready to pray.")
    )


def prepareforprayer(general_input: str, **kwargs) -> PrepareforprayerOutput:
    """
    Prepare for prayer by clearing mind and focusing on intention, returning the
    prayer intention and readiness status.

    Returns
    -------
    Tuple[str, bool]
        A tuple containing the prayer intention as a string and a boolean
        indicating whether the person is ready to pray.

    Raises
    ------
    ValueError
        If the prayer intention is empty or not a string.
    TypeError
        If the is_ready status is not a boolean.

    Examples
    --------
    >>> prepare_for_prayer()
    ('peace and harmony', True)

    >>> prepare_for_prayer()
    ('guidance', False)

    """
    mind_state: str = clear_mind(input_context=general_input)
    intention: str = focus_on_intention(mind_state=mind_state, context=general_input)
    validated_intention: str = validate_intention(intention=intention)
    readiness_status: bool = assess_readiness(intention=validated_intention, mind_state=mind_state)
    final_status: bool = verify_readiness_boolean(status=readiness_status)
    return PrepareforprayerOutput(
        prayer_intention=validated_intention,
        is_ready=final_status
    )