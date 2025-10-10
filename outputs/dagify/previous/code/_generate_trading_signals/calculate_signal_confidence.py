from typing import List


def calculate_signal_confidence(evaluations: str, strategies: str) -> List[float]:
    """
    Calculates confidence levels for trading signals based on strategy
    evaluations and recommendations.

    Parameters
    ----------
    evaluations : str
        A string containing evaluations of different trading strategies,
        expected to be in a format that can be parsed by the implementation.
    strategies : str
        A string containing recommended trading strategies, expected to be
        in a format that can be parsed by the implementation.

    Returns
    -------
    List[float]
        A list of floating-point numbers representing the confidence levels
        for the generated trading signals.

    Raises
    ------
    ValueError
        If the input strings are not in the expected format or contain
        invalid data.
    TypeError
        If the input parameters are not of the expected type.

    Examples
    --------
    >>> evaluations = 'strategy1:0.8;strategy2:0.9'
    >>> strategies = 'strategy1;strategy2'
    >>> confidence_levels = calculate_signal_confidence(evaluations, strategies)
    [0.8, 0.9]

    >>> evaluations = 'strategyA:0.7;strategyB:0.6'
    >>> strategies = 'strategyA;strategyB'
    >>> confidence_levels = calculate_signal_confidence(evaluations, strategies)
    [0.7, 0.6]

    """
    if not isinstance(evaluations, str):
        raise TypeError("evaluations parameter must be a string")
    if not isinstance(strategies, str):
        raise TypeError("strategies parameter must be a string")
    
    if not evaluations.strip() or not strategies.strip():
        raise ValueError("Input strings cannot be empty")
    
    try:
        eval_dict = {}
        for eval_pair in evaluations.split(';'):
            if ':' not in eval_pair:
                raise ValueError("Invalid evaluation format: missing ':' separator")
            strategy_name, confidence_str = eval_pair.split(':', 1)
            eval_dict[strategy_name.strip()] = float(confidence_str.strip())
        
        strategy_list = [s.strip() for s in strategies.split(';')]
        
        confidence_levels = []
        for strategy in strategy_list:
            if strategy not in eval_dict:
                raise ValueError(f"Strategy '{strategy}' not found in evaluations")
            confidence_levels.append(eval_dict[strategy])
        
        return confidence_levels
    
    except ValueError as e:
        if "could not convert string to float" in str(e):
            raise ValueError("Invalid confidence value: must be a valid float") from e
        raise
    except Exception as e:
        raise ValueError("Input strings are not in the expected format") from e