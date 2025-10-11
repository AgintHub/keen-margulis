from ._assess_market_trends.validate_market_trends_data import validate_market_trends_data
from ._assess_market_trends.process_market_trends import process_market_trends
from ._assess_market_trends.identify_market_opportunities import identify_market_opportunities
from ._assess_market_trends.identify_market_threats import identify_market_threats
from ._assess_market_trends.generate_market_forecast import generate_market_forecast

from pydantic import BaseModel, Field
from typing import List


class GatherWcfbDataOutput(BaseModel):
    """Pydantic model for gather_wcfb_data node outputs."""
    business_operations_data: str = (
        Field(..., description="Data related to business operations")
    )
    customer_feedback_data: str = (
        Field(..., description="List of customer feedback comments")
    )
    market_trends_data: float = (
        Field(..., description="List of market trend metrics")
    )


class AssessMarketTrendsOutput(BaseModel):
    """Pydantic model for assess_market_trends node outputs."""
    market_opportunities: List[str] = (
        Field(..., description="List of market opportunities")
    )
    market_threats: List[str] = Field(..., description="List of market threats")
    trend_forecast: str = (
        Field(..., description="Forecast of future market trends")
    )


def assess_market_trends(gather_wcfb_data_input: GatherWcfbDataOutput, **kwargs) -> AssessMarketTrendsOutput:
    """
    Assess market trends based on gathered data to identify opportunities,
    threats, and forecast future trends.

    Parameters
    ----------
    market_trends_data : List[float]
        List of market trend metrics gathered from various sources.

    Returns
    -------
    Tuple[List[str], List[str], str]
        A tuple containing a list of market opportunities, a list of market
        threats, and a forecast of future market trends.

    Raises
    ------
    ValueError
        If market_trends_data is empty or not a list of floats.

    Examples
    --------
    >>> assess_market_trends(market_trends_data=[0.5, 0.7, 0.3])
    (['growing demand'], ['increasing competition'], 'The market is expected to
    grow steadily.')

    >>> assess_market_trends(market_trends_data=[0.2, 0.4, 0.1])
    (['niche market'], ['declining trend'], 'The market is showing signs of
    decline.')

    """
    validated_data: List[float] = validate_market_trends_data(data=gather_wcfb_data_input.market_trends_data)
    
    processed_trends: dict = process_market_trends(trends_data=validated_data)
    
    opportunities: List[str] = identify_market_opportunities(trends_analysis=processed_trends)
    
    threats: List[str] = identify_market_threats(trends_analysis=processed_trends)
    
    forecast: str = generate_market_forecast(trends_analysis=processed_trends, opportunities=opportunities, threats=threats)
    
    return AssessMarketTrendsOutput(
        market_opportunities=opportunities,
        market_threats=threats,
        trend_forecast=forecast
    )