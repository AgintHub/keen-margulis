# validate_trading_signals PRD

## Description
Validates trading signals based on input signals and status.


## Conceptual Info

This shim node is responsible for validating trading signals based on the input signals and their generation status. It plays a crucial role in ensuring that only valid trading signals are processed further in the trading execution pipeline.

## Docstring

### Summary
Validates trading signals based on input signals and status, returning a list of validated signals.

### Parameters

- **signals** (str): Input trading signals to be validated, expected to be a string representation that can be processed.
- **status** (str): Status of the signal generation, indicating whether the signal generation was successful.

### Returns

List[str]: A list of validated trading signals.

### Raises

- ValueError: When the input signals are malformed or cannot be processed.
- TypeError: When the input types are incorrect, such as signals or status not being strings.

### Examples

```python
>>> validate_trading_signals(signals='signal1,signal2', status='success')
['signal1', 'signal2']
```

```python
>>> validate_trading_signals(signals='invalid_signal', status='failure')
[]
```
