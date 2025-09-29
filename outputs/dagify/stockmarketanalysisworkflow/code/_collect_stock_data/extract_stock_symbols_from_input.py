from typing import List


def extract_stock_symbols_from_input(input_text: str) -> List[str]:
    """
    Extracts stock symbols from the input text and returns them as a list of
    strings.

    Parameters
    ----------
    input_text : str
        The input text from which stock symbols will be extracted.

    Returns
    -------
    List[str]
        A list of stock symbols extracted from the input text.

    Raises
    ------
    ValueError
        If the input text is empty or does not contain valid stock symbols.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> stock_symbols = extract_stock_symbols_from_input(input_text='AAPL, GOOG,
    MSFT')
    >>> print(stock_symbols)
    ['AAPL', 'GOOG', 'MSFT']

    >>> stock_symbols = extract_stock_symbols_from_input(input_text='Invalid
    input')
    >>> print(stock_symbols)
    []

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")