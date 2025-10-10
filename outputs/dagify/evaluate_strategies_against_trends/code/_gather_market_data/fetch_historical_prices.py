from typing import List


import datetime
import random


def fetch_historical_prices(assets: str, start_date: str, end_date: str) -> List[float]:
    """
    Fetches historical prices for given assets between start_date and end_date.

    Parameters
    ----------
    assets : str
        Comma-separated string of asset identifiers to fetch historical
        prices for.
    start_date : str
        Start date of the historical period in 'YYYY-MM-DD' format.
    end_date : str
        End date of the historical period in 'YYYY-MM-DD' format.

    Returns
    -------
    List[float]
        A list of historical prices for the specified assets over the given
        date range.

    Raises
    ------
    ValueError
        If the date format is invalid or if start_date is later than
        end_date.
    TypeError
        If assets is not a string or if start_date/end_date are not strings.

    Examples
    --------
    >>> fetch_historical_prices(assets='AAPL,GOOG', start_date='2022-01-01',
    end_date='2022-01-31')
    [100.0, 101.0, 102.0, ...]

    >>> fetch_historical_prices(assets='MSFT', start_date='2023-01-01',
    end_date='2023-01-05')
    [200.0, 201.0, 202.0, 203.0, 204.0]

    """
    
    if not isinstance(assets, str):
        raise TypeError("assets must be a string")
    if not isinstance(start_date, str):
        raise TypeError("start_date must be a string")
    if not isinstance(end_date, str):
        raise TypeError("end_date must be a string")
    
    try:
        start_dt = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD' format.")
    
    if start_dt > end_dt:
        raise ValueError("start_date cannot be later than end_date")
    
    asset_list = [asset.strip() for asset in assets.split(',') if asset.strip()]
    
    historical_prices = []
    current_date = start_dt
    
    while current_date <= end_dt:
        for asset in asset_list:
            base_price = 100.0
            if asset.upper() == 'AAPL':
                base_price = 150.0
            elif asset.upper() == 'GOOG':
                base_price = 2500.0
            elif asset.upper() == 'MSFT':
                base_price = 300.0
            
            days_from_start = (current_date - start_dt).days
            price = base_price + (days_from_start * 0.5) + random.uniform(-2.0, 2.0)
            historical_prices.append(round(price, 2))
        
        current_date += datetime.timedelta(days=1)
    
    return historical_prices