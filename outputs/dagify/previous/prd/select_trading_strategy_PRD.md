# select_trading_strategy PRD

## Description
Choose the trading strategy to be implemented in the trading workflow, including technical and fundamental analysis.


## Conceptual Info

This node selects a trading strategy for the trading workflow based on the identified trading instruments.

## Docstring

### Summary
Selects a trading strategy for the trading workflow.

### Parameters

- **trading_instruments** (List[str]): List of trading instruments identified for inclusion in the workflow.
- **exchanges** (List[str]): List of exchanges where the trading instruments are listed.
- **listings** (List[str]): List of listings or symbols for each trading instrument.
- **market_capitalizations** (List[float]): List of market capitalizations for each trading instrument.

### Returns

{selected_strategy_name: str, strategy_principles: List[str], strategy_metrics: List[str]}: A dictionary containing the selected strategy name, its key principles, and metrics.

### Raises

- ValueError: If no suitable trading strategy can be found for the given instruments.

### Examples

```python
>>> select_trading_strategy(trading_instruments=['AAPL', 'GOOG'], exchanges=['NASDAQ'], listings=['AAPL', 'GOOG'], market_capitalizations=[1000.0, 500.0])
{'selected_strategy_name': 'Mean Reversion', 'strategy_principles': ['Buy undervalued stocks', 'Sell overvalued stocks'], 'strategy_metrics': ['Moving Averages', 'Bollinger Bands']}
```
