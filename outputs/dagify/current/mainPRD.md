# trading_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'trading_workflow' module.

## Table of Contents

- [choose_trading_strategy](#choose_trading_strategy)

- [compile_trading_workflow_summary](#compile_trading_workflow_summary)

- [define_risk_management_rules](#define_risk_management_rules)

- [define_trading_objectives](#define_trading_objectives)

- [design_monitoring_and_control_system](#design_monitoring_and_control_system)

- [develop_trade_execution_plan](#develop_trade_execution_plan)

- [identify_tradable_assets](#identify_tradable_assets)

- [specify_performance_metrics](#specify_performance_metrics)



---

## choose_trading_strategy

### Description
Select a suitable trading strategy based on the defined objectives.

### Conceptual Info

This node evaluates the trading objectives defined in the parent node and selects a trading strategy that best satisfies those objectives while considering market conditions and asset classes. The selected strategy is scored for alignment, and key characteristics such as risk factors, asset classes, and trade frequency are documented for downstream workflow components.

### Docstring

**Summary:** Select a trading strategy that aligns with the specified objectives.

**Parameters:**

- objectives (Dict[str, Any]): Dictionary containing the return target (%), maximum drawdown (%), risk tolerance category, and any additional constraints. Expected keys: 'return_target_percent', 'max_drawdown_percent', 'risk_tolerance_category', 'constraints'.
**Returns:** Dict[str, Any] - A mapping of strategy attributes: strategy_name, strategy_type, alignment_score, key_risk_factors, asset_classes, market_conditions, trade_frequency.

**Raises:**

- ValueError: Raised if any required objective key is missing or if the input type is incorrect.
**Examples:**

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



---

## compile_trading_workflow_summary

### Description
Synthesize the components into a comprehensive trading workflow summary.

### Conceptual Info

This node collects the outputs of the four upstream nodes and transforms them into human‑readable, concise summary strings that capture the essence of the trading workflow.

### Docstring

**Summary:** Generate a comprehensive trading workflow summary from the outputs of the objectives, strategy, execution plan, and monitoring nodes.

**Parameters:**

- objectives (dict): Dictionary containing the outputs of the `define_trading_objectives` node. Expected keys: `return_target_percent`, `max_drawdown_percent`, `risk_tolerance_category`, `constraints`.
- strategy (dict): Dictionary containing the outputs of the `choose_trading_strategy` node. Expected keys: `strategy_name`, `strategy_type`, `alignment_score`, `key_risk_factors`, `asset_classes`, `market_conditions`, `trade_frequency`.
- execution_plan (dict): Dictionary containing the outputs of the `develop_trade_execution_plan` node. Expected keys: `asset_classes`, `order_types`, `execution_venues`, `timing_strategy`, `slippage_tolerance_pct`, `position_size_rule`, `max_order_size`, `execution_latency_ms`, `order_submission_method`.
- monitoring (dict): Dictionary containing the outputs of the `design_monitoring_and_control_system` node. Expected keys: `monitored_metrics`, `metric_thresholds`, `alert_enabled`, `alert_frequency`, `reporting_schedule`, `reporting_channels`, `intervention_steps`, `manual_override_allowed`, `control_automation_level`.
**Returns:** dict - A dictionary with the following string keys: `objectives_summary`, `strategy_summary`, `execution_plan_summary`, `monitoring_system_summary`, `overall_summary`.

**Raises:**

- ValueError: Raised if any required field in one of the input dictionaries is missing or of an unexpected type.
**Examples:**

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



---

## define_risk_management_rules

### Description
Establish risk management rules to control exposure and potential losses.

### Conceptual Info

This node synthesizes a set of risk‑management controls that align with the selected trading strategy, ensuring that exposure, loss limits, and diversification are quantified and enforceable.

### Docstring

**Summary:** Generate risk‑management rules based on the chosen trading strategy.

**Parameters:**

- strategy (Dict[str, Any]): A dictionary containing the output from the `choose_trading_strategy` node. Expected keys include `strategy_name`, `strategy_type`, `alignment_score`, `key_risk_factors`, `asset_classes`, `market_conditions`, and `trade_frequency`.
**Returns:** Dict[str, Any] - A dictionary containing risk‑management parameters: `position_sizing_rule`, `max_position_size_pct`, `max_daily_drawdown_pct`, `stop_loss_level_pct`, `diversification_instruments`, and `portfolio_diversification_guidelines`.

**Raises:**

- ValueError: Raised when the input `strategy` dictionary is missing any of the required keys.
**Examples:**

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



---

## define_trading_objectives

### Description
Specify the primary objectives of the trading system, including return targets and risk tolerance.

### Conceptual Info

This node collects high‑level financial goals and risk parameters that steer the entire trading system. The objectives shape strategy selection, risk rules, and monitoring thresholds downstream.

### Docstring

**Summary:** Generate a dictionary of core trading objectives such as target return, drawdown limits, risk tolerance, and any special constraints.

**Returns:** dict - A mapping with keys `return_target_percent`, `max_drawdown_percent`, `risk_tolerance_category`, and `constraints` corresponding to the output structure.

**Raises:**

- ValueError: If the target return or drawdown is negative, or if the risk tolerance category is not one of the supported values.
**Examples:**

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



---

## design_monitoring_and_control_system

### Description
Create a system to monitor and control the trading system's performance.

### Conceptual Info

Configures the monitoring and control subsystem that keeps the trading engine within agreed performance bounds, triggers alerts, compiles periodic reports, and initiates intervention protocols.

### Docstring

**Summary:** Builds a monitoring and control configuration from performance metrics and trade execution details.

**Parameters:**

- performance_metrics (dict): Dictionary of performance metrics produced by ``specify_performance_metrics``. Expected keys include: ``roi``, ``sharpe_ratio``, ``max_drawdown``, ``annualized_volatility``, ``win_rate``, ``annualized_return``.
- execution_plan (dict): Dictionary of execution parameters produced by ``develop_trade_execution_plan``. Expected keys include: ``asset_classes``, ``order_types``, ``execution_venues``, ``timing_strategy``, ``slippage_tolerance_pct``, ``position_size_rule``, ``max_order_size``, ``execution_latency_ms``, ``order_submission_method``.
**Returns:** dict - A configuration dictionary containing monitoring and control settings. Keys correspond to the node's output structure.

**Raises:**

- ValueError: Raised if required metrics or execution plan keys are missing.
**Examples:**

```python
>>> performance_metrics = {
...     'roi': 0.12,
...     'sharpe_ratio': 1.4,
...     'max_drawdown': 0.05,
...     'annualized_volatility': 0.2,
...     'win_rate': 0.55,
...     'annualized_return': 0.15
>>> } 
>>> execution_plan = {
...     'asset_classes': ['Equities', 'Futures'],
...     'order_types': ['Market', 'Limit'],
...     'execution_venues': ['NYSE', 'CME'],
...     'timing_strategy': 'Intraday',
...     'slippage_tolerance_pct': 0.01,
...     'position_size_rule': 'Fixed %',
...     'max_order_size': 1000,
...     'execution_latency_ms': 10.0,
...     'order_submission_method': 'FIX'"
                "} 
>>> config = design_monitoring_and_control_system(performance_metrics, execution_plan)
>>> print(config['monitored_metrics'])
["roi", "sharpe_ratio", "max_drawdown", "annualized_volatility", "win_rate", "annualized_return"]
```

```python
>>> print(config['alert_frequency'])
"real-time"
```



---

## develop_trade_execution_plan

### Description
Create a plan for executing trades, including order types and timing.

### Conceptual Info

The execution‑plan node takes asset and risk information from its parents and synthesizes a concrete set of trade‑execution parameters. It maps asset classes to appropriate order types, selects venues that meet latency and liquidity constraints, and codifies timing, slippage, and sizing rules that align with the overall risk‑management policy.

### Docstring

**Summary:** Generate a trade execution plan from asset and risk data.

**Parameters:**

- tradable_assets (List[str]): List of tradable asset classes or instruments provided by `identify_tradable_assets`.
- position_sizing_rule (str): Identifier of the position‑sizing method defined in `define_risk_management_rules`.
- max_position_size_pct (float): Maximum position size as a percentage of portfolio capital from risk rules.
- stop_loss_level_pct (float): Stop‑loss threshold as a percentage of entry price.
**Returns:** Dict[str, Any] - Dictionary containing the execution plan fields as defined in the output structure.

**Raises:**

- ValueError: If any required input list is empty or a numeric value is non‑positive.
**Examples:**

```python
>>> plan = develop_trade_execution_plan(
...     tradable_assets=['Equity:SPY', 'Futures:ES', 'Forex:EURUSD'],
...     position_sizing_rule='fixed_percentage',
...     max_position_size_pct=2.0,
...     stop_loss_level_pct=1.5
>>> )
>>> print(plan['order_types'])
['market', 'limit', 'iceberg']
```

```python
>>> plan = develop_trade_execution_plan(
...     tradable_assets=['Equity:AAPL'],
...     position_sizing_rule='volatility_scaling',
...     max_position_size_pct=1.0,
...     stop_loss_level_pct=2.0
>>> )
>>> print(plan['timing_strategy'])
'intraday, end‑of‑day' (market close) 
```



---

## identify_tradable_assets

### Description
Determine the specific assets or instruments to be traded for the selected strategy.

### Conceptual Info

The node takes the list of asset classes proposed by the chosen trading strategy and verifies/filters them to produce the final tradable assets list and a count. It ensures that the strategy’s asset classes are valid and prepares the data for downstream execution planning.

### Docstring

**Summary:** Identify the tradable assets for a chosen trading strategy.

**Parameters:**

- asset_classes (List[str]): Asset classes or instruments suggested by the chosen trading strategy.
**Returns:** Dict[str, Any] - A dictionary containing `tradable_assets` (List[str]) and `asset_count` (int).

**Raises:**

- ValueError: If `asset_classes` is empty or not provided.
**Examples:**

```python
>>> def identify_tradable_assets(asset_classes: List[str]) -> Dict[str, Any]:
...     if not asset_classes:
...         raise ValueError("No asset classes provided.")
...     return {"tradable_assets": asset_classes, "asset_count": len(asset_classes)}
>>> # Example 1
>>> result = identify_tradable_assets(["Equities", "Forex", "Futures"])
>>> print(result)
{'tradable_assets': ['Equities', 'Forex', 'Futures'], 'asset_count': 3}
```

```python
>>> # Example 2
>>> result = identify_tradable_assets(["Commodities"])
>>> print(result)
{'tradable_assets': ['Commodities'], 'asset_count': 1}
```



---

## specify_performance_metrics

### Description
Define metrics to evaluate the performance of the trading system.

### Conceptual Info

The `specify_performance_metrics` node takes the high‑level objectives defined for the trading system and produces a set of quantitative performance indicators that can be used by downstream monitoring and control systems. These metrics provide a standardized way to benchmark the strategy against its risk tolerance and return targets.

### Docstring

**Summary:** Generate a dictionary of performance metrics based on defined trading objectives.

**Parameters:**

- return_target_percent (float): Target annualized return expressed as a percentage (e.g., 12.0 for 12%).
- max_drawdown_percent (float): Maximum acceptable drawdown expressed as a percentage of equity (e.g., 10.0 for 10%).
- risk_tolerance_category (str): Risk tolerance level, one of 'conservative', 'moderate', or 'aggressive'.
- constraints (List[str]): Additional textual constraints or special requirements for the strategy.
**Returns:** dict[str, float] - A mapping from metric names to their computed float values. The dictionary contains the keys: roi, sharpe_ratio, max_drawdown, annualized_volatility, win_rate, and annualized_return.

**Raises:**

- ValueError: If any of the required input parameters are missing or of an incorrect type.
**Examples:**

```python
>>> metrics = specify_performance_metrics(
...     return_target_percent=12.0,
...     max_drawdown_percent=10.0,
...     risk_tolerance_category='moderate',
...     constraints=['No leverage']
>>> )
{'roi': 0.12, 'sharpe_ratio': 1.4, 'max_drawdown': 0.10, 'annualized_volatility': 0.25, 'win_rate': 0.55, 'annualized_return': 0.12}
```

```python
>>> metrics = specify_performance_metrics(
...     return_target_percent=8.0,
...     max_drawdown_percent=5.0,
...     risk_tolerance_category='conservative',
...     constraints=[]
>>> )
{'roi': 0.08, 'sharpe_ratio': 1.1, 'max_drawdown': 0.05, 'annualized_volatility': 0.18, 'win_rate': 0.60, 'annualized_return': 0.08}
```

