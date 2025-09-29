# validate_trading_parameters PRD

## Description
Validates trading parameters to ensure they meet the required criteria for risk tolerance and position sizing.


## Conceptual Info

This shim node is responsible for validating trading parameters, specifically risk tolerance and position sizing, to ensure they are within acceptable ranges and properly formatted for further processing in the trading signal generation pipeline.

## Docstring

### Summary
Validates the risk tolerance and position sizing parameters to ensure they are appropriate for generating trading signals.

### Parameters

- **risk_tolerance** (str): The risk tolerance level as a string, expected to be convertible to a float between 0 and 1.
- **position_sizing** (str): The position sizing strategy as a string, expected to be convertible to a float representing a proportion of the account balance.

### Returns

str: A JSON string representing a dictionary with validated 'risk_tolerance' and 'position_sizing' parameters.

### Raises

- ValueError: If the risk tolerance or position sizing values are out of the expected range or cannot be converted to float.
- TypeError: If the input parameters are not strings or if the conversion to float fails.

### Examples

```python
>>> validate_trading_parameters(risk_tolerance='0.5', position_sizing='0.2')
{'risk_tolerance': '0.5', 'position_sizing': '0.2'}
```

```python
>>> validate_trading_parameters(risk_tolerance='1.5', position_sizing='0.2')
ValueError: Risk tolerance must be between 0 and 1
```
