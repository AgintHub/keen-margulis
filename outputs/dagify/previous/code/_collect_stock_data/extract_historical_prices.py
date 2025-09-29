from typing import List


def extract_historical_prices(data: str) -> List[float]:
    """
    Extracts historical stock prices from raw market data provided as input.

    Parameters
    ----------
    data : str
        Raw market data containing historical stock information, expected to
        be in a format that can be processed to extract historical prices.

    Returns
    -------
    List[float]
        A list of historical stock prices extracted from the raw market
        data. The prices are expected to be in chronological order
        corresponding to the stock symbols analyzed.

    Raises
    ------
    ValueError
        If the input raw market data is malformed or does not contain the
        expected historical price information.
    TypeError
        If the input data type is not a string or if the data cannot be
        processed into a list of float values.

    Examples
    --------
    >>> raw_market_data = '{ "stock1": { "prices": [10.5, 11.2, 10.8] },
    "stock2": { "prices": [20.1, 19.9, 20.3] } }'
    >>> historical_prices = extract_historical_prices(data=raw_market_data)
    [10.5, 11.2, 10.8, 20.1, 19.9, 20.3]

    >>> raw_market_data = '{ "stock1": { "prices": [15.0, 15.5] } }'
    >>> historical_prices = extract_historical_prices(data=raw_market_data)
    [15.0, 15.5]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")