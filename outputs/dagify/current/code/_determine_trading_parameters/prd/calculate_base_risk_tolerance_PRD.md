# calculate_base_risk_tolerance PRD

## Description
Calculates the base risk tolerance level based on the account balance, returning a float value between 0 and 1.


## Conceptual Info

This shim calculates the base risk tolerance for trading decisions based on the account balance, serving as a foundational component in determining overall risk tolerance.

## Docstring

### Summary
Calculates the base risk tolerance level based on the account balance.

### Parameters

- **account_balance** (str): The current account balance as a string value.

### Returns

float: The calculated base risk tolerance level, a float between 0 and 1.

### Raises

- ValueError: If the account balance is not a valid number or is negative.
- TypeError: If the account balance is not provided as a string.

### Examples

```python
>>> calculate_base_risk_tolerance(account_balance='10000')
0.5
```

```python
>>> calculate_base_risk_tolerance(account_balance='5000')
0.3
```
