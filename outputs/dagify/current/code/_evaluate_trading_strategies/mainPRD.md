# _evaluate_trading_strategies - Complete PRD Documentation

## Overview
PRDs for nodes in the '_evaluate_trading_strategies' module.

## Table of Contents

- [validate_inputs](#validate_inputs)

- [get_available_trading_strategies](#get_available_trading_strategies)

- [evaluate_strategies_against_trends](#evaluate_strategies_against_trends)

- [select_recommended_strategies](#select_recommended_strategies)



---

## validate_inputs

### Description
Validates the input trend indicators and pattern recognition results for further processing.

### Conceptual Info

This shim node is responsible for validating the input trend indicators and pattern recognition results to ensure they are suitable for further processing in the trading strategy evaluation pipeline.

### Docstring

**Summary:** Validates input trend indicators and pattern recognition results.

**Parameters:**

- trend_indicators (str): List of indicators of market trends (e.g., bullish, bearish) to be validated.
- pattern_recognition (str): List of patterns recognized in the market data to be validated.
**Returns:** str - Output indicating whether the inputs are valid.

**Raises:**

- ValueError: When the input trend indicators or pattern recognition results are invalid or inconsistent.
- TypeError: When the input types are incorrect (e.g., not lists of strings).
**Examples:**

```python
>>> validate_inputs(trend_indicators='["bullish", "bearish"]', pattern_recognition='["head_and_shoulders", "inverse_head_and_shoulders"]')
'Inputs are valid'
```

```python
>>> validate_inputs(trend_indicators='[]', pattern_recognition='["invalid_pattern"]')
'ValueError: Invalid trend indicators or pattern recognition results.'
```



---

## get_available_trading_strategies

### Description
Returns a list of available trading strategies for evaluation.

### Conceptual Info

This shim function provides a list of available trading strategies that can be used for further evaluation in the trading system.

### Docstring

**Summary:** Retrieve a list of available trading strategies.

**Returns:** List[str] - A list of available trading strategies as strings.

**Raises:**

- RuntimeError: If the list of available trading strategies cannot be retrieved.
**Examples:**

```python
>>> available_strategies = get_available_trading_strategies()
['Strategy1', 'Strategy2', 'Strategy3']
```



---

## evaluate_strategies_against_trends

### Description
Evaluates trading strategies against market trends and pattern recognition to produce strategy evaluations.

### Conceptual Info

This shim node evaluates trading strategies against market trends and recognized patterns, serving as a bridge between market analysis and strategy recommendation.

### Docstring

**Summary:** Evaluates trading strategies against market trends and pattern recognition.

**Parameters:**

- strategies (str): A string representing available trading strategies.
- trend_indicators (str): A string containing indicators of market trends (e.g., bullish, bearish).
- pattern_recognition (str): A string containing patterns recognized in the market data.
**Returns:** List[str] - A list of strings representing evaluations of different trading strategies.

**Raises:**

- ValueError: If any of the input strings are empty or malformed.
- TypeError: If any of the input parameters are not strings.
**Examples:**

```python
>>> evaluate_strategies_against_trends(strategies='mean_reversion,trend_following', trend_indicators='bullish,bearish', pattern_recognition='head_and_shoulders,double_bottom')
['mean_reversion:strong_buy', 'trend_following:strong_sell']
```

```python
>>> evaluate_strategies_against_trends(strategies='statistical_arbitrage', trend_indicators='neutral', pattern_recognition='ascending_triangle')
['statistical_arbitrage:buy']
```



---

## select_recommended_strategies

### Description
Selects recommended trading strategies based on the evaluations of different strategies against market trend indicators and pattern recognition results.

### Conceptual Info

This shim function plays a crucial role in the trading strategy evaluation pipeline by selecting the most appropriate strategies based on market trend analysis and pattern recognition.

### Docstring

**Summary:** Selects recommended trading strategies based on the evaluations of different strategies against market trends and patterns.

**Parameters:**

- evaluations (str): A string containing evaluations of different trading strategies, typically a serialized list or a descriptive text.
- trend_indicators (str): A string containing indicators of market trends, such as bullish or bearish signals.
- pattern_recognition (str): A string containing patterns recognized in the market data, which could influence strategy selection.
**Returns:** List[str] - A list of recommended trading strategies based on the input evaluations and market analysis.

**Raises:**

- ValueError: When the input parameters are not in the expected format or contain invalid data.
- TypeError: When the input parameters are not of the expected type.
**Examples:**

```python
>>> select_recommended_strategies(evaluations='["good", "bad"]', trend_indicators='["bullish"]', pattern_recognition='["continuation"]')
['strategy_1', 'strategy_3']
```

```python
>>> select_recommended_strategies(evaluations='good,bad', trend_indicators='bullish,bearish', pattern_recognition='continuation,reversal')
['strategy_2', 'strategy_4']
```

