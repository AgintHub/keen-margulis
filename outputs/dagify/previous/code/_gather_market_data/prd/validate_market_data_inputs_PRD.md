# validate_market_data_inputs PRD

## Description
Validates the inputs for market data retrieval, checking assets, start date, and end date for correctness.


## Conceptual Info

This node validates the inputs required for fetching market data, ensuring that the assets, start date, and end date are correctly formatted and valid.

## Docstring

### Summary
Validates market data inputs including assets, start date, and end date.

### Parameters

- **assets** (str): Comma-separated list of asset symbols to validate.
- **start_date** (str): Start date in 'YYYY-MM-DD' format for market data retrieval.
- **end_date** (str): End date in 'YYYY-MM-DD' format for market data retrieval.

### Returns

str: A success message if all inputs are valid.

### Raises

- ValueError: If the date format is incorrect or if the start date is after the end date.
- TypeError: If the input types are not as expected.

### Examples

```python
>>> validate_market_data_inputs(assets='AAPL,GOOG', start_date='2022-01-01', end_date='2022-12-31')
'Inputs are valid.'
```

```python
>>> validate_market_data_inputs(assets='AAPL,GOOG', start_date='2022-13-01', end_date='2022-12-31')
ValueError: Invalid date format.
```
