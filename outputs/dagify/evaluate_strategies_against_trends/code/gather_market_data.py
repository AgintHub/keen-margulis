from ._gather_market_data.parse_market_data_params import parse_market_data_params
from ._gather_market_data.validate_market_data_inputs import validate_market_data_inputs
from ._gather_market_data.fetch_current_prices import fetch_current_prices
from ._gather_market_data.fetch_historical_prices import fetch_historical_prices
from ._gather_market_data.fetch_trading_volumes import fetch_trading_volumes

from ._gather_market_data.parse_market_data_params import parse_market_data_params
from ._gather_market_data.validate_market_data_inputs import validate_market_data_inputs
from ._gather_market_data.fetch_current_prices import fetch_current_prices
from ._gather_market_data.fetch_historical_prices import fetch_historical_prices
from ._gather_market_data.fetch_trading_volumes import fetch_trading_volumes

from pydantic import BaseModel, Field
from typing import List


class GatherMarketDataOutput(BaseModel):
    """Pydantic model for gather_market_data node outputs."""
    current_prices: List[float] = (
        Field(..., description="Current prices of the assets")
    )
    historical_prices: List[float] = (
        Field(..., description = (
            "Historical price data for the assets over a specified period")
        )
    )
    trading_volumes: List[float] = (
        Field(..., description="Trading volumes for the assets")
    )


def gather_market_data(general_input: str, **kwargs) -> GatherMarketDataOutput:
    """
    Gathers current and historical market data for the specified assets or
    instruments, returning current prices, historical prices, and trading
    volumes.

    Parameters
    ----------
    assets : List[str]
        List of asset symbols or identifiers to gather data for.
    start_date : str
        Start date for historical data in 'YYYY-MM-DD' format.
    end_date : str
        End date for historical data in 'YYYY-MM-DD' format.

    Returns
    -------
    Tuple[List[float], List[float], List[float]]
        A tuple containing three lists: current prices, historical prices,
        and trading volumes for the specified assets.

    Raises
    ------
    ValueError
        If the assets list is empty or if the start_date is later than
        end_date.
    ConnectionError
        If there's a failure in connecting to the data source.

    Examples
    --------
    >>> assets = ['AAPL', 'GOOG']
    >>> start_date = '2022-01-01'
    >>> end_date = '2022-12-31'
    >>> result = gather_market_data(assets, start_date, end_date)
    ([150.0, 2800.0], [120.0, 130.0, ...], [1000.0, 2000.0])

    >>> assets = ['MSFT']
    >>> start_date = '2023-01-01'
    >>> end_date = '2023-01-31'
    >>> result = gather_market_data(assets, start_date, end_date)
    ([250.0], [240.0, 245.0, ...], [500.0])

    """
    parsed_params: dict = parse_market_data_params(input_string=general_input, kwargs=kwargs)
    assets: List[str] = parsed_params['assets']
    start_date: str = parsed_params['start_date']
    end_date: str = parsed_params['end_date']
    
    validate_market_data_inputs(assets=assets, start_date=start_date, end_date=end_date)
    
    current_prices: List[float] = fetch_current_prices(assets=assets)
    historical_prices: List[float] = fetch_historical_prices(assets=assets, start_date=start_date, end_date=end_date)
    trading_volumes: List[float] = fetch_trading_volumes(assets=assets, start_date=start_date, end_date=end_date)
    
    return GatherMarketDataOutput(
        current_prices=current_prices,
        historical_prices=historical_prices,
        trading_volumes=trading_volumes
    )