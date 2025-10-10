from ._compile_historical_narrative.validate_required_inputs import validate_required_inputs
from ._compile_historical_narrative.generate_narrative_title import generate_narrative_title
from ._compile_historical_narrative.create_introduction import create_introduction
from ._compile_historical_narrative.build_historical_context import build_historical_context
from ._compile_historical_narrative.format_key_factors_for_narrative import format_key_factors_for_narrative
from ._compile_historical_narrative.synthesize_impact_summary import synthesize_impact_summary
from ._compile_historical_narrative.craft_narrative_conclusion import craft_narrative_conclusion
from ._compile_historical_narrative.compile_full_narrative import compile_full_narrative

from pydantic import BaseModel, Field
from typing import List


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


class CompileHistoricalNarrativeOutput(BaseModel):
    """Pydantic model for compile_historical_narrative node outputs."""
    narrative_title: str = (
        Field(..., description="Title of the historical narrative.")
    )
    introduction: str = (
        Field(..., description="Introductory paragraph setting the scene.")
    )
    historical_context: str = (
        Field(..., description="Summary of the historical context.")
    )
    key_factors: List[str] = (
        Field(..., description = (
            "List of key factors (cultural, economic, political, social) influencing the event.")
        )
    )
    impact_summary: str = (
        Field(..., description = (
            "Summary of how these factors impacted the event.")
        )
    )
    conclusion: str = (
        Field(..., description = (
            "Concluding remarks linking narrative to the conclusions drawn.")
        )
    )
    overall_narrative: str = (
        Field(..., description = (
            "Full cohesive narrative string combining all parts.")
        )
    )


def compile_historical_narrative(draw_conclusions_input: DrawConclusionsOutput, **kwargs) -> CompileHistoricalNarrativeOutput:
    """
    Generate a full historical narrative from analysis outputs.

    Parameters
    ----------
    conclusion_summary : str
        Concise summary of the main conclusions about the key drivers and
        outcomes.
    key_factors : List[str]
        List of primary factors identified as key drivers.
    impact_assessment : List[str]
        Assessment of each factor's impact level (e.g., 'high', 'medium',
        'low').
    confidence_score : float
        Overall confidence level (0‑1) in the conclusions.
    recommendations : List[str]
        Actionable recommendations or implications derived from the
        conclusions.
    historical_event : str
        Name or title of the historical event or period being studied.
    time_frame : str
        Approximate time range (e.g., years) of the event or period.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing narrative_title, introduction,
        historical_context, key_factors, impact_summary, conclusion, and
        overall_narrative.

    Raises
    ------
    ValueError
        Raised when any required input is empty or missing.

    Examples
    --------
    >>> output = compile_historical_narrative(
    ...     conclusion_summary='The Industrial Revolution transformed labor and
    technology.',
    ...     key_factors=['Technological Innovation', 'Urbanization', 'Capital
    Accumulation'],
    ...     impact_assessment=['high', 'medium', 'high'],
    ...     confidence_score=0.92,
    ...     recommendations=['Study early factory labor laws.', 'Examine urban
    planning impact.'],
    ...     historical_event='Industrial Revolution',
    ...     time_frame='18th–19th centuries'"
                ")
    >>> print(output['overall_narrative'])
    "The Industrial Revolution: A Transformational Epoch\n\nThe Industrial
    Revolution, spanning the 18th–19th centuries, marked a profound shift in
    societal structure, fueled by Technological Innovation, Urbanization, and
    Capital Accumulation. These key drivers—each assessed as either high or
    medium impact—redefined labor, production, and urban life.\n\nThe analysis
    concludes that technological progress and capital flows were the dominant
    forces, with urbanization acting as a catalyst that accelerated change. The
    high confidence score of 0.92 underscores the robustness of these
    findings.\n\nImplications include a deeper study of early factory labor laws
    and the long-term effects of urban planning during this era.\n"

    >>> output = compile_historical_narrative(
    ...     conclusion_summary='The Fall of the Berlin Wall symbolized the end
    of the Cold War.',
    ...     key_factors=['Political Reform', 'Economic Strain', 'Public
    Protest'],
    ...     impact_assessment=['high', 'medium', 'high'],
    ...     confidence_score=0.88,
    ...     recommendations=['Investigate policy shifts post-1989.', 'Assess
    economic integration effects.'],
    ...     historical_event='Fall of the Berlin Wall',
    ...     time_frame='1989'"
                ")
    >>> print(output['overall_narrative'])
    "Fall of the Berlin Wall: The Collapse of Cold War Ideologies\n\nSet against
    the backdrop of 1989, the fall of the Berlin Wall marked the culmination of
    political reform, economic strain, and public protest in the Eastern Bloc.
    These key drivers—particularly the high-impact political reform and public
    protest—collectively accelerated the collapse of the Soviet sphere.\n\nThe
    narrative concludes that the political and social forces outweighed economic
    pressures, a finding reflected in the 0.88 confidence
    score.\n\nRecommendations for further study include a detailed examination
    of the policy shifts after 1989 and the economic integration outcomes that
    followed.\n"

    """
    historical_event: str = kwargs.get('historical_event', '')
    time_frame: str = kwargs.get('time_frame', '')
    
    validate_required_inputs(draw_conclusions_input, historical_event, time_frame)
    
    narrative_title: str = generate_narrative_title(event=historical_event, time_frame=time_frame)
    
    introduction: str = create_introduction(event=historical_event, time_frame=time_frame, context=draw_conclusions_input.conclusion_summary)
    
    historical_context: str = build_historical_context(event=historical_event, time_frame=time_frame, factors=draw_conclusions_input.key_factors)
    
    key_factors_narrative: List[str] = format_key_factors_for_narrative(factors=draw_conclusions_input.key_factors, assessments=draw_conclusions_input.impact_assessment)
    
    impact_summary: str = synthesize_impact_summary(factors=draw_conclusions_input.key_factors, assessments=draw_conclusions_input.impact_assessment, conclusion=draw_conclusions_input.conclusion_summary)
    
    conclusion: str = craft_narrative_conclusion(confidence=draw_conclusions_input.confidence_score, recommendations=draw_conclusions_input.recommendations, summary=draw_conclusions_input.conclusion_summary)
    
    overall_narrative: str = compile_full_narrative(title=narrative_title, intro=introduction, context=historical_context, impact=impact_summary, conclusion=conclusion)
    
    return CompileHistoricalNarrativeOutput(
        narrative_title=narrative_title,
        introduction=introduction,
        historical_context=historical_context,
        key_factors=key_factors_narrative,
        impact_summary=impact_summary,
        conclusion=conclusion,
        overall_narrative=overall_narrative
    )