from ._synthesize_influences.validate_required_keys import validate_required_keys
from ._synthesize_influences.extract_social_insights import extract_social_insights
from ._synthesize_influences.extract_political_insights import extract_political_insights
from ._synthesize_influences.extract_economic_insights import extract_economic_insights
from ._synthesize_influences.extract_cultural_insights import extract_cultural_insights
from ._synthesize_influences.identify_cross_sector_interactions import identify_cross_sector_interactions
from ._synthesize_influences.calculate_relative_importance import calculate_relative_importance
from ._synthesize_influences.generate_unified_narrative import generate_unified_narrative

from pydantic import BaseModel, Field
from typing import List


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


class AnalyzePoliticalInfluencesOutput(BaseModel):
    """Pydantic model for analyze_political_influences node outputs."""
    political_decisions: List[str] = (
        Field(..., description = (
            "Key political decisions that influenced the historical event or period.")
        )
    )
    policies_influenced: List[str] = (
        Field(..., description = (
            "Policies enacted that had an impact on the event or period.")
        )
    )
    leadership_figures: List[str] = (
        Field(..., description = (
            "Principal political leaders or figures involved in shaping the event.")
        )
    )
    summary: str = (
        Field(..., description = (
            "Concise summary of political influence on the event.")
        )
    )


class AnalyzeEconomicInfluencesOutput(BaseModel):
    """Pydantic model for analyze_economic_influences node outputs."""
    economic_factor_name: str = (
        Field(..., description="Name of the economic factor considered.")
    )
    impact_summary: str = (
        Field(..., description = (
            "Brief description of how this factor impacted the event.")
        )
    )
    evidence_sources: str = (
        Field(..., description = (
            "List of primary source references or data points supporting the analysis.")
        )
    )
    impact_strength: float = (
        Field(..., description = (
            "Rating of the factor's impact strength on a scale from 0 to 1.")
        )
    )
    time_period_affected: str = (
        Field(..., description = (
            "Time period during which the factor was most influential.")
        )
    )
    is_consensus: bool = (
        Field(..., description = (
            "Whether there is scholarly consensus on the factor's significance.")
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


class SynthesizeInfluencesOutput(BaseModel):
    """Pydantic model for synthesize_influences node outputs."""
    social_insights: str = (
        Field(..., description = (
            "Key findings distilled from the social influence analysis.")
        )
    )
    economic_insights: str = (
        Field(..., description = (
            "Key findings distilled from the economic influence analysis.")
        )
    )
    political_insights: str = (
        Field(..., description = (
            "Key findings distilled from the political influence analysis.")
        )
    )
    cultural_insights: str = (
        Field(..., description = (
            "Key findings distilled from the cultural influence analysis.")
        )
    )
    synthesis_summary: str = (
        Field(..., description = (
            "Overall synthesis describing how the identified influences interacted.")
        )
    )
    interaction_points: List[str] = (
        Field(..., description = (
            "List of key interaction points where multiple influences converged.")
        )
    )
    importance_scores: List[float] = (
        Field(..., description = (
            "Relative importance (0.0\u20131.0) assigned to each influence category (social, economic, political, cultural).")
        )
    )


def synthesize_influences(analyze_social_influences_input: AnalyzeSocialInfluencesOutput, analyze_political_influences_input: AnalyzePoliticalInfluencesOutput, analyze_economic_influences_input: AnalyzeEconomicInfluencesOutput, analyze_cultural_influences_input: AnalyzeCulturalInfluencesOutput, **kwargs) -> SynthesizeInfluencesOutput:
    """
    Synthesize social, political, economic, and cultural analyses into a
    coherent set of insights.

    Parameters
    ----------
    social_analysis : dict
        Dictionary containing outputs from `analyze_social_influences`.
        Expected keys: `number_of_factors`, `social_factors`,
        `impact_scores`, `summary`.
    political_analysis : dict
        Dictionary containing outputs from `analyze_political_influences`.
        Expected keys: `political_decisions`, `policies_influenced`,
        `leadership_figures`, `summary`.
    economic_analysis : dict
        Dictionary containing outputs from `analyze_economic_influences`.
        Expected keys: `economic_factor_name`, `impact_summary`,
        `evidence_sources`, `impact_strength`, `time_period_affected`,
        `is_consensus`.
    cultural_analysis : dict
        Dictionary containing outputs from `analyze_cultural_influences`.
        Expected keys: `cultural_factors`, `factor_categories`,
        `factor_descriptions`, `influence_scores`, `is_significant`.

    Returns
    -------
    dict
        A dictionary with keys `social_insights`, `economic_insights`,
        `political_insights`, `cultural_insights`, `synthesis_summary`,
        `interaction_points`, and `importance_scores`.

    Raises
    ------
    ValueError
        Raised if any required key is missing from one of the input analysis
        dictionaries.

    Examples
    --------
    >>> social_analysis = {
    ...     "number_of_factors": 3,
    ...     "social_factors": ["Urbanization", "Labor Movements", "Education
    Reform"],
    ...     "impact_scores": [0.8, 0.6, 0.5],
    ...     "summary": "Rapid urban growth spurred labor activism and
    educational reforms that reshaped social norms."
    >>> }
    >>> political_analysis = {
    ...     "political_decisions": ["Industrial Policy Act 1920", "Labor Law
    Reform 1935"],
    ...     "policies_influenced": ["Minimum Wage", "Workplace Safety
    Regulations"],
    ...     "leadership_figures": ["Prime Minister A", "Senator B"],
    ...     "summary": "Government policies institutionalized labor rights and
    industrial oversight."
    >>> }
    >>> economic_analysis = {
    ...     "economic_factor_name": "Post‑War Reconstruction",
    ...     "impact_summary": "Reconstruction spending accelerated industrial
    output and urban migration.",
    ...     "evidence_sources": ["Census 1941", "Trade Reports 1945"],
    ...     "impact_strength": 0.9,
    ...     "time_period_affected": "1945–1955",
    ...     "is_consensus": true
    >>> }
    >>> cultural_analysis = {
    ...     "cultural_factors": ["Modernist Art Movement", "Literary Boom"],
    ...     "factor_categories": ["Art", "Literature"],
    ...     "factor_descriptions": ["Challenged traditional aesthetics",
    "Explored new narrative forms"],
    ...     "influence_scores": [0.4, 0.3],
    ...     "is_significant": [true, true]
    >>> }
    >>> from synthesize_influences import synthesize_influences
    >>> result = synthesize_influences(social_analysis, political_analysis,
    economic_analysis, cultural_analysis)
    >>> print(result["synthesis_summary"])
    "The post‑war reconstruction boom fueled urbanization, creating a labor pool
    that empowered social movements. Government policies codified labor rights,
    while modernist art and literature reflected and reinforced the era’s
    transformative ethos. Together, these intertwined forces accelerated
    industrial growth and reshaped societal structures.
    "

    >>> # Minimal example focusing on relative importance scoring
    >>> social_analysis = {"number_of_factors":1,"social_factors":["Migration"],
    "impact_scores":[0.7],"summary":"Population shifts reshaped communities."}
    >>> political_analysis = {"political_decisions":[],"policies_influenced":[],
    "leadership_figures":[],"summary":"Political stability maintained."}
    >>> economic_analysis = {"economic_factor_name":"Export
    Boom","impact_summary":"Exports surged, boosting GDP.","evidence_sources":[]
    ,"impact_strength":0.8,"time_period_affected":"1980s","is_consensus":true}
    >>> cultural_analysis = {"cultural_factors":[],"factor_categories":[],"facto
    r_descriptions":[],"influence_scores":[],"is_significant":[]}
    >>> result = synthesize_influences(social_analysis, political_analysis,
    economic_analysis, cultural_analysis)
    >>> print(result["importance_scores"])
    [0.7, 0.1, 0.8, 0.0]

    """
    validate_required_keys(social_input=analyze_social_influences_input, political_input=analyze_political_influences_input, economic_input=analyze_economic_influences_input, cultural_input=analyze_cultural_influences_input)
    
    social_insights: str = extract_social_insights(social_analysis=analyze_social_influences_input)
    political_insights: str = extract_political_insights(political_analysis=analyze_political_influences_input)
    economic_insights: str = extract_economic_insights(economic_analysis=analyze_economic_influences_input)
    cultural_insights: str = extract_cultural_insights(cultural_analysis=analyze_cultural_influences_input)
    
    interaction_points: List[str] = identify_cross_sector_interactions(social_data=analyze_social_influences_input, political_data=analyze_political_influences_input, economic_data=analyze_economic_influences_input, cultural_data=analyze_cultural_influences_input)
    
    importance_scores: List[float] = calculate_relative_importance(social_input=analyze_social_influences_input, political_input=analyze_political_influences_input, economic_input=analyze_economic_influences_input, cultural_input=analyze_cultural_influences_input)
    
    synthesis_summary: str = generate_unified_narrative(social_insights=social_insights, political_insights=political_insights, economic_insights=economic_insights, cultural_insights=cultural_insights, interactions=interaction_points)
    
    return SynthesizeInfluencesOutput(
        social_insights=social_insights,
        economic_insights=economic_insights,
        political_insights=political_insights,
        cultural_insights=cultural_insights,
        synthesis_summary=synthesis_summary,
        interaction_points=interaction_points,
        importance_scores=importance_scores
    )