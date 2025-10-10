# evaluate_strategies_against_trends - Complete PRD Documentation

## Overview
PRDs for nodes in the 'evaluate_strategies_against_trends' module.

## Table of Contents

- [analyze_market_trends](#analyze_market_trends)

- [evaluate_trading_strategies](#evaluate_trading_strategies)

- [execute_trades](#execute_trades)

- [gather_market_data](#gather_market_data)

- [generate_trading_signals](#generate_trading_signals)

- [monitor_trade_performance](#monitor_trade_performance)



---

## analyze_market_trends

### Description
Analyze market trends based on the gathered data

### Conceptual Info

This node analyzes market trends by processing the gathered market data, including current prices, historical prices, and trading volumes, to identify trend indicators and recognize patterns.

### Docstring

**Summary:** Analyzes market trends based on gathered data.

**Parameters:**

- current_prices (List[float]): Current prices of the assets gathered by the gather_market_data node.
- historical_prices (List[float]): Historical price data for the assets over a specified period gathered by the gather_market_data node.
- trading_volumes (List[float]): Trading volumes for the assets gathered by the gather_market_data node.
**Returns:** Tuple[List[str], List[str]] - A tuple containing a list of trend indicators and a list of recognized patterns in the market data.

**Raises:**

- ValueError: If any of the input lists (current_prices, historical_prices, trading_volumes) are empty or of different lengths.
**Examples:**

```python
>>> current_prices = [100.0, 120.0, 110.0]
>>> historical_prices = [90.0, 100.0, 110.0, 120.0]
>>> trading_volumes = [1000.0, 1200.0, 1100.0]
>>> trend_indicators, pattern_recognition = analyze_market_trends(current_prices, historical_prices, trading_volumes)
(['bullish'], ['ascending triangle'])
```

```python
>>> current_prices = [100.0, 80.0, 90.0]
>>> historical_prices = [110.0, 100.0, 90.0, 80.0]
>>> trading_volumes = [1000.0, 800.0, 900.0]
>>> trend_indicators, pattern_recognition = analyze_market_trends(current_prices, historical_prices, trading_volumes)
(['bearish'], ['descending triangle'])
```



---

## evaluate_trading_strategies

### Description
Evaluate different trading strategies based on the analyzed trends

### Conceptual Info

This node evaluates various trading strategies based on the analyzed market trends provided by its parent node, analyze_market_trends.

### Docstring

**Summary:** Evaluate trading strategies based on market trend analysis.

**Parameters:**

- trend_indicators (List[str]): Indicators of market trends (e.g., bullish, bearish) from analyze_market_trends.
- pattern_recognition (List[str]): Patterns recognized in the market data from analyze_market_trends.
**Returns:** Tuple[List[str], List[str]] - A tuple containing the evaluations of different trading strategies and the recommended trading strategies.

**Raises:**

- ValueError: If trend_indicators or pattern_recognition are empty or not provided.
**Examples:**

```python
>>> trend_indicators = ['bullish', 'bearish']
>>> pattern_recognition = ['ascending triangle', 'descending triangle']
>>> strategy_evaluations, recommended_strategies = evaluate_trading_strategies(trend_indicators, pattern_recognition)
(['Strategy 1: Buy', 'Strategy 2: Sell'], ['Strategy 1', 'Strategy 3'])
```

```python
>>> trend_indicators = ['neutral']
>>> pattern_recognition = ['symmetrical triangle']
>>> strategy_evaluations, recommended_strategies = evaluate_trading_strategies(trend_indicators, pattern_recognition)
(['Strategy 3: Hold'], ['Strategy 3'])
```



---

## execute_trades

### Description
Execute trades based on the generated signals

### Conceptual Info

This node executes trades based on the generated trading signals, providing results and status of the trades.

### Docstring

**Summary:** Execute trades according to the generated trading signals and return the results and status of the trades.

**Parameters:**

- trading_signals (List[str]): Generated trading signals (buy/sell/hold) from the parent node 'generate_trading_signals'.
- signal_confidence (List[float]): Confidence levels for the generated trading signals from the parent node 'generate_trading_signals'.
**Returns:** Tuple[List[str], List[str]] - A tuple containing two lists: the first list contains the results of the executed trades, and the second list contains the status of the executed trades.

**Raises:**

- ValueError: If the lengths of 'trading_signals' and 'signal_confidence' do not match.
- RuntimeError: If there is an issue executing the trades.
**Examples:**

```python
>>> trading_signals = ['buy', 'sell', 'hold']
>>> signal_confidence = [0.8, 0.7, 0.9]
>>> trade_results, trade_status = execute_trades(trading_signals, signal_confidence)
(['trade executed', 'trade executed', 'no action'], ['success', 'success', 'held'])
```

```python
>>> trading_signals = ['buy', 'sell']
>>> signal_confidence = [0.85, 0.65]
>>> trade_results, trade_status = execute_trades(trading_signals, signal_confidence)
(['trade executed', 'trade executed'], ['success', 'success'])
```



---

## gather_market_data

### Description
Collect relevant market data including prices, volumes, and other indicators

### Conceptual Info

The gather_market_data node is responsible for collecting relevant market data, including current and historical prices, as well as trading volumes for specified assets or instruments.

### Docstring

**Summary:** Gathers current and historical market data for the specified assets or instruments, returning current prices, historical prices, and trading volumes.

**Parameters:**

- assets (List[str]): List of asset symbols or identifiers to gather data for.
- start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
- end_date (str): End date for historical data in 'YYYY-MM-DD' format.
**Returns:** Tuple[List[float], List[float], List[float]] - A tuple containing three lists: current prices, historical prices, and trading volumes for the specified assets.

**Raises:**

- ValueError: If the assets list is empty or if the start_date is later than end_date.
- ConnectionError: If there's a failure in connecting to the data source.
**Examples:**

```python
>>> assets = ['AAPL', 'GOOG']
>>> start_date = '2022-01-01'
>>> end_date = '2022-12-31'
>>> result = gather_market_data(assets, start_date, end_date)
([150.0, 2800.0], [120.0, 130.0, ...], [1000.0, 2000.0])
```

```python
>>> assets = ['MSFT']
>>> start_date = '2023-01-01'
>>> end_date = '2023-01-31'
>>> result = gather_market_data(assets, start_date, end_date)
([250.0], [240.0, 245.0, ...], [500.0])
```



---

## generate_trading_signals

### Description
Generate trading signals based on the recommended strategies

### Conceptual Info

This node generates trading signals (buy/sell/hold) based on the recommended trading strategies evaluated by its parent node.

### Docstring

**Summary:** Generate trading signals and their confidence levels based on recommended strategies.

**Parameters:**

- strategy_evaluations (List[str]): Evaluations of different trading strategies from the parent node 'evaluate_trading_strategies'.
- recommended_strategies (List[str]): Recommended trading strategies based on the evaluations from the parent node 'evaluate_trading_strategies'.
**Returns:** Tuple[List[str], List[float]] - A tuple containing a list of generated trading signals and a list of their corresponding confidence levels.

**Raises:**

- ValueError: If the input lists 'strategy_evaluations' and 'recommended_strategies' are of different lengths.
- TypeError: If the input lists contain elements of incorrect types.
**Examples:**

```python
>>> strategy_evaluations = ['good', 'bad', 'neutral']
>>> recommended_strategies = ['buy', 'sell', 'hold']
>>> trading_signals, signal_confidence = generate_trading_signals(strategy_evaluations, recommended_strategies)
(['buy', 'sell', 'hold'], [0.8, 0.7, 0.9])
```

```python
>>> strategy_evaluations = ['excellent', 'poor']
>>> recommended_strategies = ['buy', 'sell']
>>> trading_signals, signal_confidence = generate_trading_signals(strategy_evaluations, recommended_strategies)
(['buy', 'sell'], [0.9, 0.6])
```



---

## monitor_trade_performance

### Description
Monitor the performance of executed trades

### Conceptual Info

The node analyzes the performance of trades executed by the 'execute_trades' node, providing metrics and a summary.

### Docstring

**Summary:** Monitors and analyzes the performance of executed trades based on the trade results and status from the 'execute_trades' node.

**Parameters:**

- trade_results (List[str]): Results of the executed trades from the 'execute_trades' node.
- trade_status (List[str]): Status of the executed trades (e.g., success, failure) from the 'execute_trades' node.
**Returns:** Tuple[List[float], str] - A tuple containing performance metrics as a list of floats and a summary of the trade performance as a string.

**Raises:**

- ValueError: If trade results or status are not provided or are invalid.
**Examples:**

```python
>>> trade_results = ['profit:100', 'loss:50']
>>> trade_status = ['success', 'failure']
>>> performance_metrics, performance_summary = monitor_trade_performance(trade_results, trade_status)
[0.5, 100.0], 'Overall performance: 50% success rate, average profit: 100.0'
```

```python
>>> trade_results = ['profit:200', 'profit:150']
>>> trade_status = ['success', 'success']
>>> performance_metrics, performance_summary = monitor_trade_performance(trade_results, trade_status)
[1.0, 175.0], 'Overall performance: 100% success rate, average profit: 175.0'
```

