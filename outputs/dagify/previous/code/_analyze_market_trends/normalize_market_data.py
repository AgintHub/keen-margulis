import json


def normalize_market_data(current_prices: str, historical_prices: str, trading_volumes: str) -> str:
    """
    Normalizes market data inputs into a standardized dictionary format.

    Parameters
    ----------
    current_prices : str
        A string representation of a list of current prices of assets.
    historical_prices : str
        A string representation of a list of historical prices of assets.
    trading_volumes : str
        A string representation of a list of trading volumes of assets.

    Returns
    -------
    str
        A string representation of a dictionary containing the normalized
        market data.

    Raises
    ------
    ValueError
        If the input strings cannot be parsed into lists of floats.
    TypeError
        If the input parameters are not strings.

    Examples
    --------
    >>> normalize_market_data('[100.0, 200.0]', '[50.0, 150.0, 250.0]',
    '[1000.0, 2000.0]')
    '{"current_prices": [100.0, 200.0], "historical_prices": [50.0, 150.0,
    250.0], "trading_volumes": [1000.0, 2000.0]}'

    >>> normalize_market_data('[150.0, 250.0]', '[75.0, 175.0, 275.0]',
    '[1500.0, 2500.0]')
    '{"current_prices": [150.0, 250.0], "historical_prices": [75.0, 175.0,
    275.0], "trading_volumes": [1500.0, 2500.0]}'

    """
    
    if not isinstance(current_prices, str):
        raise TypeError("current_prices must be a string")
    if not isinstance(historical_prices, str):
        raise TypeError("historical_prices must be a string")
    if not isinstance(trading_volumes, str):
        raise TypeError("trading_volumes must be a string")
    
    try:
        current_prices_list = json.loads(current_prices)
        historical_prices_list = json.loads(historical_prices)
        trading_volumes_list = json.loads(trading_volumes)
    except json.JSONDecodeError as e:
        raise ValueError("Input strings cannot be parsed into lists") from e
    
    if not isinstance(current_prices_list, list):
        raise ValueError("current_prices must represent a list")
    if not isinstance(historical_prices_list, list):
        raise ValueError("historical_prices must represent a list")
    if not isinstance(trading_volumes_list, list):
        raise ValueError("trading_volumes must represent a list")
    
    try:
        current_prices_floats = [float(x) for x in current_prices_list]
        historical_prices_floats = [float(x) for x in historical_prices_list]
        trading_volumes_floats = [float(x) for x in trading_volumes_list]
    except (ValueError, TypeError) as e:
        raise ValueError("Input lists must contain values that can be converted to floats") from e
    
    normalized_data = {
        "current_prices": current_prices_floats,
        "historical_prices": historical_prices_floats,
        "trading_volumes": trading_volumes_floats
    }
    
    return json.dumps(normalized_data)