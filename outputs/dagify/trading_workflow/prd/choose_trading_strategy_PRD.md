# choose_trading_strategy PRD

## Description
Select a suitable trading strategy based on the defined objectives.


## Conceptual Info

This node evaluates the trading objectives defined in the parent node and selects a trading strategy that best satisfies those objectives while considering market conditions and asset classes. The selected strategy is scored for alignment, and key characteristics such as risk factors, asset classes, and trade frequency are documented for downstream workflow components.

## Docstring

### Summary
Select a trading strategy that aligns with the specified objectives.

### Parameters

- **objectives** (Dict[str, Any]): Dictionary containing the return target (%), maximum drawdown (%), risk tolerance category, and any additional constraints. Expected keys: 'return_target_percent', 'max_drawdown_percent', 'risk_tolerance_category', 'constraints'.

### Returns

Dict[str, Any]: A mapping of strategy attributes: strategy_name, strategy_type, alignment_score, key_risk_factors, asset_classes, market_conditions, trade_frequency.

### Raises

- ValueError: Raised if any required objective key is missing or if the input type is incorrect.

### Examples

```python
>>> objectives = {
...     'return_target_percent': 12.0,
...     'max_drawdown_percent': 8.0,
...     'risk_tolerance_category': 'moderate',
...     'constraints': ['no futures', 'must trade equities']
>>> }
>>> strategy = choose_trading_strategy(objectives)
>>> print(strategy['strategy_name'])
"Momentum Equity Swing"
```

```python
>>> objectives = {
...     'return_target_percent': 20.0,
...     'max_drawdown_percent': 4.0,
...     'risk_tolerance_category': 'aggressive',
...     'constraints': ['only options', 'min volatility < 0.5']
>>> }
>>> strategy = choose_trading_strategy(objectives)
>>> print(strategy['strategy_type'])
"options play"
```
