# validate_input_lengths PRD

## Description
Validates that the lengths of input lists are consistent.


## Conceptual Info

This shim validates the consistency of input list lengths for trading signals and their corresponding confidence levels.

## Docstring

### Summary
Validates that the input lists 'signals' and 'confidence' have the same length.

### Parameters

- **signals** (List[str]): List of trading signals.
- **confidence** (List[float]): List of confidence levels corresponding to the trading signals.

### Returns

str: Output indicating whether the input lengths are valid.

### Raises

- ValueError: When the lengths of 'signals' and 'confidence' are not equal.

### Examples

```python
>>> signals = ['buy', 'sell', 'hold']
>>> confidence = [0.8, 0.7, 0.9]
>>> validate_input_lengths(signals=signals, confidence=confidence)
'Input lengths are valid'
```

```python
>>> signals = ['buy', 'sell']
>>> confidence = [0.8, 0.7, 0.9]
>>> validate_input_lengths(signals=signals, confidence=confidence)
ValueError: 'Lengths of signals and confidence do not match'
```
