import math
import json


def calculate_average_profit(profits: str) -> float:
    """
    Calculates the average profit from a list of trade profits.

    Parameters
    ----------
    profits : List[float]
        A list of trade profits.

    Returns
    -------
    float
        The average profit calculated from the input profits. Returns 0 if
        the input list is empty.

    Raises
    ------
    TypeError
        If the input is not a list or if the list contains non-numeric
        values.
    ValueError
        If the input list contains NaN or infinity values.

    Examples
    --------
    >>> profits = [100.0, 200.0, 300.0]
    >>> average_profit = calculate_average_profit(profits)
    >>> print(average_profit)
    200.0

    >>> profits = []
    >>> average_profit = calculate_average_profit(profits)
    >>> print(average_profit)
    0

    """
    
    try:
        profits_list = json.loads(profits)
    except (json.JSONDecodeError, TypeError):
        raise TypeError("If the input is not a list or if the list contains non-numeric values.")
    
    if not isinstance(profits_list, list):
        raise TypeError("If the input is not a list or if the list contains non-numeric values.")
    
    if len(profits_list) == 0:
        return 0.0
    
    for profit in profits_list:
        if not isinstance(profit, (int, float)):
            raise TypeError("If the input is not a list or if the list contains non-numeric values.")
        if math.isnan(profit) or math.isinf(profit):
            raise ValueError("If the input list contains NaN or infinity values.")
    
    return sum(profits_list) / len(profits_list)