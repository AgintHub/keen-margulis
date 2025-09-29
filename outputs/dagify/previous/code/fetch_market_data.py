from ._fetch_market_data.get_market_data_sources import get_market_data_sources
from ._fetch_market_data.fetch_data_from_sources import fetch_data_from_sources
from ._fetch_market_data.parse_market_data import parse_market_data
from ._fetch_market_data.extract_prices import extract_prices
from ._fetch_market_data.extract_volumes import extract_volumes
from ._fetch_market_data.validate_market_data import validate_market_data

from pydantic import BaseModel, Field
from typing import List


class FetchMarketDataOutput(BaseModel):
    """Pydantic model for fetch_market_data node outputs."""
    market_prices: List[float] = (
        Field(..., description="List of current market prices")
    )
    market_volumes: List[int] = (
        Field(..., description="List of current market volumes")
    )


def fetch_market_data(general_input: str, **kwargs) -> FetchMarketDataOutput:
    """
    Fetches current market data, including prices and volumes, from multiple
    sources.

    Returns
    -------
    Tuple[List[float], List[int]]
        A tuple containing a list of current market prices and a list of
        current market volumes.

    Raises
    ------
    ConnectionError
        If there's a failure connecting to market data sources.
    DataParsingError
        If there's an issue parsing the received market data.

    Examples
    --------
    >>> market_data = fetch_market_data()
    ([123.45, 67.89], [1000, 2000])

    >>> prices, volumes = fetch_market_data()
    >>> print(f'Prices: {prices}')
    >>> print(f'Volumes: {volumes}')
    Prices: [123.45, 67.89]
    Volumes: [1000, 2000]

    """
    source_urls: List[str] = get_market_data_sources()
    raw_data: List[dict] = fetch_data_from_sources(sources=source_urls)
    parsed_data: dict = parse_market_data(raw_data=raw_data)
    prices: List[float] = extract_prices(parsed_data=parsed_data)
    volumes: List[int] = extract_volumes(parsed_data=parsed_data)
    validate_market_data(prices=prices, volumes=volumes)
    return FetchMarketDataOutput(
        market_prices=prices,
        market_volumes=volumes,
    )