# assess_risk_factors PRD

## Description
Evaluates risk factors based on anomaly detection, volatility, and RSI values to produce a list of risk factors.


## Conceptual Info

This shim evaluates risk factors associated with stock investments based on anomaly detection, volatility, and RSI values.

## Docstring

### Summary
Assesses risk factors for stock investments based on given inputs.

### Parameters

- **anomaly_detected** (str): String indicating whether any anomalies were detected in the stock trends.
- **volatility** (str): String representing the measure of stock price volatility.
- **rsi_values** (str): String containing the Relative Strength Index values for the stock.

### Returns

List[str]: A list of strings representing the identified risk factors associated with the stock investment.

### Raises

- ValueError: If the input strings are not properly formatted or contain invalid data.
- TypeError: If the input parameters are not of the expected type (str).

### Examples

```python
>>> assess_risk_factors(anomaly_detected='True', volatility='0.5', rsi_values='30,40,50')
>>> print(output)
['High Volatility Risk', 'Oversold RSI Risk']
```

```python
>>> assess_risk_factors(anomaly_detected='False', volatility='0.2', rsi_values='60,70,80')
>>> print(output)
['Low Volatility', 'Overbought RSI Warning']
```
