# _collect_account_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_collect_account_data' module.

## Table of Contents

- [establish_data_connection](#establish_data_connection)

- [fetch_account_data](#fetch_account_data)

- [extract_account_balance](#extract_account_balance)

- [extract_positions](#extract_positions)

- [format_positions_as_string](#format_positions_as_string)

- [close_data_connection](#close_data_connection)



---

## establish_data_connection

### Description
Establishes a data connection required for fetching account data.

### Conceptual Info

This shim is responsible for establishing a connection to a data source, which is necessary for retrieving account data.

### Docstring

**Summary:** Establishes a connection to a data source and returns the connection object or identifier.

**Returns:** str - A string representation of the established data connection.

**Raises:**

- ConnectionError: If the connection to the data source cannot be established.
**Examples:**

```python
>>> connection = establish_data_connection()
'data_connection_object'
```



---

## fetch_account_data

### Description
Fetches raw account data from a data connection.

### Conceptual Info

This shim function represents the capability to fetch raw account data from a data source, serving as a crucial step in the account data collection process.

### Docstring

**Summary:** Fetches raw account data using the provided connection.

**Parameters:**

- connection (str): The established data connection used to fetch account data.
**Returns:** str - The raw account data fetched from the connection, represented as a string.

**Raises:**

- ValueError: If the connection is invalid or cannot be used to fetch data.
- TypeError: If the connection parameter is not of the expected type.
**Examples:**

```python
>>> raw_data = fetch_account_data(connection='active_trading_account')
'{ "account_balance": 1000.0, "positions": [{"symbol": "AAPL", "quantity": 10}]}'
```

```python
>>> raw_data = fetch_account_data(connection='invalid_connection')
ValueError: Invalid connection provided.
```



---

## extract_account_balance

### Description
Extracts the account balance from the provided raw account data.

### Conceptual Info

This shim is responsible for extracting the account balance from raw account data fetched from a data connection. It plays a crucial role in the account data collection process.

### Docstring

**Summary:** Extracts the account balance from raw account data.

**Parameters:**

- data (str): The raw account data containing the account balance information.
**Returns:** float - The extracted account balance.

**Raises:**

- ValueError: If the raw data is malformed or missing required balance information.
- TypeError: If the input data is not of type str.
**Examples:**

```python
>>> raw_data = '{"account_balance": 1234.56, "other_info": "some data"}'
>>> balance = extract_account_balance(data=raw_data)
1234.56
```

```python
>>> raw_data = '{\"account_balance\": 7890.12, \"other_info\": \"some other data\"}'
>>> balance = extract_account_balance(data=raw_data)
7890.12
```



---

## extract_positions

### Description
Extracts and processes position data from raw account information.

### Conceptual Info

This shim function is responsible for extracting position data from raw account information and returning it in a processed format.

### Docstring

**Summary:** Extracts position data from raw account data and returns it as a string.

**Parameters:**

- data (str): Raw account data containing position information.
**Returns:** str - Processed positions data as a string, potentially representing a list or other structured data.

**Raises:**

- ValueError: If the input raw account data is malformed or missing required information.
- TypeError: If the input data type is not a string.
**Examples:**

```python
>>> raw_data = '{"positions": [{"symbol": "AAPL", "quantity": 100}, {"symbol": "GOOG", "quantity": 50}]}'
>>> processed_positions = extract_positions(data=raw_data)
'AAPL: 100, GOOG: 50'
```

```python
>>> raw_data = '{"positions": [{"symbol": "MSFT", "quantity": 200}]}'
>>> processed_positions = extract_positions(data=raw_data)
'MSFT: 200'
```



---

## format_positions_as_string

### Description
Converts a list of positions into a string representation.

### Conceptual Info

This shim function is responsible for converting a list of positions into a string format that can be used in the CollectAccountDataOutput model.

### Docstring

**Summary:** Formats a list of positions into a string representation.

**Parameters:**

- positions (str): A string representation of a list of positions.
**Returns:** str - A string representation of the input positions list.

**Raises:**

- ValueError: If the input string is not a valid representation of a list.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> positions_list = "['AAPL', 'GOOG', 'MSFT']"
>>> formatted_positions = format_positions_as_string(positions=positions_list)
>>> print(formatted_positions)
'AAPL, GOOG, MSFT'
```

```python
>>> positions_list = "['AMZN']"
>>> formatted_positions = format_positions_as_string(positions=positions_list)
>>> print(formatted_positions)
'AMZN'
```



---

## close_data_connection

### Description
Closes an established data connection to release system resources.

### Conceptual Info

The close_data_connection shim is responsible for terminating an active data connection, ensuring that system resources are properly released and made available for other tasks.

### Docstring

**Summary:** Closes an established data connection and returns the status of the operation.

**Parameters:**

- connection (str): A string representing the established data connection to be closed.
**Returns:** str - A string indicating the result or status of closing the data connection, such as 'success' or an error message.

**Raises:**

- ValueError: If the input 'connection' is not a valid or recognized connection string.
- TypeError: If the 'connection' parameter is not of type string.
**Examples:**

```python
>>> close_data_connection(connection='active_connection_string')
'success'
```

```python
>>> close_data_connection(connection='invalid_connection')
'error: invalid connection'
```

