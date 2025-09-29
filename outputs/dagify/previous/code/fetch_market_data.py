from ._fetch_market_data.establish_market_data_connection import establish_market_data_connection
from ._fetch_market_data.retrieve_raw_market_data import retrieve_raw_market_data
from ._fetch_market_data.validate_market_data_integrity import validate_market_data_integrity
from ._fetch_market_data.extract_market_prices import extract_market_prices
from ._fetch_market_data.extract_market_volumes import extract_market_volumes
from ._fetch_market_data.close_market_data_connection import close_market_data_connection

from pydantic import BaseModel, Field
from typing import List


class FetchMarketDataOutput(BaseModel):
    """Pydantic model for fetch_market_data node outputs."""
    market_prices: List[float] = (
        Field(..., description="List of current market prices.")
    )
    market_volumes: List[int] = (
        Field(..., description="List of current market volumes.")
    )


def fetch_market_data(general_input: str, **kwargs) -> FetchMarketDataOutput:
    """
    Fetches current market data including prices and volumes.

    Returns
    -------
    Tuple[List[float], List[int]]
        A tuple containing a list of current market prices as floats and a
        list of current market volumes as integers.

    Raises
    ------
    ConnectionError
        If there's a failure in connecting to the market data source.
    DataError
        If the retrieved data is malformed or incomplete.

    Examples
    --------
    >>> fetch_market_data()
    ([12.5, 15.2, 10.8], [100, 200, 50])

    >>> prices, volumes = fetch_market_data()
    prices: [12.5, 15.2, 10.8]
    volumes: [100, 200, 50]

    """
    connection = establish_market_data_connection()
    raw_data: dict = retrieve_raw_market_data(connection=connection)
    validated_data: dict = validate_market_data_integrity(data=raw_data)
    prices: List[float] = extract_market_prices(data=validated_data)
    volumes: List[int] = extract_market_volumes(data=validated_data)
    close_market_data_connection(connection=connection)
    return FetchMarketDataOutput(market_prices=prices, market_volumes=volumes)