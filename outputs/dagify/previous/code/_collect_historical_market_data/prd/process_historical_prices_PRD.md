# process_historical_prices PRD

## Description
Processes historical price data into a list of floats.


## Conceptual Info

This shim processes historical price data that has been validated and cleaned, transforming it into a standardized list of float values for further analysis or processing.

## Docstring

### Summary
Processes validated historical price data into a list of float values.

### Parameters

- **data** (str): Input validated historical price data in a string representation, expected to be a list of dictionaries or similar structure that can be parsed into float values.

### Returns

List[float]: A list of historical prices processed into float format.

### Raises

- ValueError: If the input data cannot be parsed into float values.
- TypeError: If the input type is not as expected (e.g., not a string representation of a list of dictionaries).

### Examples

```python
>>> process_historical_prices(data='[{"price": 10.5}, {"price": 11.2}]')
[10.5, 11.2]
```

```python
>>> process_historical_prices(data='[{"price": "12.1"}, {"price": "13.4"}]')
[12.1, 13.4]
```
