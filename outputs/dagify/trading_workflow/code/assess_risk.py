from pydantic import BaseModel, Field
from typing import List


class FetchMarketDataOutput(BaseModel):
    """Pydantic model for fetch_market_data node outputs."""
    current_prices: List[float] = (
        Field(..., description="List of current stock prices.")
    )
    historical_data: List[float] = (
        Field(..., description="2D list of historical stock prices and volumes.")
    )


class AssessRiskOutput(BaseModel):
    """Pydantic model for assess_risk node outputs."""
    risk_levels: List[float] = (
        Field(..., description="List of risk levels associated with potential trades.")
    )
    risk_factors: List[str] = (
        Field(..., description="List of factors contributing to the risk assessment.")
    )


def assess_risk(fetch_market_data_input: FetchMarketDataOutput, **kwargs) -> AssessRiskOutput:
    """
    Assess the risk associated with potential trades based on current market
    conditions.

    Parameters
    ----------
    market_data : Dict[str, List[float]]
        Dictionary containing current prices and historical data fetched
        from fetch_market_data.

    Returns
    -------
    Tuple[List[float], List[str]]
        A tuple containing a list of risk levels and a list of risk factors.

    Raises
    ------
    ValueError
        If market_data is empty or does not contain the required keys.

    Examples
    --------
    >>> market_data = {'current_prices': [100.0, 200.0], 'historical_data':
    [[90.0, 100.0], [190.0, 200.0]]}
    >>> risk_levels, risk_factors = assess_risk(market_data)
    ([0.5, 0.3], ['volatility', 'liquidity'])

    >>> market_data = {'current_prices': [150.0, 250.0], 'historical_data':
    [[140.0, 150.0], [240.0, 250.0]]}
    >>> risk_levels, risk_factors = assess_risk(market_data)
    ([0.4, 0.2], ['market_trend', 'economic_indicators'])

    """
    return AssessRiskOutput(
        risk_levels=[],
        risk_factors=[],
    )