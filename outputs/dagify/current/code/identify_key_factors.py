from ._identify_key_factors.validate_input_parameters import validate_input_parameters
from ._identify_key_factors.gather_historical_data import gather_historical_data
from ._identify_key_factors.extract_social_factors import extract_social_factors
from ._identify_key_factors.extract_political_factors import extract_political_factors
from ._identify_key_factors.extract_economic_factors import extract_economic_factors
from ._identify_key_factors.extract_cultural_factors import extract_cultural_factors

from pydantic import BaseModel, Field
from typing import List


class DefineHistoricalContextOutput(BaseModel):
    """Pydantic model for define_historical_context node outputs."""
    historical_event: str = (
        Field(..., description = (
            "The name or title of the historical event or period being studied")
        )
    )
    time_frame: str = (
        Field(..., description = (
            "The approximate time range (e.g., years or dates) of the event or period")
        )
    )


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


def identify_key_factors(define_historical_context_input: DefineHistoricalContextOutput, **kwargs) -> IdentifyKeyFactorsOutput:
    """
    Identify the primary social, political, economic, and cultural factors that
    shaped a specific historical event or period.

    Parameters
    ----------
    historical_event : str
        The name or title of the historical event or period being studied.
    time_frame : str
        Approximate time range of the event (e.g., years or dates).

    Returns
    -------
    Dict[str, List[str]]
        A dictionary containing four lists of factor names, one for each
        domain: social, political, economic, and cultural.

    Raises
    ------
    ValueError
        Raised when either `historical_event` or `time_frame` is empty or
        None.

    Examples
    --------
    >>> social_factors, political_factors, economic_factors, cultural_factors =
    identify_key_factors('French Revolution', '1789-1799')
    >>> print('Social:', social_factors)
    >>> print('Political:', political_factors)
    Social: ['Monarchy', 'Social Inequality', 'Enlightenment Ideas']
    Political: ['Absolute Monarchy', 'Reign of Terror', 'Constitutional
    Reforms']

    >>> factors = identify_key_factors('Renaissance', '1400-1600')
    >>> print(factors['cultural_factors'])
    ['Humanism', 'Artistic Patronage', 'Scientific Curiosity']

    """
    validate_input_parameters(event=define_historical_context_input.historical_event, timeframe=define_historical_context_input.time_frame)
    
    contextual_data: dict = gather_historical_data(event=define_historical_context_input.historical_event, time_period=define_historical_context_input.time_frame)
    
    social_factors: List[str] = extract_social_factors(historical_data=contextual_data, event=define_historical_context_input.historical_event)
    political_factors: List[str] = extract_political_factors(historical_data=contextual_data, event=define_historical_context_input.historical_event)
    economic_factors: List[str] = extract_economic_factors(historical_data=contextual_data, event=define_historical_context_input.historical_event)
    cultural_factors: List[str] = extract_cultural_factors(historical_data=contextual_data, event=define_historical_context_input.historical_event)
    
    return IdentifyKeyFactorsOutput(
        social_factors=social_factors,
        political_factors=political_factors,
        economic_factors=economic_factors,
        cultural_factors=cultural_factors,
    )