# define_risk_management_rules PRD

## Description
Establish risk management rules to control exposure and potential losses.


## Conceptual Info

This node synthesizes a set of risk‑management controls that align with the selected trading strategy, ensuring that exposure, loss limits, and diversification are quantified and enforceable.

## Docstring

### Summary
Generate risk‑management rules based on the chosen trading strategy.

### Parameters

- **strategy** (Dict[str, Any]): A dictionary containing the output from the `choose_trading_strategy` node. Expected keys include `strategy_name`, `strategy_type`, `alignment_score`, `key_risk_factors`, `asset_classes`, `market_conditions`, and `trade_frequency`.

### Returns

Dict[str, Any]: A dictionary containing risk‑management parameters: `position_sizing_rule`, `max_position_size_pct`, `max_daily_drawdown_pct`, `stop_loss_level_pct`, `diversification_instruments`, and `portfolio_diversification_guidelines`.

### Raises

- ValueError: Raised when the input `strategy` dictionary is missing any of the required keys.

### Examples

```python
>>> strategy = {
...     'strategy_name': 'MomentumTrader',
...     'strategy_type': 'trend following',
...     'alignment_score': 0.85,
...     'key_risk_factors': ['market_risk', 'liquidity_risk'],
...     'asset_classes': ['equities', 'ETFs'],
...     'market_conditions': ['bullish'],
...     'trade_frequency': 5
>>> }
>>> risk = define_risk_management_rules(strategy)
>>> print(risk)
{
  'position_sizing_rule': 'fixed_percentage',
  'max_position_size_pct': 0.02,
  'max_daily_drawdown_pct': 0.015,
  'stop_loss_level_pct': 0.01,
  'diversification_instruments': ['equities', 'ETFs', 'bonds'],
  'portfolio_diversification_guidelines': 'Limit any single sector to <20% of total position, maintain at least 30% of capital in liquid equities.'
}
```

```python
>>> strategy = {
...     'strategy_name': 'MeanReversionFX',
...     'strategy_type': 'mean reversion',
...     'alignment_score': 0.78,
...     'key_risk_factors': ['currency_risk', 'counterparty_risk'],
...     'asset_classes': ['forex'],
...     'market_conditions': ['stable'],
...     'trade_frequency': 20
>>> }
>>> risk = define_risk_management_rules(strategy)
>>> print(risk)
{
  'position_sizing_rule': 'volatility_scaling',
  'max_position_size_pct': 0.01,
  'max_daily_drawdown_pct': 0.02,
  'stop_loss_level_pct': 0.005,
  'diversification_instruments': ['forex', 'interest_rate_futures'],
  'portfolio_diversification_guidelines': 'Do not exceed 10% exposure to any single currency pair; maintain a minimum 50/50 split between currency and interest‑rate derivatives.'
}
```
