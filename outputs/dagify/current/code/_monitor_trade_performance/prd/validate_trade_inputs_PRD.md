# validate_trade_inputs PRD

## Description
Validates trade inputs to ensure they meet the required format and criteria for further processing.


## Conceptual Info

This shim node is responsible for validating trade inputs to ensure they are correctly formatted and meet the necessary criteria before being processed further in the system.

## Docstring

### Summary
Validates trade inputs based on their results and status.

### Parameters

- **trade_results** (str): A string containing the results of the executed trades, expected to be in a specific format.
- **trade_status** (str): A string containing the status of the executed trades, indicating success or failure.

### Returns

str: A string indicating the outcome of the validation process.

### Raises

- ValueError: Raised when the trade results or status are not in the expected format or contain invalid data.
- TypeError: Raised when the input types are not as expected (e.g., not strings).

### Examples

```python
>>> validate_trade_inputs(trade_results='success,100,buy', trade_status='success')
>>> print(output)
'Validation successful'
```

```python
>>> validate_trade_inputs(trade_results='failure,0,sell', trade_status='failure')
>>> print(output)
'Validation successful'
```
