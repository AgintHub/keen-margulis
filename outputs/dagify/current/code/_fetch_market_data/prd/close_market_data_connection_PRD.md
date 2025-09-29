# close_market_data_connection PRD

## Description
Closes the established market data connection to free up resources.


## Conceptual Info

This shim is responsible for closing an established market data connection, ensuring that system resources are properly released after use.

## Docstring

### Summary
Closes a market data connection and returns a status message.

### Parameters

- **connection** (str): The identifier or object representing the market data connection to be closed.

### Returns

str: A message indicating the result of closing the connection, such as 'Connection closed successfully' or an error message.

### Raises

- ValueError: If the provided connection is invalid or not found.
- ConnectionError: If there's an issue closing the connection.

### Examples

```python
>>> close_market_data_connection(connection='market_data_conn_123')
'Connection closed successfully'
```

```python
>>> close_market_data_connection(connection='invalid_conn')
'Error: Invalid connection ID'
```
