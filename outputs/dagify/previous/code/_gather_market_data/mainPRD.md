# _gather_market_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_gather_market_data' module.

## Table of Contents

- [parse_market_data_params](#parse_market_data_params)

- [validate_market_data_inputs](#validate_market_data_inputs)

- [fetch_current_prices](#fetch_current_prices)

- [fetch_historical_prices](#fetch_historical_prices)

- [fetch_trading_volumes](#fetch_trading_volumes)



---

## parse_market_data_params

### Description
Parses input parameters for market data gathering into a structured dictionary.

### Conceptual Info

This shim function is responsible for parsing input parameters for market data gathering into a structured dictionary that can be used by subsequent functions.

### Docstring

**Summary:** Parses input string and keyword arguments into a dictionary of market data parameters.

**Parameters:**

- input_string (str): The input string containing market data parameters in a specific format.
- kwargs (str): Additional keyword arguments containing market data parameters.
**Returns:** str - A JSON string representing a dictionary with keys 'assets', 'start_date', and 'end_date'.

**Raises:**

- ValueError: If the input string or keyword arguments are invalid or missing required parameters.
- TypeError: If the input types are incorrect or cannot be parsed.
**Examples:**

```python
>>> parse_market_data_params(input_string='assets:AAPL,GOOG;start_date:2022-01-01;end_date:2022-12-31', kwargs='{}')
>>> parse_market_data_params(input_string='assets:MSFT;start_date:2023-01-01;end_date:2023-06-30', kwargs='{"assets": ["MSFT"]}')
>>> parse_market_data_params(input_string='', kwargs='{"assets": ["AAPL", "GOOG"], "start_date": "2022-01-01", "end_date": "2022-12-31"}')
{"assets": ["AAPL", "GOOG"], "start_date": "2022-01-01", "end_date": "2022-12-31"}
```



---

## validate_market_data_inputs

### Description
Validates the inputs for market data retrieval, checking assets, start date, and end date for correctness.

### Conceptual Info

This node validates the inputs required for fetching market data, ensuring that the assets, start date, and end date are correctly formatted and valid.

### Docstring

**Summary:** Validates market data inputs including assets, start date, and end date.

**Parameters:**

- assets (str): Comma-separated list of asset symbols to validate.
- start_date (str): Start date in 'YYYY-MM-DD' format for market data retrieval.
- end_date (str): End date in 'YYYY-MM-DD' format for market data retrieval.
**Returns:** str - A success message if all inputs are valid.

**Raises:**

- ValueError: If the date format is incorrect or if the start date is after the end date.
- TypeError: If the input types are not as expected.
**Examples:**

```python
>>> validate_market_data_inputs(assets='AAPL,GOOG', start_date='2022-01-01', end_date='2022-12-31')
'Inputs are valid.'
```

```python
>>> validate_market_data_inputs(assets='AAPL,GOOG', start_date='2022-13-01', end_date='2022-12-31')
ValueError: Invalid date format.
```



---

## fetch_current_prices

### Description
Fetches current prices for the given assets.

### Conceptual Info

This shim node is responsible for retrieving the current market prices of specified financial assets.

### Docstring

**Summary:** Fetches current prices for a given list of assets represented as a comma-separated string.

**Parameters:**

- assets (str): Comma-separated string of asset identifiers (e.g., stock symbols, currency pairs).
**Returns:** List[float] - A list of current prices corresponding to the assets provided, in the same order.

**Raises:**

- ValueError: If the input string is empty or contains invalid asset identifiers.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> fetch_current_prices('AAPL,GOOG,MSFT')
[150.5, 2800.2, 230.1]
```

```python
>>> fetch_current_prices('EURUSD,GBPUSD')
[1.1001, 1.3002]
```



---

## fetch_historical_prices

### Description
Fetches historical price data for specified assets over a given date range.

### Conceptual Info

This shim node is responsible for retrieving historical price data for a list of assets between specified start and end dates. It plays a crucial role in the gather_market_data function by providing the necessary historical price information.

### Docstring

**Summary:** Fetches historical prices for given assets between start_date and end_date.

**Parameters:**

- assets (str): Comma-separated string of asset identifiers to fetch historical prices for.
- start_date (str): Start date of the historical period in 'YYYY-MM-DD' format.
- end_date (str): End date of the historical period in 'YYYY-MM-DD' format.
**Returns:** List[float] - A list of historical prices for the specified assets over the given date range.

**Raises:**

- ValueError: If the date format is invalid or if start_date is later than end_date.
- TypeError: If assets is not a string or if start_date/end_date are not strings.
**Examples:**

```python
>>> fetch_historical_prices(assets='AAPL,GOOG', start_date='2022-01-01', end_date='2022-01-31')
[100.0, 101.0, 102.0, ...]
```

```python
>>> fetch_historical_prices(assets='MSFT', start_date='2023-01-01', end_date='2023-01-05')
[200.0, 201.0, 202.0, 203.0, 204.0]
```



---

## fetch_trading_volumes

### Description
Fetches trading volumes for specified assets over a given date range.

### Conceptual Info

This shim node is designed to retrieve trading volume data for a list of assets over a specified date range, playing a crucial role in market data gathering and analysis.

### Docstring

**Summary:** Fetches trading volumes for specified assets between given start and end dates.

**Parameters:**

- assets (str): Comma-separated string of asset identifiers to fetch trading volumes for.
- start_date (str): Start date of the period in 'YYYY-MM-DD' format.
- end_date (str): End date of the period in 'YYYY-MM-DD' format.
**Returns:** List[float] - List of trading volumes corresponding to the specified assets over the given date range.

**Raises:**

- ValueError: If the date range is invalid or assets string is malformed.
- TypeError: If input types are not as expected.
**Examples:**

```python
>>> fetch_trading_volumes(assets='AAPL,GOOG', start_date='2023-01-01', end_date='2023-01-31')
[1000.0, 500.0]
```

```python
>>> fetch_trading_volumes(assets='MSFT,AMZN', start_date='2023-02-01', end_date='2023-02-28')
[2000.0, 1500.0]
```

