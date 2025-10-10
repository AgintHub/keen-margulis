from ._determine_sport_type.validate_sport_input import validate_sport_input
from ._determine_sport_type.analyze_sport_characteristics import analyze_sport_characteristics
from ._determine_sport_type.classify_sport_type import classify_sport_type
from ._determine_sport_type.generate_classification_rationale import generate_classification_rationale

from pydantic import BaseModel, Field


class IdentifySportOutput(BaseModel):
    """Pydantic model for identify_sport node outputs."""
    selected_sport: str = (
        Field(..., description = (
            "The name of the sport identified or specified by the user")
        )
    )


class DetermineSportTypeOutput(BaseModel):
    """Pydantic model for determine_sport_type node outputs."""
    sport_type: str = (
        Field(..., description="Whether the sport is team-based or individual")
    )
    rationale: str = (
        Field(..., description = (
            "One-sentence explanation for the classification")
        )
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
    selected_sport: str = identify_sport_input.selected_sport
    
    validated_sport: str = validate_sport_input(sport_name=selected_sport)
    sport_characteristics: dict = analyze_sport_characteristics(sport=validated_sport)
    classification: str = classify_sport_type(characteristics=sport_characteristics)
    explanation: str = generate_classification_rationale(sport=validated_sport, sport_type=classification, characteristics=sport_characteristics)
    
    return DetermineSportTypeOutput(
        sport_type=classification,
        rationale=explanation
    )