# fetch_account_data PRD

## Description
Fetches raw account data from a data connection.


## Conceptual Info

This shim function represents the capability to fetch raw account data from a data source, serving as a crucial step in the account data collection process.

## Docstring

### Summary
Fetches raw account data using the provided connection.

### Parameters

- **connection** (str): The established data connection used to fetch account data.

### Returns

str: The raw account data fetched from the connection, represented as a string.

### Raises

- ValueError: If the connection is invalid or cannot be used to fetch data.
- TypeError: If the connection parameter is not of the expected type.

### Examples

```python
>>> raw_data = fetch_account_data(connection='active_trading_account')
'{ "account_balance": 1000.0, "positions": [{"symbol": "AAPL", "quantity": 10}]}'
```

```python
>>> raw_data = fetch_account_data(connection='invalid_connection')
ValueError: Invalid connection provided.
```
