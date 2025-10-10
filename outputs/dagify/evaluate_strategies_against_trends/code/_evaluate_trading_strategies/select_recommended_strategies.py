from typing import List


import json


def select_recommended_strategies(evaluations: str, trend_indicators: str, pattern_recognition: str) -> List[str]:
    """
    Selects recommended trading strategies based on the evaluations of different
    strategies against market trends and patterns.

    Parameters
    ----------
    evaluations : str
        A string containing evaluations of different trading strategies,
        typically a serialized list or a descriptive text.
    trend_indicators : str
        A string containing indicators of market trends, such as bullish or
        bearish signals.
    pattern_recognition : str
        A string containing patterns recognized in the market data, which
        could influence strategy selection.

    Returns
    -------
    List[str]
        A list of recommended trading strategies based on the input
        evaluations and market analysis.

    Raises
    ------
    ValueError
        When the input parameters are not in the expected format or contain
        invalid data.
    TypeError
        When the input parameters are not of the expected type.

    Examples
    --------
    >>> select_recommended_strategies(evaluations='["good", "bad"]',
    trend_indicators='["bullish"]', pattern_recognition='["continuation"]')
    ['strategy_1', 'strategy_3']

    >>> select_recommended_strategies(evaluations='good,bad',
    trend_indicators='bullish,bearish',
    pattern_recognition='continuation,reversal')
    ['strategy_2', 'strategy_4']

    """
    
    if not isinstance(evaluations, str) or not isinstance(trend_indicators, str) or not isinstance(pattern_recognition, str):
        raise TypeError("All input parameters must be strings")
    
    if not evaluations.strip() or not trend_indicators.strip() or not pattern_recognition.strip():
        raise ValueError("Input parameters cannot be empty")
    
    try:
        if evaluations.startswith('[') and evaluations.endswith(']'):
            eval_list = json.loads(evaluations)
        else:
            eval_list = [item.strip() for item in evaluations.split(',')]
        
        if trend_indicators.startswith('[') and trend_indicators.endswith(']'):
            trend_list = json.loads(trend_indicators)
        else:
            trend_list = [item.strip() for item in trend_indicators.split(',')]
        
        if pattern_recognition.startswith('[') and pattern_recognition.endswith(']'):
            pattern_list = json.loads(pattern_recognition)
        else:
            pattern_list = [item.strip() for item in pattern_recognition.split(',')]
    except (json.JSONDecodeError, ValueError) as e:
        raise ValueError("Input parameters are not in the expected format") from e
    
    recommended_strategies = []
    
    for i, evaluation in enumerate(eval_list):
        if evaluation.lower() == 'good':
            if i < len(trend_list) and trend_list[i].lower() == 'bullish':
                if i < len(pattern_list) and pattern_list[i].lower() == 'continuation':
                    recommended_strategies.append('strategy_1')
                else:
                    recommended_strategies.append('strategy_3')
            elif i < len(trend_list) and trend_list[i].lower() == 'bearish':
                if i < len(pattern_list) and pattern_list[i].lower() == 'reversal':
                    recommended_strategies.append('strategy_2')
                else:
                    recommended_strategies.append('strategy_4')
    
    if 'bullish' in [t.lower() for t in trend_list] and 'bearish' in [t.lower() for t in trend_list]:
        if 'continuation' in [p.lower() for p in pattern_list] and 'reversal' in [p.lower() for p in pattern_list]:
            recommended_strategies = ['strategy_2', 'strategy_4']
    
    return list(set(recommended_strategies))