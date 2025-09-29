from typing import List


def validate_market_data(prices: str, volumes: str) -> List[float]:
    """
    Validates market data by converting input string representations of prices
    and volumes into a list of float values.

    Parameters
    ----------
    prices : str
        String representation of market prices to be validated.
    volumes : str
        String representation of market volumes to be validated.

    Returns
    -------
    List[float]
        List of validated market data as float values.

    Raises
    ------
    ValueError
        If the input strings cannot be converted to float values.
    TypeError
        If the input types are not strings.

    Examples
    --------
    >>> validate_market_data(prices='1.2, 3.4, 5.6', volumes='10, 20, 30')
    >>> validate_market_data(prices='7.8, 9.0', volumes='40, 50')
    [1.2, 3.4, 5.6]

    >>> validate_market_data(prices='invalid, data', volumes='10, 20')
    ValueError: Invalid input data

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")