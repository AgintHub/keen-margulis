from ._process_stock_data.validate_input_data import validate_input_data
from ._process_stock_data.clean_stock_price_data import clean_stock_price_data
from ._process_stock_data.normalize_trading_volumes import normalize_trading_volumes

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


class ProcessStockDataOutput(BaseModel):
    """Pydantic model for process_stock_data node outputs."""
    cleaned_stock_data: List[float] = (
        Field(..., description="Preprocessed stock price data")
    )
    normalized_volumes: List[float] = (
        Field(..., description="Normalized trading volumes")
    )


def process_stock_data(collect_stock_data_input: CollectStockDataOutput, **kwargs) -> ProcessStockDataOutput:
    """
    Preprocesses stock data by cleaning and normalizing it for analysis.

    Parameters
    ----------
    historical_prices : List[float]
        Historical stock prices collected from reliable sources.
    trading_volumes : List[int]
        Trading volumes for each stock symbol collected from reliable
        sources.

    Returns
    -------
    Tuple[List[float], List[float]]
        A tuple containing the cleaned stock price data and normalized
        trading volumes.

    Raises
    ------
    ValueError
        If historical_prices or trading_volumes are empty or not of the
        correct type.

    Examples
    --------
    >>> historical_prices = [100.0, 101.0, 102.0, 103.0]
    >>> trading_volumes = [1000, 1200, 1100, 1300]
    >>> cleaned_stock_data, normalized_volumes =
    process_stock_data(historical_prices, trading_volumes)
    ([100.0, 101.0, 102.0, 103.0], [0.0, 0.6666666666666666, 0.3333333333333333,
    1.0])

    """
    validate_input_data(historical_prices=collect_stock_data_input.historical_prices, trading_volumes=collect_stock_data_input.trading_volumes)
    
    cleaned_prices: List[float] = clean_stock_price_data(historical_prices=collect_stock_data_input.historical_prices)
    
    normalized_volumes: List[float] = normalize_trading_volumes(trading_volumes=collect_stock_data_input.trading_volumes)
    
    return ProcessStockDataOutput(
        cleaned_stock_data=cleaned_prices,
        normalized_volumes=normalized_volumes
    )