from pydantic import BaseModel, Field
from typing import List


class AnalyzeMarketTrendsOutput(BaseModel):
    """Pydantic model for analyze_market_trends node outputs."""
    trend_indicators: List[float] = (
        Field(..., description="List of trend indicators, such as moving averages.")
    )
    pattern_recognition: List[str] = (
        Field(..., description="List of identified patterns, such as 'bullish' or 'bearish'.")
    )


class DefineTradingRulesOutput(BaseModel):
    """Pydantic model for define_trading_rules node outputs."""
    buy_rules: List[str] = (
        Field(..., description="List of conditions for buying stocks.")
    )
    sell_rules: List[str] = (
        Field(..., description="List of conditions for selling stocks.")
    )


def define_trading_rules(analyze_market_trends_input: AnalyzeMarketTrendsOutput, **kwargs) -> DefineTradingRulesOutput:
    """
    Define trading rules based on market trend analysis.

    Parameters
    ----------
    trend_indicators : List[float]
        List of trend indicators, such as moving averages, from the market
        trend analysis.
    pattern_recognition : List[str]
        List of identified patterns, such as 'bullish' or 'bearish', from
        the market trend analysis.

    Returns
    -------
    {'buy_rules': List[str], 'sell_rules': List[str]}
        Dictionary containing lists of conditions for buying and selling
        stocks based on the trend analysis.

    Raises
    ------
    ValueError
        If trend indicators or pattern recognition results are invalid or
        inconsistent.

    Examples
    --------
    >>> trend_indicators = [50.0, 200.0]
    >>> pattern_recognition = ['bullish', 'bearish']
    >>> result = define_trading_rules(trend_indicators, pattern_recognition)
    {'buy_rules': ['price > 50', 'macd > signal'], 'sell_rules': ['price < 200',
    'rsi > 70']}

    >>> trend_indicators = [100.0, 50.0]
    >>> pattern_recognition = ['bearish', 'bullish']
    >>> result = define_trading_rules(trend_indicators, pattern_recognition)
    {'buy_rules': ['price > 100', 'stochastic < 20'], 'sell_rules': ['price <
    50', 'macd < signal']}

    """
    return DefineTradingRulesOutput(
        buy_rules=[],
        sell_rules=[],
    )