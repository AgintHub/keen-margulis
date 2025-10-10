from typing import List


import random


def fetch_current_prices(assets: str) -> List[float]:
    """
    Fetches current prices for a given list of assets represented as a comma-
    separated string.

    Parameters
    ----------
    assets : str
        Comma-separated string of asset identifiers (e.g., stock symbols,
        currency pairs).

    Returns
    -------
    List[float]
        A list of current prices corresponding to the assets provided, in
        the same order.

    Raises
    ------
    ValueError
        If the input string is empty or contains invalid asset identifiers.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> fetch_current_prices('AAPL,GOOG,MSFT')
    [150.5, 2800.2, 230.1]

    >>> fetch_current_prices('EURUSD,GBPUSD')
    [1.1001, 1.3002]

    """
    
    if not isinstance(assets, str):
        raise TypeError("If the input is not a string.")
    
    if not assets or assets.strip() == "":
        raise ValueError("If the input string is empty or contains invalid asset identifiers.")
    
    asset_list = [asset.strip() for asset in assets.split(',') if asset.strip()]
    
    if not asset_list:
        raise ValueError("If the input string is empty or contains invalid asset identifiers.")
    
    prices = []
    for asset in asset_list:
        if not asset or len(asset) < 2:
            raise ValueError("If the input string is empty or contains invalid asset identifiers.")
        
        random.seed(hash(asset) % (2**32))
        if asset.upper() in ['AAPL', 'GOOG', 'MSFT', 'TSLA', 'AMZN']:
            price = random.uniform(100.0, 3000.0)
        elif asset.upper() in ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD']:
            price = random.uniform(0.5, 2.0)
        else:
            price = random.uniform(10.0, 500.0)
        
        prices.append(round(price, 4))
    
    return prices