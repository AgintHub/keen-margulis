from pydantic import BaseModel, Field


class IdentifySportOutput(BaseModel):
    """Pydantic model for identify_sport node outputs."""
    selected_sport: str = (
        Field(..., description="The name of the sport identified or specified by the user")
    )


def identify_sport(general_input: str, **kwargs) -> IdentifySportOutput:
    """
    Prompts the user to specify a sport of interest and returns the selected
    sport name as a string.

    Returns
    -------
    str
        The selected sport name.

    Raises
    ------
    ValueError
        Raised if the user provides an empty or whitespace-only input.

    Examples
    --------
    >>> sport = identify_sport()
    'soccer'

    >>> sport = identify_sport()
    'basketball'

    """
    return IdentifySportOutput(
        selected_sport="",
    )