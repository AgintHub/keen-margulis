from ._determine_trading_parameters.validate_account_data import validate_account_data
from ._determine_trading_parameters.validate_market_trends_data import validate_market_trends_data
from ._determine_trading_parameters.calculate_base_risk_tolerance import calculate_base_risk_tolerance
from ._determine_trading_parameters.analyze_market_risk_from_trends import analyze_market_risk_from_trends
from ._determine_trading_parameters.adjust_risk_tolerance import adjust_risk_tolerance
from ._determine_trading_parameters.calculate_position_sizing import calculate_position_sizing

from pydantic import BaseModel, Field
from typing import List


class CollectAccountDataOutput(BaseModel):
    """Pydantic model for collect_account_data node outputs."""
    account_balance: float = Field(..., description="Current account balance")
    positions: str = Field(..., description="List of current positions")


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[str] = (
        Field(..., description="List of trend indicators")
    )
    trend_directions: List[str] = (
        Field(..., description="List of trend directions")
    )


class DetermineTradingParametersOutput(BaseModel):
    """Pydantic model for determine_trading_parameters node outputs."""
    risk_tolerance: float = (
        Field(..., description="Risk tolerance level between 0 and 1")
    )
    position_sizing: float = (
        Field(..., description="Position sizing strategy as a proportion of account balance")
    )


def determine_trading_parameters(collect_account_data_input: CollectAccountDataOutput, analyze_market_trends_input: AnalyzeMarketTrendsOutput, **kwargs) -> DetermineTradingParametersOutput:
    """
    Determines trading parameters including risk tolerance and position sizing
    based on account data and market trends.

    Parameters
    ----------
    account_data : dict
        Account data including balance and positions, typically output from
        'collect_account_data' node.
    market_trends : dict
        Market trends analysis including trend indicators and directions,
        typically output from 'analyze_market_trends' node.

    Returns
    -------
    dict
        Dictionary containing 'risk_tolerance' and 'position_sizing' as
        floats.

    Raises
    ------
    ValueError
        If account balance is negative or if market trends data is
        inconsistent.
    TypeError
        If input data types are incorrect or missing required fields.

    Examples
    --------
    >>> account_data = {'account_balance': 10000.0, 'positions': ['AAPL',
    'GOOG']}
    >>> market_trends = {'trend_indicators': ['MACD', 'RSI'],
    'trend_directions': ['UP', 'DOWN']}
    >>> trading_params = determine_trading_parameters(account_data,
    market_trends)
    {'risk_tolerance': 0.5, 'position_sizing': 0.2}

    >>> account_data = {'account_balance': 5000.0, 'positions': ['AMZN']}
    >>> market_trends = {'trend_indicators': ['SMA'], 'trend_directions':
    ['UP']}
    >>> trading_params = determine_trading_parameters(account_data,
    market_trends)
    {'risk_tolerance': 0.3, 'position_sizing': 0.15}

    """
    validate_account_data(account_balance=collect_account_data_input.account_balance, positions=collect_account_data_input.positions)
    validate_market_trends_data(trend_indicators=analyze_market_trends_input.trend_indicators, trend_directions=analyze_market_trends_input.trend_directions)
    
    base_risk_tolerance: float = calculate_base_risk_tolerance(account_balance=collect_account_data_input.account_balance)
    market_risk_adjustment: float = analyze_market_risk_from_trends(trend_indicators=analyze_market_trends_input.trend_indicators, trend_directions=analyze_market_trends_input.trend_directions)
    final_risk_tolerance: float = adjust_risk_tolerance(base_risk=base_risk_tolerance, market_adjustment=market_risk_adjustment)
    
    position_sizing: float = calculate_position_sizing(account_balance=collect_account_data_input.account_balance, risk_tolerance=final_risk_tolerance, current_positions=collect_account_data_input.positions)
    
    return DetermineTradingParametersOutput(
        risk_tolerance=final_risk_tolerance,
        position_sizing=position_sizing
    )