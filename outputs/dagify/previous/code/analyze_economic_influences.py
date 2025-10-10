from ._analyze_economic_influences.validate_economic_factors_input import validate_economic_factors_input
from ._analyze_economic_influences.analyze_factor_impact import analyze_factor_impact
from ._analyze_economic_influences.gather_evidence_sources import gather_evidence_sources
from ._analyze_economic_influences.format_evidence_sources import format_evidence_sources
from ._analyze_economic_influences.calculate_impact_strength import calculate_impact_strength
from ._analyze_economic_influences.determine_time_period_affected import determine_time_period_affected
from ._analyze_economic_influences.check_scholarly_consensus import check_scholarly_consensus

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
    economic_factors: List[str] = identify_key_factors_input.economic_factors
    
    validated_factors: List[str] = validate_economic_factors_input(factors=economic_factors)
    
    factor_name: str = validated_factors[0]
    
    impact_analysis: str = analyze_factor_impact(factor_name=factor_name, historical_context=kwargs.get('historical_context', ''))
    
    evidence_list: List[str] = gather_evidence_sources(factor_name=factor_name)
    evidence_sources_str: str = format_evidence_sources(evidence_list=evidence_list)
    
    impact_strength_score: float = calculate_impact_strength(factor_name=factor_name, impact_analysis=impact_analysis)
    
    time_period: str = determine_time_period_affected(factor_name=factor_name, historical_context=kwargs.get('historical_context', ''))
    
    consensus_status: bool = check_scholarly_consensus(factor_name=factor_name)
    
    return AnalyzeEconomicInfluencesOutput(
        economic_factor_name=factor_name,
        impact_summary=impact_analysis,
        evidence_sources=evidence_sources_str,
        impact_strength=impact_strength_score,
        time_period_affected=time_period,
        is_consensus=consensus_status
    )