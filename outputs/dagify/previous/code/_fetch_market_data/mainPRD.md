# _fetch_market_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_fetch_market_data' module.

## Table of Contents

- [establish_market_data_connection](#establish_market_data_connection)

- [retrieve_raw_market_data](#retrieve_raw_market_data)

- [validate_market_data_integrity](#validate_market_data_integrity)

- [extract_market_prices](#extract_market_prices)

- [extract_market_volumes](#extract_market_volumes)

- [close_market_data_connection](#close_market_data_connection)



---

## establish_market_data_connection

### Description
Establishes a connection to retrieve market data.

### Conceptual Info

This shim is responsible for creating a connection to a market data source, which is then used to fetch raw market data.

### Docstring

**Summary:** Establishes a connection to a market data source and returns a connection object.

**Returns:** str - A connection object that can be used to retrieve market data.

**Raises:**

- ConnectionError: If the connection to the market data source cannot be established.
**Examples:**

```python
>>> connection = establish_market_data_connection()
<market_data_connection_object>
```



---

## retrieve_raw_market_data

### Description
Retrieves raw market data from a given connection.

### Conceptual Info

This shim function serves as an interface to retrieve raw market data from an established connection. It plays a crucial role in the data processing pipeline by providing the initial raw data that will be further processed and validated.

### Docstring

**Summary:** Retrieves raw market data from the given connection and returns it as a string representation of a dictionary.

**Parameters:**

- connection (str): The established market data connection used to retrieve raw data.
**Returns:** str - A string representation of the raw market data dictionary.

**Raises:**

- ConnectionError: If the connection to the market data source fails.
- TypeError: If the connection parameter is not a string.
**Examples:**

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



---

## validate_market_data_integrity

### Description
Validates the integrity of the provided market data to ensure it is correct and consistent.

### Conceptual Info

This shim is responsible for validating the integrity of market data retrieved from an external source, ensuring that it is accurate and consistent before further processing.

### Docstring

**Summary:** Validates the integrity of the given market data dictionary.

**Parameters:**

- data (str): The raw market data to be validated, expected to be a string representation of a dictionary.
**Returns:** str - A string representation of the validated market data dictionary.

**Raises:**

- ValueError: If the input data is not a valid dictionary or contains inconsistent information.
- TypeError: If the input data is not of type string or cannot be parsed into a dictionary.
**Examples:**

```python
>>> validate_market_data_integrity(data='{"market_prices": [10.5, 20.3], "market_volumes": [100, 200]}')
'{"market_prices": [10.5, 20.3], "market_volumes": [100, 200]}'
```

```python
>>> validate_market_data_integrity(data='invalid_data')
ValueError: Invalid market data format.
```



---

## extract_market_prices

### Description
Extracts a list of market prices from the provided validated market data.

### Conceptual Info

This shim extracts market prices from validated market data, playing a crucial role in the market data processing pipeline.

### Docstring

**Summary:** Extracts market prices from the provided validated market data string.

**Parameters:**

- data (str): Validated market data containing prices to be extracted.
**Returns:** List[float] - List of extracted market prices.

**Raises:**

- ValueError: If the input data is malformed or does not contain valid market prices.
- TypeError: If the input data is not of type string.
**Examples:**

```python
>>> extract_market_prices(data='{"prices": [10.5, 20.3, 30.7]}')
[10.5, 20.3, 30.7]
```

```python
>>> extract_market_prices(data='{}')
[]
```



---

## extract_market_volumes

### Description
Extracts market volumes from validated market data.

### Conceptual Info

This shim node is responsible for extracting market volumes from validated market data, playing a crucial role in providing the necessary data for further processing in the market data pipeline.

### Docstring

**Summary:** Extracts market volumes from the provided validated market data string.

**Parameters:**

- data (str): Validated market data in string format, expected to contain volume information.
**Returns:** List[int] - A list of integers representing the current market volumes extracted from the input data.

**Raises:**

- ValueError: When the input data is malformed or does not contain valid volume information.
- TypeError: When the input data is not of type string.
**Examples:**

```python
>>> extract_market_volumes(data='{"market_volumes": [100, 200, 300]}')
[100, 200, 300]
```

```python
>>> extract_market_volumes(data='invalid_data')
ValueError: Invalid data format
```



---

## close_market_data_connection

### Description
Closes the established market data connection to free up resources.

### Conceptual Info

This shim is responsible for closing an established market data connection, ensuring that system resources are properly released after use.

### Docstring

**Summary:** Closes a market data connection and returns a status message.

**Parameters:**

- connection (str): The identifier or object representing the market data connection to be closed.
**Returns:** str - A message indicating the result of closing the connection, such as 'Connection closed successfully' or an error message.

**Raises:**

- ValueError: If the provided connection is invalid or not found.
- ConnectionError: If there's an issue closing the connection.
**Examples:**

```python
>>> close_market_data_connection(connection='market_data_conn_123')
'Connection closed successfully'
```

```python
>>> close_market_data_connection(connection='invalid_conn')
'Error: Invalid connection ID'
```

