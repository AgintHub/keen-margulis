from ._analyze_social_influences.validate_social_factors_input import validate_social_factors_input
from ._analyze_social_influences.calculate_impact_scores import calculate_impact_scores
from ._analyze_social_influences.count_social_factors import count_social_factors
from ._analyze_social_influences.format_factors_as_string import format_factors_as_string
from ._analyze_social_influences.calculate_average_impact import calculate_average_impact
from ._analyze_social_influences.generate_interaction_summary import generate_interaction_summary

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


class AnalyzeSocialInfluencesOutput(BaseModel):
    """Pydantic model for analyze_social_influences node outputs."""
    number_of_factors: int = (
        Field(..., description = (
            "Total number of distinct social factors identified.")
        )
    )
    social_factors: str = (
        Field(..., description = (
            "List of names or brief descriptions of each social factor that influenced the event.")
        )
    )
    impact_scores: float = (
        Field(..., description = (
            "Impact rating for each social factor on a scale from 0.0 (minimal) to 1.0 (major). Order corresponds to the social_factors list.")
        )
    )
    summary: str = (
        Field(..., description = (
            "A concise narrative summarizing how the identified social factors interacted to shape the historical event.")
        )
    )


def analyze_social_influences(identify_key_factors_input: IdentifyKeyFactorsOutput, **kwargs) -> AnalyzeSocialInfluencesOutput:
    """
    Analyze the social influences on a historical event, assigning impact scores
    and summarizing their combined effect.

    Parameters
    ----------
    input_social_factors : List[str]
        List of primary social factors returned by the parent node
        `identify_key_factors`.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the number of factors, the list of social
        factors, their impact scores, and a summary narrative.

    Raises
    ------
    ValueError
        Raised when `input_social_factors` is empty or None.

    Examples
    --------
    >>> result = analyze_social_influences(["Women’s suffrage", "Urbanization"])
    {"number_of_factors": 2, "social_factors": ["Women’s suffrage",
    "Urbanization"], "impact_scores": [0.8, 0.6], "summary": "Women’s suffrage
    and urbanization combined accelerated democratic reforms."}

    >>> result = analyze_social_influences(["Industrial labor strikes"])
    {"number_of_factors": 1, "social_factors": ["Industrial labor strikes"],
    "impact_scores": [0.7], "summary": "Industrial labor strikes pressured
    governments to enact labor protections."}

    """
    input_social_factors: List[str] = identify_key_factors_input.social_factors
    
    validated_factors: List[str] = validate_social_factors_input(factors=input_social_factors)
    
    impact_scores_list: List[float] = calculate_impact_scores(social_factors=validated_factors)
    
    factor_count: int = count_social_factors(factors=validated_factors)
    
    factors_string: str = format_factors_as_string(factors=validated_factors)
    
    average_impact: float = calculate_average_impact(scores=impact_scores_list)
    
    narrative_summary: str = generate_interaction_summary(factors=validated_factors, scores=impact_scores_list)
    
    return AnalyzeSocialInfluencesOutput(
        number_of_factors=factor_count,
        social_factors=factors_string,
        impact_scores=average_impact,
        summary=narrative_summary
    )