from ._collect_stock_data.extract_stock_symbols_from_input import extract_stock_symbols_from_input
from ._collect_stock_data.validate_stock_symbols import validate_stock_symbols
from ._collect_stock_data.establish_data_source_connection import establish_data_source_connection
from ._collect_stock_data.handle_connection_error import handle_connection_error
from ._collect_stock_data.fetch_historical_data import fetch_historical_data
from ._collect_stock_data.extract_historical_prices import extract_historical_prices
from ._collect_stock_data.extract_trading_volumes import extract_trading_volumes

from pydantic import BaseModel, Field
from typing import List


class CollectStockDataOutput(BaseModel):
    """Pydantic model for collect_stock_data node outputs."""
    stock_symbols: List[str] = (
        Field(..., description="List of stock symbols analyzed")
    )
    historical_prices: List[float] = (
        Field(..., description="Historical stock prices for each symbol")
    )
    trading_volumes: List[int] = (
        Field(..., description="Trading volumes for each stock symbol")
    )


def collect_stock_data(general_input: str, **kwargs) -> CollectStockDataOutput:
    """
    Collects historical stock prices and trading volumes for given stock
    symbols.

    Parameters
    ----------
    stock_symbols : List[str]
        List of stock symbols to gather data for.

    Returns
    -------
    Tuple[List[str], List[float], List[int]]
        A tuple containing the list of stock symbols, their historical
        prices, and trading volumes.

    Raises
    ------
    ValueError
        If the input stock symbols list is empty or contains invalid
        symbols.
    ConnectionError
        If there's a failure connecting to the data source.

    Examples
    --------
    >>> stock_data = collect_stock_data(['AAPL', 'GOOG'])
    >>> print(stock_data)
    (['AAPL', 'GOOG'], [150.5, 2800.2], [100000, 50000])

    >>> stock_symbols = ['MSFT', 'AMZN']
    >>> data = collect_stock_data(stock_symbols)
    >>> print(data)
    (['MSFT', 'AMZN'], [220.1, 3200.5], [80000, 70000])

    """
    stock_symbols_list: List[str] = extract_stock_symbols_from_input(input_text=general_input)
    validate_stock_symbols(symbols=stock_symbols_list)
    connection_status: bool = establish_data_source_connection()
    if not connection_status:
        handle_connection_error()
    raw_market_data: dict = fetch_historical_data(symbols=stock_symbols_list)
    historical_prices: List[float] = extract_historical_prices(data=raw_market_data)
    trading_volumes: List[int] = extract_trading_volumes(data=raw_market_data)
    return CollectStockDataOutput(
        stock_symbols=stock_symbols_list,
        historical_prices=historical_prices,
        trading_volumes=trading_volumes
    )