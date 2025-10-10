from ._define_historical_context.parse_user_input import parse_user_input
from ._define_historical_context.extract_historical_event import extract_historical_event
from ._define_historical_context.validate_historical_event import validate_historical_event
from ._define_historical_context.determine_time_frame import determine_time_frame
from ._define_historical_context.validate_time_frame import validate_time_frame

from pydantic import BaseModel, Field


class DefineHistoricalContextOutput(BaseModel):
    """Pydantic model for define_historical_context node outputs."""
    historical_event: str = (
        Field(..., description = (
            "The name or title of the historical event or period being studied")
        )
    )
    time_frame: str = (
        Field(..., description = (
            "The approximate time range (e.g., years or dates) of the event or period")
        )
    )


def define_historical_context(general_input: str, **kwargs) -> DefineHistoricalContextOutput:
    """
    Determines the historical event or period to be examined and returns its
    name and time frame.

    Returns
    -------
    Tuple[str, str]
        A tuple containing the historical event name and its approximate
        time frame.

    Raises
    ------
    ValueError
        Raised if the user fails to provide a valid event name or time
        frame.

    Examples
    --------
    >>> event, timeframe = define_historical_context()
    >>> print(event)
    >>> print(timeframe)
    "Renaissance"
    "14th–17th centuries"

    >>> event, timeframe = define_historical_context()
    >>> assert event == "Industrial Revolution"
    >>> assert timeframe == "late 18th–19th centuries"
    "No output, assertions passed."

    """
    parsed_input: str = parse_user_input(input_text=general_input)
    event_name: str = extract_historical_event(parsed_input=parsed_input)
    validated_event: str = validate_historical_event(event_name=event_name)
    time_frame: str = determine_time_frame(historical_event=validated_event)
    validate_time_frame(time_frame=time_frame)
    return DefineHistoricalContextOutput(
        historical_event=validated_event,
        time_frame=time_frame,
    )