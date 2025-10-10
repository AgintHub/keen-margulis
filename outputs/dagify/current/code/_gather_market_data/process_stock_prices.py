from typing import List


def process_stock_prices(data: str) -> List[float]:
    """
    Converts raw stock price data into a list of floats.

    Parameters
    ----------
    data : str
        Raw stock price data, either as a comma‑separated string or a JSON
        array string.

    Returns
    -------
    LIST_FLOAT
        A list of float values representing the processed stock prices.

    Raises
    ------
    ValueError
        Raised when the input string cannot be parsed into valid float
        values.
    TypeError
        Raised when the input is not of type str.

    Examples
    --------
    >>> prices = process_stock_prices('100.5, 101.2, 102')
    [100.5, 101.2, 102.0]

    >>> try:
    ...     process_stock_prices('abc, 200')
    >>> except ValueError as e:
    ...     print(e)
    "Invalid stock price data: cannot convert to float"

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")