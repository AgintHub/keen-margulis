# define_trading_objectives PRD

## Description
Specify the primary objectives of the trading system, including return targets and risk tolerance.


## Conceptual Info

This node collects high‑level financial goals and risk parameters that steer the entire trading system. The objectives shape strategy selection, risk rules, and monitoring thresholds downstream.

## Docstring

### Summary
Generate a dictionary of core trading objectives such as target return, drawdown limits, risk tolerance, and any special constraints.

### Returns

dict: A mapping with keys `return_target_percent`, `max_drawdown_percent`, `risk_tolerance_category`, and `constraints` corresponding to the output structure.

### Raises

- ValueError: If the target return or drawdown is negative, or if the risk tolerance category is not one of the supported values.

### Examples

```python
>>> objectives = define_trading_objectives()
>>> print(objectives)
{\n  "return_target_percent": 12.5,\n  "max_drawdown_percent": 20.0,\n  "risk_tolerance_category": "moderate",\n  "constraints": [\n    "No leverage over 2x",\n    "Position size capped at 5% of portfolio"\n  ]\n}
```

```python
>>> objectives = define_trading_objectives()
>>> objectives['risk_tolerance_category'] = "conservative"
>>> print(objectives['risk_tolerance_category'])
"conservative"
```
