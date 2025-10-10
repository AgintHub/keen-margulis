from typing import List


import re


def parse_trade_profits(trade_results: str) -> List[float]:
    """
    Parses a string of trade results and returns a list of profit values as
    floats.

    Parameters
    ----------
    trade_results : str
        A string containing the results of executed trades, potentially
        including profit information.

    Returns
    -------
    List[float]
        A list of floating-point numbers representing the profit values
        extracted from the trade results.

    Raises
    ------
    ValueError
        If the input string is malformed or does not contain valid profit
        information.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>>
    parse_trade_profits(trade_results='Trade1:Profit=100.5,Trade2:Profit=200.8')
    [100.5, 200.8]

    >>> parse_trade_profits(trade_results='Profit:150.2;Loss:50.1')
    [150.2]

    """
    
    if not isinstance(trade_results, str):
        raise TypeError("Input must be a string")
    
    if not trade_results.strip():
        raise ValueError("Input string is empty or malformed")
    
    profit_pattern = r'[Pp]rofit[=:]([0-9]+(?:\.[0-9]+)?)'
    matches = re.findall(profit_pattern, trade_results)
    
    if not matches:
        raise ValueError("No valid profit information found in the input string")
    
    try:
        profits = [float(match) for match in matches]
    except ValueError as e:
        raise ValueError("Invalid profit values found in the input string") from e
    
    return profits