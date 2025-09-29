# analyze_technical_indicators PRD

## Description
Analyzes technical indicators such as moving averages and RSI values to generate technical signals for investment decisions.


## Conceptual Info

This shim node analyzes technical indicators to provide insights for investment decisions.

## Docstring

### Summary
Analyzes moving averages and RSI values to generate technical signals.

### Parameters

- **moving_averages** (str): String representation of moving averages data.
- **rsi_values** (str): String representation of RSI values data.

### Returns

List[str]: List of technical signals indicating potential investment opportunities or risks.

### Raises

- ValueError: If the input strings for moving averages or RSI values are not properly formatted.
- TypeError: If the input parameters are not strings.

### Examples

```python
>>> analyze_technical_indicators(moving_averages='[50.2, 51.1, 49.8]', rsi_values='[30, 40, 20]')
['Bullish Signal', 'Oversold Condition']
```

```python
>>> analyze_technical_indicators(moving_averages='[100.5, 101.2, 99.8]', rsi_values='[70, 80, 60]')
['Bearish Signal', 'Overbought Condition']
```
