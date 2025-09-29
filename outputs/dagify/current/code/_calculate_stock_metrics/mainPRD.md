# _calculate_stock_metrics - Complete PRD Documentation

## Overview
PRDs for nodes in the '_calculate_stock_metrics' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [calculate_moving_averages](#calculate_moving_averages)

- [calculate_rsi](#calculate_rsi)

- [calculate_volatility](#calculate_volatility)



---

## validate_input_data

### Description
Validates the preprocessed stock data and normalized volumes for further analysis.

### Conceptual Info

This shim function is responsible for validating the preprocessed stock data and normalized volumes, ensuring they are suitable for further financial analysis.

### Docstring

**Summary:** Validates preprocessed stock data and normalized trading volumes.

**Parameters:**

- cleaned_data (str): Preprocessed stock price data in a string format, expected to be convertible to a list of floats.
- volumes (str): Normalized trading volumes in a string format, expected to be convertible to a list of floats.
**Returns:** str - A string indicating the validation result, such as 'valid' or 'invalid'.

**Raises:**

- ValueError: Raised when the input data cannot be converted to the expected numerical format.
- TypeError: Raised when the input types are not as expected.
**Examples:**

```python
>>> validate_input_data(cleaned_data='[1.0, 2.0, 3.0]', volumes='[10, 20, 30]')
'valid'
```

```python
>>> validate_input_data(cleaned_data='invalid_data', volumes='[10, 20, 30]')
'invalid'
```



---

## calculate_moving_averages

### Description
This shim node calculates moving averages from the provided stock price data.

### Conceptual Info

This shim is responsible for calculating moving averages from the given stock price data, which is a critical component in stock market analysis.

### Docstring

**Summary:** Calculates moving averages from the provided stock price data.

**Parameters:**

- price_data (str): Input stock price data as a string, expected to contain comma-separated or JSON-formatted float values representing historical stock prices.
**Returns:** List[float] - A list of moving averages calculated from the input stock price data. The length and values of the list depend on the specific moving average algorithm implemented.

**Raises:**

- ValueError: When the input string is not properly formatted or contains non-numeric data.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> price_data = '1.0, 2.0, 3.0, 4.0, 5.0'
>>> moving_averages = calculate_moving_averages(price_data)
>>> print(moving_averages)
[1.0, 1.5, 2.0, 2.5, 3.0]
```

```python
>>> price_data = '[1.0, 2.0, 3.0, 4.0, 5.0]'
>>> moving_averages = calculate_moving_averages(price_data)
>>> print(moving_averages)
[1.0, 1.5, 2.0, 2.5, 3.0]
```



---

## calculate_rsi

### Description
Calculates Relative Strength Index (RSI) values based on given price data and trading volumes.

### Conceptual Info

This shim node is responsible for calculating the Relative Strength Index (RSI), a technical indicator used to measure the magnitude of recent price changes in order to determine overbought or oversold conditions.

### Docstring

**Summary:** Calculates RSI values based on the provided price data and trading volumes.

**Parameters:**

- price_data (str): Serialized list of float values representing stock prices.
- volumes (str): Serialized list of float values representing trading volumes.
**Returns:** List[float] - List of RSI values corresponding to the input price data.

**Raises:**

- ValueError: If the input price data or volumes are not valid serialized lists of floats.
- TypeError: If the input types are not strings or if deserialization fails.
**Examples:**

```python
>>> import json
>>> price_data = json.dumps([12.5, 13.2, 12.8, 13.5, 14.1])
>>> volumes = json.dumps([1000, 1200, 1100, 1300, 1400])
>>> rsi_values = calculate_rsi(price_data=price_data, volumes=volumes)
[0.45, 0.52, 0.48, 0.55, 0.60]
```

```python
>>> import json
>>> price_data = json.dumps([25.1, 24.8, 25.3, 24.9, 25.5])
>>> volumes = json.dumps([2000, 2100, 2200, 2300, 2400])
>>> rsi_values = calculate_rsi(price_data=price_data, volumes=volumes)
[0.58, 0.55, 0.60, 0.57, 0.62]
```



---

## calculate_volatility

### Description
Calculates the volatility of stock prices based on the provided price data.

### Conceptual Info

This shim node is responsible for calculating the volatility of stock prices, which is a crucial metric in financial analysis. It takes stock price data as input and returns a measure of volatility.

### Docstring

**Summary:** Calculates the volatility of stock prices based on the input price data.

**Parameters:**

- price_data (str): A string representing the stock price data used for calculating volatility.
**Returns:** float - The calculated volatility of the stock prices represented as a float value.

**Raises:**

- ValueError: When the input price data is invalid or cannot be processed.
- TypeError: When the input price data is not of the expected type.
**Examples:**

```python
>>> price_data = '[1.0, 2.0, 3.0, 4.0, 5.0]'
>>> volatility = calculate_volatility(price_data=price_data)
>>> print(volatility)
1.5811388300000002
```

```python
>>> price_data = '[5.0, 5.0, 5.0, 5.0, 5.0]'
>>> volatility = calculate_volatility(price_data=price_data)
>>> print(volatility)
0.0
```

