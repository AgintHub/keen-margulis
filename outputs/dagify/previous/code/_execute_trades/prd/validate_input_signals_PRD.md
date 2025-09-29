# validate_input_signals PRD

## Description
Validates input trading signals and their confidence levels to ensure they are within acceptable parameters.


## Conceptual Info

This shim node is responsible for validating the input trading signals and their confidence levels before they are processed further in the trading execution pipeline.

## Docstring

### Summary
Validates input trading signals and their confidence levels.

### Parameters

- **signals** (List[str]): List of trading signals (buy/sell/hold) to be validated.
- **confidence** (List[float]): List of confidence levels corresponding to the trading signals.

### Returns

str: Output indicating whether the input signals are valid.

### Raises

- ValueError: When the input signals or confidence levels are invalid or out of range.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> signals = ['buy', 'sell', 'hold']
>>> confidence = [0.8, 0.7, 0.9]
>>> validate_input_signals(signals=signals, confidence=confidence)
'Input signals are valid.'
```

```python
>>> signals = ['invalid_signal', 'sell', 'hold']
>>> confidence = [0.8, 0.7, 0.9]
>>> validate_input_signals(signals=signals, confidence=confidence)
'Invalid signal: invalid_signal.'
```
