from pydantic import BaseModel, Field
from typing import List


class IdentifyTradingInstrumentsOutput(BaseModel):
    """Pydantic model for identify_trading_instruments node outputs."""
    trading_instruments: List[str] = Field(..., description="List of trading instruments identified for inclusion in the workflow.")
    exchanges: List[str] = Field(..., description="List of exchanges where the trading instruments are listed.")
    listings: List[str] = Field(..., description="List of listings or symbols for each trading instrument.")
    market_capitalizations: List[float] = Field(..., description="List of market capitalizations for each trading instrument.")


class SelectTradingStrategyOutput(BaseModel):
    """Pydantic model for select_trading_strategy node outputs."""
    selected_strategy_name: str = Field(..., description="The name of the selected trading strategy.")
    strategy_principles: List[str] = Field(..., description="A list of key principles associated with the selected trading strategy.")
    strategy_metrics: List[str] = Field(..., description="A list of metrics used in the selected trading strategy.")


def select_trading_strategy(identify_trading_instruments_input: IdentifyTradingInstrumentsOutput, **kwargs) -> SelectTradingStrategyOutput:
    """
    Selects a trading strategy for the trading workflow.

    Parameters
    ----------
    trading_instruments : List[str]
        List of trading instruments identified for inclusion in the
        workflow.
    exchanges : List[str]
        List of exchanges where the trading instruments are listed.
    listings : List[str]
        List of listings or symbols for each trading instrument.
    market_capitalizations : List[float]
        List of market capitalizations for each trading instrument.

    Returns
    -------
    {selected_strategy_name: str, strategy_principles: List[str], strategy_metrics: List[str]}
        A dictionary containing the selected strategy name, its key
        principles, and metrics.

    Raises
    ------
    ValueError
        If no suitable trading strategy can be found for the given
        instruments.

    Examples
    --------
    >>> select_trading_strategy(trading_instruments=['AAPL', 'GOOG'],
    exchanges=['NASDAQ'], listings=['AAPL', 'GOOG'],
    market_capitalizations=[1000.0, 500.0])
    {'selected_strategy_name': 'Mean Reversion', 'strategy_principles': ['Buy
    undervalued stocks', 'Sell overvalued stocks'], 'strategy_metrics': ['Moving
    Averages', 'Bollinger Bands']}

    """
    return SelectTradingStrategyOutput(
        selected_strategy_name="",
        strategy_principles=[],
        strategy_metrics=[],
    )