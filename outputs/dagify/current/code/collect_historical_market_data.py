from ._collect_historical_market_data.identify_market_data_sources import identify_market_data_sources
from ._collect_historical_market_data.fetch_price_data_from_sources import fetch_price_data_from_sources
from ._collect_historical_market_data.fetch_volume_data_from_sources import fetch_volume_data_from_sources
from ._collect_historical_market_data.fetch_additional_metrics_from_sources import fetch_additional_metrics_from_sources
from ._collect_historical_market_data.validate_and_clean_price_data import validate_and_clean_price_data
from ._collect_historical_market_data.validate_and_clean_volume_data import validate_and_clean_volume_data
from ._collect_historical_market_data.validate_and_clean_metrics_data import validate_and_clean_metrics_data
from ._collect_historical_market_data.process_historical_prices import process_historical_prices
from ._collect_historical_market_data.process_historical_volumes import process_historical_volumes
from ._collect_historical_market_data.process_other_metrics import process_other_metrics

from pydantic import BaseModel, Field
from typing import List


class CollectHistoricalMarketDataOutput(BaseModel):
    """Pydantic model for collect_historical_market_data node outputs."""
    historical_prices: List[float] = (
        Field(..., description="List of historical prices")
    )
    historical_volumes: List[float] = (
        Field(..., description="List of historical volumes")
    )
    other_metrics: List[str] = (
        Field(..., description="Other relevant historical metrics")
    )


def collect_historical_market_data(general_input: str, **kwargs) -> CollectHistoricalMarketDataOutput:
    """
    Collects historical market data from multiple sources, returning prices,
    volumes, and other metrics.

    Returns
    -------
    Tuple[List[float], List[float], List[str]]
        A tuple containing historical prices, volumes, and other metrics.

    Raises
    ------
    ConnectionError
        If there's an issue connecting to the data sources.
    DataError
        If the retrieved data is malformed or incomplete.

    Examples
    --------
    >>> historical_data = collect_historical_market_data()
    ([100.0, 101.0, 102.0], [1000.0, 1100.0, 1200.0], ['metric1', 'metric2',
    'metric3'])

    """
    data_sources: List[str] = identify_market_data_sources(input_params=general_input, kwargs=kwargs)
    
    raw_price_data: List[dict] = fetch_price_data_from_sources(sources=data_sources)
    raw_volume_data: List[dict] = fetch_volume_data_from_sources(sources=data_sources)
    raw_metrics_data: List[dict] = fetch_additional_metrics_from_sources(sources=data_sources)
    
    validated_price_data: List[dict] = validate_and_clean_price_data(raw_data=raw_price_data)
    validated_volume_data: List[dict] = validate_and_clean_volume_data(raw_data=raw_volume_data)
    validated_metrics_data: List[dict] = validate_and_clean_metrics_data(raw_data=raw_metrics_data)
    
    processed_prices: List[float] = process_historical_prices(data=validated_price_data)
    processed_volumes: List[float] = process_historical_volumes(data=validated_volume_data)
    processed_metrics: List[str] = process_other_metrics(data=validated_metrics_data)
    
    return CollectHistoricalMarketDataOutput(
        historical_prices=processed_prices,
        historical_volumes=processed_volumes,
        other_metrics=processed_metrics
    )