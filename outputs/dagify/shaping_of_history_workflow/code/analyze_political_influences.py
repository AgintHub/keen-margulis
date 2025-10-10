from ._analyze_political_influences.validate_political_factors import validate_political_factors
from ._analyze_political_influences.extract_political_decisions import extract_political_decisions
from ._analyze_political_influences.identify_policies_influenced import identify_policies_influenced
from ._analyze_political_influences.extract_leadership_figures import extract_leadership_figures
from ._analyze_political_influences.synthesize_political_summary import synthesize_political_summary

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


def analyze_political_influences(identify_key_factors_input: IdentifyKeyFactorsOutput, **kwargs) -> AnalyzePoliticalInfluencesOutput:
    """
    Generates a structured summary of the political influences affecting a
    historical event, based on primary political factors identified by the
    previous node.

    Parameters
    ----------
    political_factors : List[str]
        List of primary political factors (e.g., treaties, revolutions,
        wars) supplied by the identify_key_factors node.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing four keys: - political_decisions: List of
        key decisions. - policies_influenced: List of policies that were
        enacted. - leadership_figures: List of main political leaders. -
        summary: A concise narrative describing the political influence.

    Raises
    ------
    ValueError
        Raised if political_factors is empty or None.
    TypeError
        Raised if political_factors is not a list.

    Examples
    --------
    >>> result = analyze_political_influences([
    ...     'Treaty of Versailles',
    ...     'French Revolution',
    ...     'Napoleonic Wars'
    >>> ])
    >>> print(result['summary'])
    "The Treaty of Versailles, the French Revolution, and the Napoleonic Wars
    collectively redefined European borders, governance structures, and
    international law, setting the stage for the modern nation-state system."

    >>> result = analyze_political_influences(['Industrial Revolution'])
    >>> print(result['political_decisions'])
    "['Industrial Revolution']"

    """
    political_factors: List[str] = identify_key_factors_input.political_factors
    
    validate_political_factors(factors=political_factors)
    
    key_decisions: List[str] = extract_political_decisions(political_factors=political_factors)
    
    influenced_policies: List[str] = identify_policies_influenced(political_factors=political_factors)
    
    leadership_figures: List[str] = extract_leadership_figures(political_factors=political_factors)
    
    political_summary: str = synthesize_political_summary(
        decisions=key_decisions,
        policies=influenced_policies, 
        leaders=leadership_figures,
        factors=political_factors
    )
    
    return AnalyzePoliticalInfluencesOutput(
        political_decisions=key_decisions,
        policies_influenced=influenced_policies,
        leadership_figures=leadership_figures,
        summary=political_summary
    )