# filter_signals_by_confidence PRD

## Description
Filters trading signals based on their confidence levels.


## Conceptual Info

This shim node filters trading signals based on their associated confidence levels, playing a crucial role in refining trading decisions by eliminating signals that do not meet a certain confidence threshold.

## Docstring

### Summary
Filters trading signals based on their confidence levels.

### Parameters

- **signals** (str): A string representation of a list of trading signals.
- **confidence_levels** (str): A string representation of a list of confidence levels corresponding to the trading signals.

### Returns

List[str]: A list of trading signals that have been filtered based on their confidence levels.

### Raises

- ValueError: If the input signals or confidence levels are not valid or cannot be parsed.
- TypeError: If the input types are not as expected.

### Examples

```python
>>> signals = '["signal1", "signal2", "signal3"]'
>>> confidence_levels = '[0.8, 0.4, 0.9]'
>>> filtered_signals = filter_signals_by_confidence(signals=signals, confidence_levels=confidence_levels)
["signal1", "signal3"]
```

```python
>>> signals = '["buy", "sell", "hold"]'
>>> confidence_levels = '[0.7, 0.3, 0.6]'
>>> filtered_signals = filter_signals_by_confidence(signals=signals, confidence_levels=confidence_levels)
["buy"]
```
