from ._calculate_stock_metrics.validate_input_data import validate_input_data
from ._calculate_stock_metrics.calculate_moving_averages import calculate_moving_averages
from ._calculate_stock_metrics.calculate_rsi import calculate_rsi
from ._calculate_stock_metrics.calculate_volatility import calculate_volatility

from pydantic import BaseModel, Field
from typing import List


class ProcessStockDataOutput(BaseModel):
    """Pydantic model for process_stock_data node outputs."""
    cleaned_stock_data: List[float] = (
        Field(..., description="Preprocessed stock price data")
    )
    normalized_volumes: List[float] = (
        Field(..., description="Normalized trading volumes")
    )


class CalculateStockMetricsOutput(BaseModel):
    """Pydantic model for calculate_stock_metrics node outputs."""
    moving_averages: List[float] = (
        Field(..., description="Moving averages for the stock prices.")
    )
    rsi_values: List[float] = (
        Field(..., description="Relative Strength Index values.")
    )
    volatility: float = (
        Field(..., description="Stock price volatility measure.")
    )


def calculate_stock_metrics(process_stock_data_input: ProcessStockDataOutput, **kwargs) -> CalculateStockMetricsOutput:
    """
    Calculates moving averages, Relative Strength Index (RSI), and volatility
    from preprocessed stock data.

    Parameters
    ----------
    cleaned_stock_data : List[float]
        Preprocessed stock price data from the 'process_stock_data' node.
    normalized_volumes : List[float]
        Normalized trading volumes from the 'process_stock_data' node.

    Returns
    -------
    Tuple[List[float], List[float], float]
        A tuple containing moving averages, RSI values, and volatility
        measure.

    Raises
    ------
    ValueError
        If cleaned_stock_data or normalized_volumes are empty or malformed.

    Examples
    --------
    >>> cleaned_data = [100.0, 101.0, 102.0, 103.0, 104.0]
    >>> normalized_volumes = [0.5, 0.6, 0.7, 0.8, 0.9]
    >>> moving_averages, rsi_values, volatility =
    calculate_stock_metrics(cleaned_data, normalized_volumes)
    ([101.0, 102.0], [0.2, 0.3], 0.015)

    >>> cleaned_data = [50.0, 51.0, 52.0, 53.0, 54.0]
    >>> normalized_volumes = [0.1, 0.2, 0.3, 0.4, 0.5]
    >>> moving_averages, rsi_values, volatility =
    calculate_stock_metrics(cleaned_data, normalized_volumes)
    ([51.0, 52.0], [0.1, 0.2], 0.020)

    """
    validate_input_data(cleaned_data=process_stock_data_input.cleaned_stock_data, volumes=process_stock_data_input.normalized_volumes)
    
    moving_averages: List[float] = calculate_moving_averages(price_data=process_stock_data_input.cleaned_stock_data)
    
    rsi_values: List[float] = calculate_rsi(price_data=process_stock_data_input.cleaned_stock_data, volumes=process_stock_data_input.normalized_volumes)
    
    volatility: float = calculate_volatility(price_data=process_stock_data_input.cleaned_stock_data)
    
    return CalculateStockMetricsOutput(
        moving_averages=moving_averages,
        rsi_values=rsi_values,
        volatility=volatility
    )