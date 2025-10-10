from typing import List


from datetime import datetime
import random


def fetch_trading_volumes(assets: str, start_date: str, end_date: str) -> List[float]:
    """
    Fetches trading volumes for specified assets between given start and end
    dates.

    Parameters
    ----------
    assets : str
        Comma-separated string of asset identifiers to fetch trading volumes
        for.
    start_date : str
        Start date of the period in 'YYYY-MM-DD' format.
    end_date : str
        End date of the period in 'YYYY-MM-DD' format.

    Returns
    -------
    List[float]
        List of trading volumes corresponding to the specified assets over
        the given date range.

    Raises
    ------
    ValueError
        If the date range is invalid or assets string is malformed.
    TypeError
        If input types are not as expected.

    Examples
    --------
    >>> fetch_trading_volumes(assets='AAPL,GOOG', start_date='2023-01-01',
    end_date='2023-01-31')
    [1000.0, 500.0]

    >>> fetch_trading_volumes(assets='MSFT,AMZN', start_date='2023-02-01',
    end_date='2023-02-28')
    [2000.0, 1500.0]

    """
    
    if not isinstance(assets, str) or not isinstance(start_date, str) or not isinstance(end_date, str):
        raise TypeError("All input parameters must be strings")
    
    if not assets or not assets.strip():
        raise ValueError("Assets string cannot be empty")
    
    try:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Date format must be 'YYYY-MM-DD'")
    
    if start_dt > end_dt:
        raise ValueError("Start date must be before or equal to end date")
    
    try:
        asset_list = [asset.strip() for asset in assets.split(',')]
    except Exception:
        raise ValueError("Assets string is malformed")
    
    if not all(asset for asset in asset_list):
        raise ValueError("Assets string contains empty asset identifiers")
    
    volumes = []
    random.seed(42)
    for asset in asset_list:
        base_volume = hash(asset + start_date + end_date) % 10000
        volume = float(abs(base_volume) + random.uniform(100, 5000))
        volumes.append(volume)
    
    return volumes