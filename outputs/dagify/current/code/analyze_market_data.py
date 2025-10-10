from ._analyze_market_data.validate_input_data import validate_input_data
from ._analyze_market_data.identify_market_trends import identify_market_trends
from ._analyze_market_data.recognize_trading_patterns import recognize_trading_patterns
from ._analyze_market_data.detect_market_anomalies import detect_market_anomalies
from ._analyze_market_data.validate_analysis_results import validate_analysis_results

from pydantic import BaseModel, Field
from typing import List


class CollectMarketDataOutput(BaseModel):
    """Pydantic model for collect_market_data node outputs."""
    stock_prices: List[float] = Field(..., description="List of stock prices")
    trading_volumes: List[int] = (
        Field(..., description="List of trading volumes")
    )
    economic_indicators: List[float] = (
        Field(..., description="List of economic indicators")
    )
    data_collection_status: bool = (
        Field(..., description="Whether data collection was successful")
    )


class AnalyzeMarketDataOutput(BaseModel):
    """Pydantic model for analyze_market_data node outputs."""
    trend_identification: List[str] = (
        Field(..., description="List of identified trends")
    )
    pattern_recognition: List[str] = (
        Field(..., description="List of recognized patterns")
    )
    anomaly_detection: List[str] = (
        Field(..., description="List of detected anomalies")
    )
    analysis_status: bool = (
        Field(..., description="Whether data analysis was successful")
    )


def analyze_market_data(collect_market_data_input: CollectMarketDataOutput, **kwargs) -> AnalyzeMarketDataOutput:
    """
    Analyzes market data to identify trends, patterns, and anomalies.

    Parameters
    ----------
    stock_prices : List[float]
        List of stock prices collected from various sources.
    trading_volumes : List[int]
        List of trading volumes collected from various sources.
    economic_indicators : List[float]
        List of economic indicators collected from various sources.
    data_collection_status : bool
        Whether data collection was successful.

    Returns
    -------
    Tuple[List[str], List[str], List[str], bool]
        A tuple containing the list of identified trends, recognized
        patterns, detected anomalies, and a boolean indicating whether the
        analysis was successful.

    Raises
    ------
    ValueError
        If the input data is inconsistent or missing.
    RuntimeError
        If an error occurs during the analysis process.

    Examples
    --------
    >>> stock_prices = [100.0, 120.0, 110.0]
    >>> trading_volumes = [1000, 1200, 1100]
    >>> economic_indicators = [2.0, 2.1, 2.2]
    >>> data_collection_status = True
    >>> analyze_market_data(stock_prices, trading_volumes, economic_indicators,
    data_collection_status)
    (['uptrend'], ['increasing_volume'], ['price_spike'], True)

    """
    if not collect_market_data_input.data_collection_status:
        return AnalyzeMarketDataOutput(
            trend_identification=[],
            pattern_recognition=[],
            anomaly_detection=[],
            analysis_status=False
        )
    
    validated_data: bool = validate_input_data(
        stock_prices=collect_market_data_input.stock_prices,
        trading_volumes=collect_market_data_input.trading_volumes,
        economic_indicators=collect_market_data_input.economic_indicators
    )
    
    if not validated_data:
        raise ValueError("Input data is inconsistent or missing")
    
    try:
        identified_trends: List[str] = identify_market_trends(
            prices=collect_market_data_input.stock_prices,
            volumes=collect_market_data_input.trading_volumes
        )
        
        recognized_patterns: List[str] = recognize_trading_patterns(
            prices=collect_market_data_input.stock_prices,
            volumes=collect_market_data_input.trading_volumes,
            economic_data=collect_market_data_input.economic_indicators
        )
        
        detected_anomalies: List[str] = detect_market_anomalies(
            prices=collect_market_data_input.stock_prices,
            volumes=collect_market_data_input.trading_volumes,
            economic_indicators=collect_market_data_input.economic_indicators
        )
        
        analysis_success: bool = validate_analysis_results(
            trends=identified_trends,
            patterns=recognized_patterns,
            anomalies=detected_anomalies
        )
        
        return AnalyzeMarketDataOutput(
            trend_identification=identified_trends,
            pattern_recognition=recognized_patterns,
            anomaly_detection=detected_anomalies,
            analysis_status=analysis_success
        )
        
    except Exception as e:
        raise RuntimeError(f"Error occurred during analysis process: {str(e)}")