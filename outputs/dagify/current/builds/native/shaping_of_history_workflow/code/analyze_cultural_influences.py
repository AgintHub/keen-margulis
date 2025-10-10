from pydantic import BaseModel, Field
from typing import List


class IdentifyKeyFactorsOutput(BaseModel):
    """Pydantic model for identify_key_factors node outputs."""
    social_factors: List[str] = (
        Field(..., description = (
            "List of primary social factors that influenced the event or period.")
        )
    )
    political_factors: List[str] = (
        Field(..., description = (
            "List of primary political factors that influenced the event or period.")
        )
    )
    economic_factors: List[str] = (
        Field(..., description = (
            "List of primary economic factors that influenced the event or period.")
        )
    )
    cultural_factors: List[str] = (
        Field(..., description = (
            "List of primary cultural factors that influenced the event or period.")
        )
    )


class AnalyzeCulturalInfluencesOutput(BaseModel):
    """Pydantic model for analyze_cultural_influences node outputs."""
    cultural_factors: List[str] = (
        Field(..., description="Names of cultural factors identified")
    )
    factor_categories: List[str] = (
        Field(..., description = (
            "Category of each cultural factor (e.g., norm, value, artistic movement, religious belief, linguistic trend)")
        )
    )
    factor_descriptions: List[str] = (
        Field(..., description="Brief description of each cultural factor")
    )
    influence_scores: List[float] = (
        Field(..., description = (
            "Estimated influence score of each factor on the historical event or period (0 to 1)")
        )
    )
    is_significant: List[bool] = (
        Field(..., description = (
            "Whether each factor is considered significant (True = significant, False = not significant)")
        )
    )


def analyze_cultural_influences(identify_key_factors_input: IdentifyKeyFactorsOutput, **kwargs) -> AnalyzeCulturalInfluencesOutput:
    """
    Analyze cultural influences for a historical event and return detailed
    scores and descriptors.

    Parameters
    ----------
    cultural_factors : List[str]
        List of cultural factor names produced by the identify_key_factors
        node.

    Returns
    -------
    dict
        Dictionary containing the keys 'cultural_factors',
        'factor_categories', 'factor_descriptions', 'influence_scores', and
        'is_significant', each mapping to a list of equal length.

    Raises
    ------
    ValueError
        Raised if the input list is empty or contains non-string elements.

    Examples
    --------
    >>> result = analyze_cultural_influences(['Romanticism', 'Buddhism'])
    >>> print(result['cultural_factors'])
    >>> print(result['factor_categories'])
    >>> print(result['influence_scores'])
    >>> print(result['is_significant'])
    ["Romanticism", "Buddhism"]
    ["Artistic movement", "Religious belief"]
    [0.8, 0.6]
    [True, True]

    >>> try:
    ...     analyze_cultural_influences([])
    >>> except ValueError as e:
    ...     print(e)
    "No cultural factors provided. At least one is required."

    """
    return AnalyzeCulturalInfluencesOutput(
        cultural_factors=[],
        factor_categories=[],
        factor_descriptions=[],
        influence_scores=[],
        is_significant=[],
    )