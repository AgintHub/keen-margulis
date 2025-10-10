# validate_strategy_inputs PRD

## Description
Validates a trading strategy name and confidence level before trade execution.


## Conceptual Info

The shim ensures that the strategy and confidence inputs are valid before proceeding with trade execution, preventing runtime errors in downstream trading logic.

## Docstring

### Summary
Validates trading strategy and confidence level, raising errors on invalid inputs and returning a confirmation string.

### Parameters

- **strategy** (str): The name of the trading strategy to be validated.
- **confidence** (str): String representation of the confidence level associated with the strategy.

### Returns

str: A message confirming that the strategy and confidence level are valid.

### Raises

- TypeError: If strategy or confidence is not a string.
- ValueError: If strategy is not one of the accepted strategies or if confidence is not a numeric string between 0 and 1.

### Examples

```python
>>> validate_strategy_inputs(strategy='scalping', confidence='0.85')
'Strategy scalping with confidence 0.85 validated.'
```

```python
>>> validate_strategy_inputs(strategy='mean_reversion', confidence='1.2')
ValueError: Confidence must be a numeric string between 0 and 1.
```
