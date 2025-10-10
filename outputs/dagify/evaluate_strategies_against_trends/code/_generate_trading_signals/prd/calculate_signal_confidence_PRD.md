# calculate_signal_confidence PRD

## Description
Calculates confidence levels for generated trading signals based on strategy evaluations and recommendations.


## Conceptual Info

This shim node is responsible for determining the confidence levels of trading signals generated based on the evaluations of different trading strategies and the recommended strategies.

## Docstring

### Summary
Calculates confidence levels for trading signals based on strategy evaluations and recommendations.

### Parameters

- **evaluations** (str): A string containing evaluations of different trading strategies, expected to be in a format that can be parsed by the implementation.
- **strategies** (str): A string containing recommended trading strategies, expected to be in a format that can be parsed by the implementation.

### Returns

List[float]: A list of floating-point numbers representing the confidence levels for the generated trading signals.

### Raises

- ValueError: If the input strings are not in the expected format or contain invalid data.
- TypeError: If the input parameters are not of the expected type.

### Examples

```python
>>> evaluations = 'strategy1:0.8;strategy2:0.9'
>>> strategies = 'strategy1;strategy2'
>>> confidence_levels = calculate_signal_confidence(evaluations, strategies)
[0.8, 0.9]
```

```python
>>> evaluations = 'strategyA:0.7;strategyB:0.6'
>>> strategies = 'strategyA;strategyB'
>>> confidence_levels = calculate_signal_confidence(evaluations, strategies)
[0.7, 0.6]
```
