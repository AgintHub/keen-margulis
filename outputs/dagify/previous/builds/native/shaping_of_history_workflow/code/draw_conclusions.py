from pydantic import BaseModel, Field
from typing import List


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


class DrawConclusionsOutput(BaseModel):
    """Pydantic model for draw_conclusions node outputs."""
    conclusion_summary: str = (
        Field(..., description = (
            "Concise summary of the main conclusions about the key drivers and outcomes.")
        )
    )
    key_factors: List[str] = (
        Field(..., description = (
            "List of primary factors identified as key drivers.")
        )
    )
    impact_assessment: List[str] = (
        Field(..., description = (
            "Assessment of each factor's impact level (e.g., high, medium, low).")
        )
    )
    confidence_score: float = (
        Field(..., description = (
            "Overall confidence level (0-1) in the conclusions.")
        )
    )
    recommendations: List[str] = (
        Field(..., description = (
            "Actionable recommendations or implications derived from the conclusions.")
        )
    )


def draw_conclusions(synthesize_influences_input: SynthesizeInfluencesOutput, **kwargs) -> DrawConclusionsOutput:
    """
    Generate a structured set of conclusions about a historical event based on
    synthesized influence data.

    Parameters
    ----------
    synthesis : dict
        Dictionary containing the outputs of `synthesize_influences`,
        including key insights and interaction points.

    Returns
    -------
    dict
        Dictionary matching the `draw_conclusions` output structure.

    Raises
    ------
    ValueError
        If `synthesis` is missing required keys or contains invalid data.

    Examples
    --------
    >>> synth = {
    ...     'social_insights': 'Social unrest spurred reforms.',
    ...     'economic_insights': 'Industrial growth fueled capital
    accumulation.',
    ...     'political_insights': 'New constitution centralized authority.',
    ...     'cultural_insights': 'Romanticism challenged traditional norms.',
    ...     'synthesis_summary': 'Multiple fronts converged to reshape
    governance.',
    ...     'interaction_points': ['Economic growth ↔ Political reform',
    'Cultural shifts ↔ Social movements'],
    ...     'importance_scores': [0.8, 0.9, 0.7, 0.6]
    >>> }
    {
      'conclusion_summary': 'The era was driven by intertwined social, economic,
    political, and cultural forces that collectively accelerated institutional
    change.',
      'key_factors': ['Economic Growth', 'Political Reform', 'Social Unrest',
    'Cultural Shifts'],
      'impact_assessment': ['high', 'high', 'medium', 'medium'],
      'confidence_score': 0.88,
      'recommendations': ['Focus on sustaining economic diversification',
    'Encourage inclusive political dialogues', 'Support cultural initiatives
    that bridge tradition and innovation']
    }

    >>> synth = {
    ...     'social_insights': 'Demographic shifts altered labor markets.',
    ...     'economic_insights': 'Trade embargoes disrupted supply chains.',
    ...     'political_insights': 'Leadership turnover destabilized
    governance.',
    ...     'cultural_insights': 'Artistic movements reflected societal
    tensions.',
    ...     'synthesis_summary': 'A fragile equilibrium existed between
    competing pressures.',
    ...     'interaction_points': ['Economic disruption ↔ Political
    instability'],
    ...     'importance_scores': [0.6, 0.7, 0.5, 0.4]
    >>> }
    {
      'conclusion_summary': 'Instability arose from the interplay of economic
    shocks, political turbulence, and cultural expression.',
      'key_factors': ['Trade Embargoes', 'Leadership Turnover', 'Demographic
    Shifts', 'Artistic Movements'],
      'impact_assessment': ['high', 'medium', 'medium', 'low'],
      'confidence_score': 0.72,
      'recommendations': ['Reform trade policies', 'Promote political stability
    mechanisms', 'Invest in social cohesion programs']
    }

    """
    return DrawConclusionsOutput(
        conclusion_summary="",
        key_factors=[],
        impact_assessment=[],
        confidence_score=0.0,
        recommendations=[],
    )