from typing import List


def extract_trade_volumes(trade_results: str) -> List[int]:
    """
    Extracts trade volume integers from a list of trade result dictionaries.

    Parameters
    ----------
    trade_results : list
        List of trade result dictionaries, each expected to contain a
        'volume' key with an integer (or numeric string) value.

    Returns
    -------
    list
        List of integers representing the trade volumes extracted from each
        trade result.

    Raises
    ------
    ValueError
        If any trade result dictionary does not contain a 'volume' key or
        the value cannot be converted to an int.
    TypeError
        If the input is not a list.

    Examples
    --------
    >>> raw_trade_results = [
    ...     {'volume': 100, 'price': 10.5},
    ...     {'volume': 200, 'price': 10.7},
    >>> ]
    >>> extract_trade_volumes(raw_trade_results)
    [100, 200]

    >>> raw_trade_results = [
    ...     {'volume': '300', 'price': 10.2},
    >>> ]
    >>> extract_trade_volumes(raw_trade_results)
    [300]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")