# compile_trading_workflow_summary PRD

## Description
Synthesize the components into a comprehensive trading workflow summary.


## Conceptual Info

This node collects the outputs of the four upstream nodes and transforms them into human‑readable, concise summary strings that capture the essence of the trading workflow.

## Docstring

### Summary
Generate a comprehensive trading workflow summary from the outputs of the objectives, strategy, execution plan, and monitoring nodes.

### Parameters

- **objectives** (dict): Dictionary containing the outputs of the `define_trading_objectives` node. Expected keys: `return_target_percent`, `max_drawdown_percent`, `risk_tolerance_category`, `constraints`.
- **strategy** (dict): Dictionary containing the outputs of the `choose_trading_strategy` node. Expected keys: `strategy_name`, `strategy_type`, `alignment_score`, `key_risk_factors`, `asset_classes`, `market_conditions`, `trade_frequency`.
- **execution_plan** (dict): Dictionary containing the outputs of the `develop_trade_execution_plan` node. Expected keys: `asset_classes`, `order_types`, `execution_venues`, `timing_strategy`, `slippage_tolerance_pct`, `position_size_rule`, `max_order_size`, `execution_latency_ms`, `order_submission_method`.
- **monitoring** (dict): Dictionary containing the outputs of the `design_monitoring_and_control_system` node. Expected keys: `monitored_metrics`, `metric_thresholds`, `alert_enabled`, `alert_frequency`, `reporting_schedule`, `reporting_channels`, `intervention_steps`, `manual_override_allowed`, `control_automation_level`.

### Returns

dict: A dictionary with the following string keys: `objectives_summary`, `strategy_summary`, `execution_plan_summary`, `monitoring_system_summary`, `overall_summary`.

### Raises

- ValueError: Raised if any required field in one of the input dictionaries is missing or of an unexpected type.

### Examples

```python
>>> objectives = {
...     'return_target_percent': 12.5,
...     'max_drawdown_percent': 7.0,
...     'risk_tolerance_category': 'moderate',
...     'constraints': ['no leveraged ETFs', 'max 5% position per asset']
>>> }
>>> strategy = {
...     'strategy_name': 'Mean Reversion Bot',
...     'strategy_type': 'mean reversion',
...     'alignment_score': 0.85,
...     'key_risk_factors': ['market volatility', 'liquidity'],
...     'asset_classes': ['equities', 'ETFs'],
...     'market_conditions': ['high volatility', 'low correlation'],
...     'trade_frequency': 20
>>> }
>>> execution_plan = {
...     'asset_classes': ['equities', 'ETFs'],
...     'order_types': ['limit', 'bracket'],
...     'execution_venues': ['NYSE', 'NASDAQ'],
...     'timing_strategy': 'intraday',
...     'slippage_tolerance_pct': 0.1,
...     'position_size_rule': 'fixed 1% of capital',
...     'max_order_size': 1000,
...     'execution_latency_ms': 50.0,
...     'order_submission_method': 'FIX'
>>> }
>>> monitoring = {
...     'monitored_metrics': ['PnL', 'Sharpe', 'drawdown'],
...     'metric_thresholds': [0.0, 1.0, 5.0],
...     'alert_enabled': True,
...     'alert_frequency': 'real-time',
...     'reporting_schedule': 'daily',
...     'reporting_channels': ['email', 'dashboard'],
...     'intervention_steps': ['pause orders', 'notify risk manager'],
...     'manual_override_allowed': False,
...     'control_automation_level': 'fully automated'
>>> }
>>> summary = compile_trading_workflow_summary(objectives, strategy, execution_plan, monitoring)
>>> print(summary['overall_summary'])
"The trading workflow aims for a 12.5% annual return with a 7% maximum drawdown, employing a moderate risk tolerance. A mean‑reversion strategy targeting equities and ETFs is used, achieving an 85% alignment score. Trades are executed via limit and bracket orders on NYSE and NASDAQ, intraday, with 0.1% slippage tolerance and 1% capital position sizing. Monitoring tracks PnL, Sharpe ratio, and drawdown in real‑time, sending alerts and daily reports. All components are fully automated, ensuring rapid response to threshold breaches."
```

```python
>>> # Minimal example with placeholder values
>>> summary = compile_trading_workflow_summary({
...     'return_target_percent': 8.0,
...     'max_drawdown_percent': 5.0,
...     'risk_tolerance_category': 'conservative',
...     'constraints': []
>>> }, {
...     'strategy_name': 'Trend Following',
...     'strategy_type': 'trend following',
...     'alignment_score': 0.9,
...     'key_risk_factors': [],
...     'asset_classes': ['forex'],
...     'market_conditions': ['bullish'],
...     'trade_frequency': 5
>>> }, {
...     'asset_classes': ['forex'],
...     'order_types': ['market'],
...     'execution_venues': ['OANDA'],
...     'timing_strategy': 'market open',
...     'slippage_tolerance_pct': 0.2,
...     'position_size_rule': 'fixed 2% of capital',
...     'max_order_size': 10000,
...     'execution_latency_ms': 10.0,
...     'order_submission_method': 'REST'
>>> }, {
...     'monitored_metrics': ['PnL'],
...     'metric_thresholds': [0.0],
...     'alert_enabled': False,
...     'alert_frequency': 'none',
...     'reporting_schedule': 'weekly',
...     'reporting_channels': ['email'],
...     'intervention_steps': [],
...     'manual_override_allowed': True,
...     'control_automation_level': 'semi-automated'
>>> })
>>> print(summary['objectives_summary'])
"Objective: Target an 8% annual return with a 5% maximum drawdown under a conservative risk tolerance."
```
