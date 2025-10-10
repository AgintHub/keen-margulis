from typing import List


def get_available_trading_strategies() -> List[str]:
    """
    Retrieve a list of available trading strategies.

    Returns
    -------
    List[str]
        A list of available trading strategies as strings.

    Raises
    ------
    RuntimeError
        If the list of available trading strategies cannot be retrieved.

    Examples
    --------
    >>> available_strategies = get_available_trading_strategies()
    ['Strategy1', 'Strategy2', 'Strategy3']

    """
    try:
        strategies = [
            "MovingAverageCrossover",
            "RSIStrategy",
            "BollingerBands",
            "MACDStrategy",
            "MeanReversion",
            "MomentumStrategy",
            "PairsTradingStrategy",
            "ArbitrageStrategy",
            "TrendFollowing",
            "GridTradingStrategy"
        ]
        return strategies
    except Exception as e:
        raise RuntimeError("If the list of available trading strategies cannot be retrieved.") from e