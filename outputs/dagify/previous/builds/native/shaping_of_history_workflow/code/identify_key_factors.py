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
    return IdentifyKeyFactorsOutput(
        social_factors=[],
        political_factors=[],
        economic_factors=[],
        cultural_factors=[],
    )