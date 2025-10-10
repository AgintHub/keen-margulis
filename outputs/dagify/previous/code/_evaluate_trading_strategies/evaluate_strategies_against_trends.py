from typing import List


def evaluate_strategies_against_trends(strategies: str, trend_indicators: str, pattern_recognition: str) -> List[str]:
    """
    Evaluates trading strategies against market trends and pattern recognition.

    Parameters
    ----------
    strategies : str
        A string representing available trading strategies.
    trend_indicators : str
        A string containing indicators of market trends (e.g., bullish,
        bearish).
    pattern_recognition : str
        A string containing patterns recognized in the market data.

    Returns
    -------
    List[str]
        A list of strings representing evaluations of different trading
        strategies.

    Raises
    ------
    ValueError
        If any of the input strings are empty or malformed.
    TypeError
        If any of the input parameters are not strings.

    Examples
    --------
    >>> evaluate_strategies_against_trends(strategies='mean_reversion,trend_foll
    owing', trend_indicators='bullish,bearish',
    pattern_recognition='head_and_shoulders,double_bottom')
    ['mean_reversion:strong_buy', 'trend_following:strong_sell']

    >>> evaluate_strategies_against_trends(strategies='statistical_arbitrage',
    trend_indicators='neutral', pattern_recognition='ascending_triangle')
    ['statistical_arbitrage:buy']

    """
    if not isinstance(strategies, str):
        raise TypeError("strategies parameter must be a string")
    if not isinstance(trend_indicators, str):
        raise TypeError("trend_indicators parameter must be a string")
    if not isinstance(pattern_recognition, str):
        raise TypeError("pattern_recognition parameter must be a string")
    
    if not strategies.strip() or not trend_indicators.strip() or not pattern_recognition.strip():
        raise ValueError("Input strings cannot be empty or malformed")
    
    strategy_list = [s.strip() for s in strategies.split(',') if s.strip()]
    trend_list = [t.strip() for t in trend_indicators.split(',') if t.strip()]
    pattern_list = [p.strip() for p in pattern_recognition.split(',') if p.strip()]
    
    evaluations = []
    
    for strategy in strategy_list:
        if strategy == 'mean_reversion':
            if 'bearish' in trend_list or 'head_and_shoulders' in pattern_list or 'double_bottom' in pattern_list:
                evaluations.append(f'{strategy}:strong_buy')
            elif 'bullish' in trend_list:
                evaluations.append(f'{strategy}:sell')
            elif 'neutral' in trend_list:
                evaluations.append(f'{strategy}:hold')
            else:
                evaluations.append(f'{strategy}:hold')
        elif strategy == 'trend_following':
            if 'bullish' in trend_list or 'ascending_triangle' in pattern_list:
                evaluations.append(f'{strategy}:strong_buy')
            elif 'bearish' in trend_list or 'head_and_shoulders' in pattern_list:
                evaluations.append(f'{strategy}:strong_sell')
            elif 'neutral' in trend_list:
                evaluations.append(f'{strategy}:hold')
            else:
                evaluations.append(f'{strategy}:hold')
        elif strategy == 'statistical_arbitrage':
            if 'neutral' in trend_list or 'ascending_triangle' in pattern_list:
                evaluations.append(f'{strategy}:buy')
            elif 'bullish' in trend_list or 'bearish' in trend_list:
                evaluations.append(f'{strategy}:hold')
            else:
                evaluations.append(f'{strategy}:hold')
        else:
            if 'bullish' in trend_list:
                evaluations.append(f'{strategy}:buy')
            elif 'bearish' in trend_list:
                evaluations.append(f'{strategy}:sell')
            else:
                evaluations.append(f'{strategy}:hold')
    
    return evaluations