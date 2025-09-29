# calculate_moving_averages PRD

## Description
This shim node calculates moving averages from the provided stock price data.


## Conceptual Info

This shim is responsible for calculating moving averages from the given stock price data, which is a critical component in stock market analysis.

## Docstring

### Summary
Calculates moving averages from the provided stock price data.

### Parameters

- **price_data** (str): Input stock price data as a string, expected to contain comma-separated or JSON-formatted float values representing historical stock prices.

### Returns

List[float]: A list of moving averages calculated from the input stock price data. The length and values of the list depend on the specific moving average algorithm implemented.

### Raises

- ValueError: When the input string is not properly formatted or contains non-numeric data.
- TypeError: When the input is not a string.

### Examples

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
