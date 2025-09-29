from ._assess_risk.validate_market_data import validate_market_data
from ._assess_risk.calculate_volatility import calculate_volatility
from ._assess_risk.analyze_liquidity import analyze_liquidity
from ._assess_risk.analyze_market_trends import analyze_market_trends
from ._assess_risk.fetch_economic_indicators import fetch_economic_indicators
from ._assess_risk.compute_composite_risk_scores import compute_composite_risk_scores
from ._assess_risk.identify_primary_risk_factors import identify_primary_risk_factors

from pydantic import BaseModel, Field
from typing import List


class FetchMarketDataOutput(BaseModel):
    """Pydantic model for fetch_market_data node outputs."""
    market_prices: List[float] = (
        Field(..., description="List of current market prices.")
    )
    market_volumes: List[int] = (
        Field(..., description="List of current market volumes.")
    )


class AssessRiskOutput(BaseModel):
    """Pydantic model for assess_risk node outputs."""
    risk_levels: List[float] = (
        Field(..., description="List of risk levels associated with different trades.")
    )
    risk_factors: List[str] = (
        Field(..., description="List of factors contributing to the risk assessment.")
    )


def assess_risk(fetch_market_data_input: FetchMarketDataOutput, **kwargs) -> AssessRiskOutput:
    """
    Assess the risk associated with potential trades based on market data
    fetched from reliable sources.

    Parameters
    ----------
    market_prices : List[float]
        List of current market prices fetched from reliable sources.
    market_volumes : List[int]
        List of current market volumes fetched from reliable sources.

    Returns
    -------
    Tuple[List[float], List[str]]
        A tuple containing a list of risk levels associated with different
        trades and a list of factors contributing to the risk assessment.

    Raises
    ------
    ValueError
        If market_prices or market_volumes are empty or invalid.

    Examples
    --------
    >>> market_prices = [100.0, 120.0, 90.0]
    >>> market_volumes = [1000, 1500, 800]
    >>> risk_levels, risk_factors = assess_risk(market_prices, market_volumes)
    risk_levels = [0.5, 0.7, 0.3], risk_factors = ['volatility', 'market_trend',
    'liquidity']

    >>> market_prices = [80.0, 110.0, 130.0]
    >>> market_volumes = [500, 2000, 1200]
    >>> risk_levels, risk_factors = assess_risk(market_prices, market_volumes)
    risk_levels = [0.4, 0.8, 0.6], risk_factors = ['market_trend', 'volatility',
    'economic_indicators']

    """
    market_prices = fetch_market_data_input.market_prices
    market_volumes = fetch_market_data_input.market_volumes
    
    validate_market_data(prices=market_prices, volumes=market_volumes)
    
    volatility_metrics: List[float] = calculate_volatility(prices=market_prices)
    liquidity_metrics: List[float] = analyze_liquidity(volumes=market_volumes, prices=market_prices)
    trend_analysis: List[float] = analyze_market_trends(prices=market_prices)
    economic_indicators: List[float] = fetch_economic_indicators()
    
    risk_components: List[List[float]] = [volatility_metrics, liquidity_metrics, trend_analysis, economic_indicators]
    risk_levels: List[float] = compute_composite_risk_scores(components=risk_components)
    
    risk_factors: List[str] = identify_primary_risk_factors(volatility=volatility_metrics, liquidity=liquidity_metrics, trends=trend_analysis, economic=economic_indicators)
    
    return AssessRiskOutput(risk_levels=risk_levels, risk_factors=risk_factors)