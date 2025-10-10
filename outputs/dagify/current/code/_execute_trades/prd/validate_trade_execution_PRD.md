# validate_trade_execution PRD

## Description
Validates trade execution outcomes and volumes against predefined business rules to ensure correctness before returning processed results.


## Conceptual Info

This shim checks that each trade outcome is valid and that each corresponding volume is a positive integer, raising informative errors if any rule is violated. It centralises validation logic so that the rest of the execution pipeline can rely on clean, correctly formatted data.

## Docstring

### Summary
Validates trade execution outcomes and volumes against predefined business rules.

### Parameters

- **outcomes** (List[str]): A list of trade outcomes, each must be one of 'SUCCESS', 'REJECTED', or 'PARTIAL'.
- **volumes** (List[int]): A list of corresponding trade volumes, each must be a positive integer.

### Returns

str: A string indicating the result of the validation, typically "Validation Successful".

### Raises

- ValueError: Raised when an outcome is invalid, a volume is non‑positive, or any trade is rejected.
- TypeError: Raised when inputs are not lists of the expected types.

### Examples

```python
>>> from validate_trade_execution import validate_trade_execution
>>> # Successful validation
>>> result = validate_trade_execution(outcomes=['SUCCESS', 'PARTIAL'], volumes=[100, 200])
>>> print(result)
"Validation Successful"
```

```python
>>> # Validation failure due to rejected trade
>>> try:
...     validate_trade_execution(outcomes=['SUCCESS', 'REJECTED'], volumes=[150, 300])
>>> except ValueError as e:
...     print(e)
"Trade rejected: indices [1]"
```
