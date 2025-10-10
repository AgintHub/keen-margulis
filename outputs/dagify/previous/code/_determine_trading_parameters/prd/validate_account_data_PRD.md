# validate_account_data PRD

## Description
Validates the account data including balance and positions.


## Conceptual Info

This shim function is responsible for validating account data, specifically the account balance and positions, to ensure they are in an expected format and range.

## Docstring

### Summary
Validates account data by checking the account balance and positions.

### Parameters

- **account_balance** (str): The account balance to be validated.
- **positions** (str): The current positions to be validated.

### Returns

str: A string indicating whether the account data is valid.

### Raises

- ValueError: If the account balance or positions are not in the expected format.
- TypeError: If the input types are not strings.

### Examples

```python
>>> validate_account_data(account_balance='1000.0', positions='["AAPL", "GOOG"]')
>>> print(output)
'Account data is valid.'
```

```python
>>> validate_account_data(account_balance='invalid', positions='["AAPL", "GOOG"]')
ValueError: Invalid account balance format.
```
