from ._collect_account_data.establish_data_connection import establish_data_connection
from ._collect_account_data.fetch_account_data import fetch_account_data
from ._collect_account_data.extract_account_balance import extract_account_balance
from ._collect_account_data.extract_positions import extract_positions
from ._collect_account_data.format_positions_as_string import format_positions_as_string
from ._collect_account_data.close_data_connection import close_data_connection

from pydantic import BaseModel, Field


class CollectAccountDataOutput(BaseModel):
    """Pydantic model for collect_account_data node outputs."""
    account_balance: float = Field(..., description="Current account balance")
    positions: str = Field(..., description="List of current positions")


def collect_account_data(general_input: str, **kwargs) -> CollectAccountDataOutput:
    """
    Collects and returns account data including balance and positions.

    Returns
    -------
    Dict[str, Union[float, List[str]]]
        A dictionary containing the account balance as a float and positions
        as a list of strings.

    Raises
    ------
    ConnectionError
        If there's an issue connecting to the data source.
    DataRetrievalError
        If there's an error retrieving account data.

    Examples
    --------
    >>> account_data = collect_account_data()
    {'account_balance': 10000.0, 'positions': ['AAPL', 'GOOG']}

    >>> account_data = collect_account_data()
    >>> print(account_data['account_balance'])
    >>> print(account_data['positions'])
    10000.0
    ['AAPL', 'GOOG']

    """
    connection = establish_data_connection()
    raw_account_data = fetch_account_data(connection=connection)
    account_balance: float = extract_account_balance(data=raw_account_data)
    positions_list = extract_positions(data=raw_account_data)
    positions_string: str = format_positions_as_string(positions=positions_list)
    close_data_connection(connection=connection)
    return CollectAccountDataOutput(
        account_balance=account_balance,
        positions=positions_string,
    )