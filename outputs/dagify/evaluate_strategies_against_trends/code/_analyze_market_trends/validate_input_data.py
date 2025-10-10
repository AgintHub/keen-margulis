import ast


def validate_input_data(current_prices: str, historical_prices: str, trading_volumes: str) -> str:
    """
    Validates input market data including current prices, historical prices, and
    trading volumes.

    Parameters
    ----------
    current_prices : str
        Current prices of the assets in string format, expected to be
        convertible to a list of floats.
    historical_prices : str
        Historical price data for the assets over a specified period in
        string format, expected to be convertible to a list of floats.
    trading_volumes : str
        Trading volumes for the assets in string format, expected to be
        convertible to a list of floats.

    Returns
    -------
    str
        A string indicating whether the input data is valid ('valid') or not
        ('invalid').

    Raises
    ------
    ValueError
        Raised when the input strings cannot be converted to the expected
        numerical formats or are out of expected ranges.
    TypeError
        Raised when the input parameters are not strings.

    Examples
    --------
    >>> validate_input_data(current_prices='[1.0, 2.0, 3.0]',
    historical_prices='[4.0, 5.0, 6.0]', trading_volumes='[7.0, 8.0, 9.0]')
    'valid'

    >>> validate_input_data(current_prices='invalid', historical_prices='[4.0,
    5.0, 6.0]', trading_volumes='[7.0, 8.0, 9.0]')
    'invalid'

    """
    
    try:
        if not isinstance(current_prices, str):
            raise TypeError("current_prices must be a string")
        if not isinstance(historical_prices, str):
            raise TypeError("historical_prices must be a string")
        if not isinstance(trading_volumes, str):
            raise TypeError("trading_volumes must be a string")
        
        try:
            current_prices_list = ast.literal_eval(current_prices)
            historical_prices_list = ast.literal_eval(historical_prices)
            trading_volumes_list = ast.literal_eval(trading_volumes)
        except (ValueError, SyntaxError):
            return 'invalid'
        
        if not isinstance(current_prices_list, list):
            return 'invalid'
        if not isinstance(historical_prices_list, list):
            return 'invalid'
        if not isinstance(trading_volumes_list, list):
            return 'invalid'
        
        for price in current_prices_list:
            if not isinstance(price, (int, float)):
                return 'invalid'
            if price < 0:
                raise ValueError("Current prices must be non-negative")
        
        for price in historical_prices_list:
            if not isinstance(price, (int, float)):
                return 'invalid'
            if price < 0:
                raise ValueError("Historical prices must be non-negative")
        
        for volume in trading_volumes_list:
            if not isinstance(volume, (int, float)):
                return 'invalid'
            if volume < 0:
                raise ValueError("Trading volumes must be non-negative")
        
        return 'valid'
    
    except (TypeError, ValueError):
        raise