from pydantic import BaseModel, Field


class DefineHistoricalContextOutput(BaseModel):
    """Pydantic model for define_historical_context node outputs."""
    historical_event: str = (
        Field(..., description="The name or title of the historical event or period being studied")
    )
    time_frame: str = (
        Field(..., description="The approximate time range (e.g., years or dates) of the event or period")
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
    return DefineHistoricalContextOutput(
        historical_event="",
        time_frame="",
    )