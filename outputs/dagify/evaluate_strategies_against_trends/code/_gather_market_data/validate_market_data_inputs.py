from datetime import datetime


def validate_market_data_inputs(assets: str, start_date: str, end_date: str) -> str:
    """
    Validates market data inputs including assets, start date, and end date.

    Parameters
    ----------
    assets : str
        Comma-separated list of asset symbols to validate.
    start_date : str
        Start date in 'YYYY-MM-DD' format for market data retrieval.
    end_date : str
        End date in 'YYYY-MM-DD' format for market data retrieval.

    Returns
    -------
    str
        A success message if all inputs are valid.

    Raises
    ------
    ValueError
        If the date format is incorrect or if the start date is after the
        end date.
    TypeError
        If the input types are not as expected.

    Examples
    --------
    >>> validate_market_data_inputs(assets='AAPL,GOOG', start_date='2022-01-01',
    end_date='2022-12-31')
    'Inputs are valid.'

    >>> validate_market_data_inputs(assets='AAPL,GOOG', start_date='2022-13-01',
    end_date='2022-12-31')
    ValueError: Invalid date format.

    """
    
    if not isinstance(assets, str):
        raise TypeError("Assets must be a string")
    if not isinstance(start_date, str):
        raise TypeError("Start date must be a string")
    if not isinstance(end_date, str):
        raise TypeError("End date must be a string")
    
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format.")
    
    try:
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format.")
    
    if start_dt > end_dt:
        raise ValueError("Start date cannot be after end date")
    
    return "Inputs are valid."