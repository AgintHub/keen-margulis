# assess_risk PRD

## Description
Assess the risk associated with potential trades based on market data.


## Conceptual Info

This node assesses the risk associated with potential trades based on current and historical market data fetched by its parent node, fetch_market_data.

## Docstring

### Summary
Assess the risk associated with potential trades based on current market conditions.

### Parameters

- **market_data** (Dict[str, List[float]]): Dictionary containing current prices and historical data fetched from fetch_market_data.

### Returns

Tuple[List[float], List[str]]: A tuple containing a list of risk levels and a list of risk factors.

### Raises

- ValueError: If market_data is empty or does not contain the required keys.

### Examples

```python
>>> market_data = {'current_prices': [100.0, 200.0], 'historical_data': [[90.0, 100.0], [190.0, 200.0]]}
>>> risk_levels, risk_factors = assess_risk(market_data)
([0.5, 0.3], ['volatility', 'liquidity'])
```

```python
>>> market_data = {'current_prices': [150.0, 250.0], 'historical_data': [[140.0, 150.0], [240.0, 250.0]]}
>>> risk_levels, risk_factors = assess_risk(market_data)
([0.4, 0.2], ['market_trend', 'economic_indicators'])
```
