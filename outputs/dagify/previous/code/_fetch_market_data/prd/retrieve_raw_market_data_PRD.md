# retrieve_raw_market_data PRD

## Description
Retrieves raw market data from a given connection.


## Conceptual Info

This shim function serves as an interface to retrieve raw market data from an established connection. It plays a crucial role in the data processing pipeline by providing the initial raw data that will be further processed and validated.

## Docstring

### Summary
Retrieves raw market data from the given connection and returns it as a string representation of a dictionary.

### Parameters

- **connection** (str): The established market data connection used to retrieve raw data.

### Returns

str: A string representation of the raw market data dictionary.

### Raises

- ConnectionError: If the connection to the market data source fails.
- TypeError: If the connection parameter is not a string.

### Examples

```python
>>> connection = 'market_data_connection'
>>> raw_data = retrieve_raw_market_data(connection=connection)
{'market_prices': [10.5, 20.3], 'market_volumes': [100, 200]}
```

```python
>>> invalid_connection = 123
>>> try:
...     retrieve_raw_market_data(connection=invalid_connection)
>>> except TypeError as e:
...     print(e)
Connection parameter must be a string.
```
