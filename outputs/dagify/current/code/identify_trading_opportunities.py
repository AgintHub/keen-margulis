from ._identify_trading_opportunities.validate_historical_data import validate_historical_data
from ._identify_trading_opportunities.validate_trend_analysis import validate_trend_analysis
from ._identify_trading_opportunities.analyze_price_patterns import analyze_price_patterns
from ._identify_trading_opportunities.analyze_volume_patterns import analyze_volume_patterns
from ._identify_trading_opportunities.combine_trend_indicators import combine_trend_indicators
from ._identify_trading_opportunities.merge_trading_signals import merge_trading_signals
from ._identify_trading_opportunities.filter_trading_opportunities import filter_trading_opportunities
from ._identify_trading_opportunities.rank_and_select_opportunities import rank_and_select_opportunities

from pydantic import BaseModel, Field
from typing import List


class CollectHistoricalMarketDataOutput(BaseModel):
    """Pydantic model for collect_historical_market_data node outputs."""
    historical_prices: List[float] = (
        Field(..., description="List of historical prices")
    )
    historical_volumes: List[float] = (
        Field(..., description="List of historical volumes")
    )
    other_metrics: List[str] = (
        Field(..., description="Other relevant historical metrics")
    )


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[str] = (
        Field(..., description="List of trend indicators")
    )
    trend_directions: List[str] = (
        Field(..., description="List of trend directions")
    )


class IdentifyTradingOpportunitiesOutput(BaseModel):
    """Pydantic model for identify_trading_opportunities node outputs."""
    trading_opportunities: List[str] = (
        Field(..., description="List of potential trading opportunities")
    )


def identify_trading_opportunities(collect_historical_market_data_input: CollectHistoricalMarketDataOutput, analyze_market_trends_input: AnalyzeMarketTrendsOutput, **kwargs) -> IdentifyTradingOpportunitiesOutput:
    """
    Identify potential trading opportunities based on historical market data and
    trend analysis.

    Parameters
    ----------
    historical_market_data : dict
        Historical market data including prices, volumes, and other relevant
        metrics from 'collect_historical_market_data' node.
    trend_analysis : dict
        Trend indicators and directions from 'analyze_market_trends' node.

    Returns
    -------
    List[str]
        List of identified trading opportunities.

    Raises
    ------
    ValueError
        If historical market data or trend analysis is missing or malformed.

    Examples
    --------
    >>> historical_data = {'historical_prices': [100.0, 120.0, 110.0],
    'historical_volumes': [1000, 1200, 1100], 'other_metrics': ['metric1',
    'metric2']}
    >>> trend_analysis = {'trend_indicators': ['indicator1', 'indicator2'],
    'trend_directions': ['up', 'down']}
    >>> trading_opportunities = identify_trading_opportunities(historical_data,
    trend_analysis)
    ['buy', 'sell']

    """
    validate_historical_data(historical_data=collect_historical_market_data_input)
    validate_trend_analysis(trend_analysis=analyze_market_trends_input)
    
    price_signals: List[str] = analyze_price_patterns(prices=collect_historical_market_data_input.historical_prices)
    volume_signals: List[str] = analyze_volume_patterns(volumes=collect_historical_market_data_input.historical_volumes)
    trend_signals: List[str] = combine_trend_indicators(indicators=analyze_market_trends_input.trend_indicators, directions=analyze_market_trends_input.trend_directions)
    
    all_signals: List[str] = merge_trading_signals(price_signals=price_signals, volume_signals=volume_signals, trend_signals=trend_signals)
    filtered_opportunities: List[str] = filter_trading_opportunities(signals=all_signals, other_metrics=collect_historical_market_data_input.other_metrics)
    final_opportunities: List[str] = rank_and_select_opportunities(opportunities=filtered_opportunities)
    
    return IdentifyTradingOpportunitiesOutput(trading_opportunities=final_opportunities)