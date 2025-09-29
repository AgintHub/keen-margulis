# validate_stock_symbols PRD

## Description
Validates a list of stock symbols to ensure they are correctly formatted and exist in the financial database.


## Conceptual Info

This shim node is responsible for validating a list of stock symbols against a financial database to ensure their correctness and existence.

## Docstring

### Summary
Validates a list of stock symbols and returns a success message if all are valid.

### Parameters

- **symbols** (str): A list of stock symbols to be validated, passed as a string representation of a list.

### Returns

str: A message indicating whether the validation was successful or not.

### Raises

- ValueError: If any of the stock symbols are invalid or do not exist in the database.
- TypeError: If the input is not a string representation of a list.

### Examples

```python
>>> validate_stock_symbols(symbols='["AAPL", "GOOGL"]')
'Validation successful'
```

```python
>>> validate_stock_symbols(symbols='["INVALID", "GOOGL"]')
'Validation failed: INVALID is not a valid stock symbol'
```
