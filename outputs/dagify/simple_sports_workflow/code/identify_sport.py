from ._identify_sport.prompt_user_for_sport import prompt_user_for_sport
from ._identify_sport.clean_and_validate_input import clean_and_validate_input
from ._identify_sport.normalize_sport_name import normalize_sport_name

from pydantic import BaseModel, Field


class IdentifySportOutput(BaseModel):
    """Pydantic model for identify_sport node outputs."""
    selected_sport: str = (
        Field(..., description = (
            "The name of the sport identified or specified by the user")
        )
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
    user_input: str = prompt_user_for_sport(message="Please specify a sport of interest: ")
    cleaned_input: str = clean_and_validate_input(raw_input=user_input)
    if not cleaned_input or cleaned_input.isspace():
        raise ValueError("User provided empty or whitespace-only input")
    normalized_sport: str = normalize_sport_name(sport_name=cleaned_input)
    return IdentifySportOutput(selected_sport=normalized_sport)