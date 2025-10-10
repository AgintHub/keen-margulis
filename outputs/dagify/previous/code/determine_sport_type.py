from pydantic import BaseModel, Field


class IdentifySportOutput(BaseModel):
    """Pydantic model for identify_sport node outputs."""
    selected_sport: str = (
        Field(..., description="The name of the sport identified or specified by the user")
    )


class DetermineSportTypeOutput(BaseModel):
    """Pydantic model for determine_sport_type node outputs."""
    sport_type: str = (
        Field(..., description="Whether the sport is team-based or individual")
    )
    rationale: str = (
        Field(..., description="One-sentence explanation for the classification")
    )


def determine_sport_type(identify_sport_input: IdentifySportOutput, **kwargs) -> DetermineSportTypeOutput:
    """
    Determines whether a sport is team-based or individual.

    Parameters
    ----------
    selected_sport : str
        The name of the sport identified by the parent node.

    Returns
    -------
    Dict[str, str]
        A dictionary containing `sport_type` and `rationale` keys.

    Raises
    ------
    ValueError
        If `selected_sport` is empty or not recognized.

    Examples
    --------
    >>> result = determine_sport_type('soccer')
    >>> print(result['sport_type'])
    >>> print(result['rationale'])
    'team-based'
    'Soccer is a team sport because each side fields 11 players who must
    coordinate to score goals.'

    >>> result = determine_sport_type('tennis')
    >>> print(result['sport_type'])
    >>> print(result['rationale'])
    'individual'
    'Tennis is played by one or two players competing against each other, making
    it an individual sport.'

    """
    return DetermineSportTypeOutput(
        sport_type="",
        rationale="",
    )