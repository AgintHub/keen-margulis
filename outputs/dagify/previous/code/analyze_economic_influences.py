from pydantic import BaseModel, Field
from typing import List


class IdentifyKeyFactorsOutput(BaseModel):
    """Pydantic model for identify_key_factors node outputs."""
    social_factors: List[str] = (
        Field(..., description="List of primary social factors that influenced the event or period.")
    )
    political_factors: List[str] = (
        Field(..., description="List of primary political factors that influenced the event or period.")
    )
    economic_factors: List[str] = (
        Field(..., description="List of primary economic factors that influenced the event or period.")
    )
    cultural_factors: List[str] = (
        Field(..., description="List of primary cultural factors that influenced the event or period.")
    )


class AnalyzeEconomicInfluencesOutput(BaseModel):
    """Pydantic model for analyze_economic_influences node outputs."""
    economic_factor_name: str = (
        Field(..., description="Name of the economic factor considered.")
    )
    impact_summary: str = (
        Field(..., description="Brief description of how this factor impacted the event.")
    )
    evidence_sources: str = (
        Field(..., description="List of primary source references or data points supporting the analysis.")
    )
    impact_strength: float = (
        Field(..., description="Rating of the factor's impact strength on a scale from 0 to 1.")
    )
    time_period_affected: str = (
        Field(..., description="Time period during which the factor was most influential.")
    )
    is_consensus: bool = (
        Field(..., description="Whether there is scholarly consensus on the factor's significance.")
    )


def analyze_economic_influences(identify_key_factors_input: IdentifyKeyFactorsOutput, **kwargs) -> AnalyzeEconomicInfluencesOutput:
    """
    Analyzes each economic factor from the input list and returns a structured
    assessment of its impact on the historical event or period.

    Parameters
    ----------
    economic_factors : List[str]
        List of economic factors identified by the `identify_key_factors`
        node.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries, each containing structured information about
        an economic factor.

    Raises
    ------
    ValueError
        Raised when the `economic_factors` list is empty.
    TypeError
        Raised when `economic_factors` is not a list of strings.

    Examples
    --------
    >>> analyze_economic_influences(['Inflation', 'Trade Embargo'])
    [{'economic_factor_name': 'Inflation', 'impact_summary': 'High inflation
    reduced purchasing power and disrupted domestic markets.',
    'evidence_sources': ['Economic Report 1931', 'Historical GDP Data'],
    'impact_strength': 0.85, 'time_period_affected': '1931-1933',
    'is_consensus': True}, {'economic_factor_name': 'Trade Embargo',
    'impact_summary': 'The embargo limited exports, weakening the national
    economy.', 'evidence_sources': ['Trade Records 1940', 'Diplomatic
    Correspondence'], 'impact_strength': 0.70, 'time_period_affected':
    '1940-1945', 'is_consensus': False}]

    >>> analyze_economic_influences(['Industrial Production Growth'])
    [{'economic_factor_name': 'Industrial Production Growth', 'impact_summary':
    'Rapid industrial growth fueled wartime manufacturing.', 'evidence_sources':
    ['Industrial Production Index 1944'], 'impact_strength': 0.90,
    'time_period_affected': '1942-1945', 'is_consensus': True}]

    """
    return AnalyzeEconomicInfluencesOutput(
        economic_factor_name="",
        impact_summary="",
        evidence_sources="",
        impact_strength=0.0,
        time_period_affected="",
        is_consensus=False,
    )