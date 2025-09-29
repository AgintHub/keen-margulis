def fetch_account_data(connection: str) -> str:
    """
    Fetches raw account data using the provided connection.

    Parameters
    ----------
    connection : str
        The established data connection used to fetch account data.

    Returns
    -------
    str
        The raw account data fetched from the connection, represented as a
        string.

    Raises
    ------
    ValueError
        If the connection is invalid or cannot be used to fetch data.
    TypeError
        If the connection parameter is not of the expected type.

    Examples
    --------
    >>> raw_data = fetch_account_data(connection='active_trading_account')
    '{ "account_balance": 1000.0, "positions": [{"symbol": "AAPL", "quantity":
    10}]}'

    >>> raw_data = fetch_account_data(connection='invalid_connection')
    ValueError: Invalid connection provided.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")