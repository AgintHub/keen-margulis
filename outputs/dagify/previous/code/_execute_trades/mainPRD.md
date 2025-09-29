# _execute_trades - Complete PRD Documentation

## Overview
PRDs for nodes in the '_execute_trades' module.

## Table of Contents

- [validate_trading_signals](#validate_trading_signals)

- [filter_signals_by_confidence](#filter_signals_by_confidence)

- [convert_signals_to_orders](#convert_signals_to_orders)

- [execute_trade_orders](#execute_trade_orders)

- [check_execution_success](#check_execution_success)

- [format_trade_details](#format_trade_details)



---

## validate_trading_signals

### Description
Validates trading signals based on input signals and status.

### Conceptual Info

This shim node is responsible for validating trading signals based on the input signals and their generation status. It plays a crucial role in ensuring that only valid trading signals are processed further in the trading execution pipeline.

### Docstring

**Summary:** Validates trading signals based on input signals and status, returning a list of validated signals.

**Parameters:**

- signals (str): Input trading signals to be validated, expected to be a string representation that can be processed.
- status (str): Status of the signal generation, indicating whether the signal generation was successful.
**Returns:** List[str] - A list of validated trading signals.

**Raises:**

- ValueError: When the input signals are malformed or cannot be processed.
- TypeError: When the input types are incorrect, such as signals or status not being strings.
**Examples:**

```python
>>> validate_trading_signals(signals='signal1,signal2', status='success')
['signal1', 'signal2']
```

```python
>>> validate_trading_signals(signals='invalid_signal', status='failure')
[]
```



---

## filter_signals_by_confidence

### Description
Filters trading signals based on their confidence levels.

### Conceptual Info

This shim node filters trading signals based on their associated confidence levels, playing a crucial role in refining trading decisions by eliminating signals that do not meet a certain confidence threshold.

### Docstring

**Summary:** Filters trading signals based on their confidence levels.

**Parameters:**

- signals (str): A string representation of a list of trading signals.
- confidence_levels (str): A string representation of a list of confidence levels corresponding to the trading signals.
**Returns:** List[str] - A list of trading signals that have been filtered based on their confidence levels.

**Raises:**

- ValueError: If the input signals or confidence levels are not valid or cannot be parsed.
- TypeError: If the input types are not as expected.
**Examples:**

```python
>>> signals = '["signal1", "signal2", "signal3"]'
>>> confidence_levels = '[0.8, 0.4, 0.9]'
>>> filtered_signals = filter_signals_by_confidence(signals=signals, confidence_levels=confidence_levels)
["signal1", "signal3"]
```

```python
>>> signals = '["buy", "sell", "hold"]'
>>> confidence_levels = '[0.7, 0.3, 0.6]'
>>> filtered_signals = filter_signals_by_confidence(signals=signals, confidence_levels=confidence_levels)
["buy"]
```



---

## convert_signals_to_orders

### Description
Converts trading signals and their confidence levels into a list of trade orders represented as dictionaries.

### Conceptual Info

This shim function is responsible for transforming trading signals and their associated confidence levels into a structured format representing trade orders, which can be used for execution.

### Docstring

**Summary:** Converts trading signals and confidence levels into trade orders.

**Parameters:**

- signals (str): A JSON encoded string representing a list of trading signals.
- confidence_levels (str): A JSON encoded string representing a list of confidence levels corresponding to the trading signals.
**Returns:** List[dict] - A list of dictionaries where each dictionary contains details of a trade order, including trade type, quantity, and price, derived from the input signals and confidence levels.

**Raises:**

- ValueError: Raised when the input signals or confidence levels are not valid JSON encoded lists, or when their lengths do not match.
- TypeError: Raised when the decoded JSON does not result in a list for signals or a list of floats for confidence levels.
**Examples:**

```python
>>> import json
>>> signals = json.dumps(['buy', 'sell'])
>>> confidence_levels = json.dumps([0.8, 0.7])
>>> convert_signals_to_orders(signals, confidence_levels)
[{'trade_type': 'buy', 'confidence': 0.8, 'quantity': 100, 'price': 50.0}, {'trade_type': 'sell', 'confidence': 0.7, 'quantity': 50, 'price': 51.0}]
```

```python
>>> import json
>>> signals = json.dumps(['buy'])
>>> confidence_levels = json.dumps([0.9])
>>> convert_signals_to_orders(signals, confidence_levels)
[{'trade_type': 'buy', 'confidence': 0.9, 'quantity': 200, 'price': 49.0}]
```



---

## execute_trade_orders

### Description
Executes trade orders by processing the input list of trade orders and returning the execution results.

### Conceptual Info

This shim node is responsible for executing trade orders generated by the trading signal processing pipeline. It takes a list of trade orders as input, processes them, and returns the execution results.

### Docstring

**Summary:** Executes trade orders based on the provided input and returns the execution results.

**Parameters:**

- orders (str): A JSON string representing a list of trade orders, where each order contains details such as trade type, quantity, and price.
**Returns:** List[dict] - A list of dictionaries, where each dictionary contains the execution result for a trade order, including status and any relevant details.

**Raises:**

- ValueError: If the input 'orders' is not a valid JSON string or does not contain a list of trade orders.
- TypeError: If the input 'orders' is not a string.
**Examples:**

```python
>>> orders = '[{"trade_type": "buy", "quantity": 100, "price": 50.0}, {"trade_type": "sell", "quantity": 50, "price": 51.0}]'
>>> execution_results = execute_trade_orders(orders=orders)
[{"status": "success", "details": {"trade_type": "buy", "quantity": 100, "price": 50.0}}, {"status": "success", "details": {"trade_type": "sell", "quantity": 50, "price": 51.0}}]
```

```python
>>> orders = '[{"trade_type": "invalid", "quantity": 100, "price": 50.0}]'
>>> execution_results = execute_trade_orders(orders=orders)
[{"status": "failed", "details": {"trade_type": "invalid", "quantity": 100, "price": 50.0}, "error": "Invalid trade type"}]
```



---

## check_execution_success

### Description
Evaluates the success status of trade execution results.

### Conceptual Info

This shim node assesses the outcome of trade executions to determine overall success.

### Docstring

**Summary:** Checks if trade execution was successful based on the provided results.

**Parameters:**

- results (List[dict]): List of dictionaries containing trade execution results and details.
**Returns:** bool - True if all trades were executed successfully, False otherwise.

**Raises:**

- ValueError: If the input results are not in the expected format.
- TypeError: If the input type is not a list of dictionaries.
**Examples:**

```python
>>> execution_results = [{'status': 'success', 'details': 'Trade executed successfully'}, {'status': 'success', 'details': 'Trade executed successfully'}]
>>> check_execution_success(results=execution_results)
True
```

```python
>>> execution_results = [{'status': 'failure', 'details': 'Insufficient funds'}, {'status': 'success', 'details': 'Trade executed successfully'}]
>>> check_execution_success(results=execution_results)
False
```



---

## format_trade_details

### Description
Formats trade execution results into a list of human-readable trade details.

### Conceptual Info

This shim node is responsible for taking trade execution results and formatting them into a list of human-readable strings that contain trade details such as trade type, quantity, and price.

### Docstring

**Summary:** Formats trade execution results into a list of human-readable trade details.

**Parameters:**

- results (str): Trade execution results in a string format that needs to be parsed and formatted.
**Returns:** List[str] - List of formatted trade details, including information such as trade type, quantity, and price.

**Raises:**

- ValueError: If the input results string is malformed or cannot be parsed.
- TypeError: If the input results is not of type str.
**Examples:**

```python
>>> execution_results = '{"trade_type": "buy", "quantity": 100, "price": 50.0}'
>>> formatted_details = format_trade_details(results=execution_results)
>>> print(formatted_details)
["Trade Type: buy, Quantity: 100, Price: 50.0"]
```

```python
>>> execution_results = '[{"trade_type": "sell", "quantity": 50, "price": 55.0}, {"trade_type": "buy", "quantity": 200, "price": 52.0}]'
>>> formatted_details = format_trade_details(results=execution_results)
>>> print(formatted_details)
["Trade Type: sell, Quantity: 50, Price: 55.0", "Trade Type: buy, Quantity: 200, Price: 52.0"]
```

