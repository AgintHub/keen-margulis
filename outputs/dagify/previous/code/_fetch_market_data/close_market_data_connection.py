def close_market_data_connection(connection: str) -> str:
    """
    Closes a market data connection and returns a status message.

    Parameters
    ----------
    connection : str
        The identifier or object representing the market data connection to
        be closed.

    Returns
    -------
    str
        A message indicating the result of closing the connection, such as
        'Connection closed successfully' or an error message.

    Raises
    ------
    ValueError
        If the provided connection is invalid or not found.
    ConnectionError
        If there's an issue closing the connection.

    Examples
    --------
    >>> close_market_data_connection(connection='market_data_conn_123')
    'Connection closed successfully'

    >>> close_market_data_connection(connection='invalid_conn')
    'Error: Invalid connection ID'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")