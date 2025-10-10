# _monitor_trade_performance - Complete PRD Documentation

## Overview
PRDs for nodes in the '_monitor_trade_performance' module.

## Table of Contents

- [validate_trade_inputs](#validate_trade_inputs)

- [calculate_success_rate](#calculate_success_rate)

- [parse_trade_profits](#parse_trade_profits)

- [calculate_average_profit](#calculate_average_profit)

- [generate_performance_summary](#generate_performance_summary)



---

## validate_trade_inputs

### Description
Validates trade inputs to ensure they meet the required format and criteria for further processing.

### Conceptual Info

This shim node is responsible for validating trade inputs to ensure they are correctly formatted and meet the necessary criteria before being processed further in the system.

### Docstring

**Summary:** Validates trade inputs based on their results and status.

**Parameters:**

- trade_results (str): A string containing the results of the executed trades, expected to be in a specific format.
- trade_status (str): A string containing the status of the executed trades, indicating success or failure.
**Returns:** str - A string indicating the outcome of the validation process.

**Raises:**

- ValueError: Raised when the trade results or status are not in the expected format or contain invalid data.
- TypeError: Raised when the input types are not as expected (e.g., not strings).
**Examples:**

```python
>>> validate_trade_inputs(trade_results='success,100,buy', trade_status='success')
>>> print(output)
'Validation successful'
```

```python
>>> validate_trade_inputs(trade_results='failure,0,sell', trade_status='failure')
>>> print(output)
'Validation successful'
```



---

## calculate_success_rate

### Description
Calculates the success rate of trades based on their status.

### Conceptual Info

This node calculates the success rate of trades by analyzing their status, playing a crucial role in monitoring trade performance.

### Docstring

**Summary:** Calculates the success rate of trades based on their status.

**Parameters:**

- trade_status (List[str]): A list of strings representing the status of each trade (e.g., 'success', 'failure').
**Returns:** float - The success rate of the trades as a float value between 0 and 1.

**Raises:**

- ValueError: If the input list is empty or contains invalid status values.
- TypeError: If the input is not a list or if the list contains non-string values.
**Examples:**

```python
>>> trade_status = ['success', 'failure', 'success']
>>> success_rate = calculate_success_rate(trade_status=trade_status)
0.6666666666666666
```

```python
>>> trade_status = ['success', 'success', 'success']
>>> success_rate = calculate_success_rate(trade_status=trade_status)
1.0
```



---

## parse_trade_profits

### Description
Parses trade results to extract profit values as a list of floats.

### Conceptual Info

This shim function is designed to parse trade results and extract profit values, playing a crucial role in analyzing trade performance.

### Docstring

**Summary:** Parses a string of trade results and returns a list of profit values as floats.

**Parameters:**

- trade_results (str): A string containing the results of executed trades, potentially including profit information.
**Returns:** List[float] - A list of floating-point numbers representing the profit values extracted from the trade results.

**Raises:**

- ValueError: If the input string is malformed or does not contain valid profit information.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> parse_trade_profits(trade_results='Trade1:Profit=100.5,Trade2:Profit=200.8')
[100.5, 200.8]
```

```python
>>> parse_trade_profits(trade_results='Profit:150.2;Loss:50.1')
[150.2]
```



---

## calculate_average_profit

### Description
Calculates the average profit from a list of trade profits.

### Conceptual Info

This shim node is responsible for calculating the average profit from a list of trade profits, serving as a crucial component in monitoring trade performance.

### Docstring

**Summary:** Calculates the average profit from a list of trade profits.

**Parameters:**

- profits (List[float]): A list of trade profits.
**Returns:** float - The average profit calculated from the input profits. Returns 0 if the input list is empty.

**Raises:**

- TypeError: If the input is not a list or if the list contains non-numeric values.
- ValueError: If the input list contains NaN or infinity values.
**Examples:**

```python
>>> profits = [100.0, 200.0, 300.0]
>>> average_profit = calculate_average_profit(profits)
>>> print(average_profit)
200.0
```

```python
>>> profits = []
>>> average_profit = calculate_average_profit(profits)
>>> print(average_profit)
0
```



---

## generate_performance_summary

### Description
Generates a performance summary string based on the provided success rate and average profit.

### Conceptual Info

This shim generates a human-readable summary of trade performance based on the success rate and average profit of trades.

### Docstring

**Summary:** Generates a performance summary string based on the provided success rate and average profit.

**Parameters:**

- success_rate (str): The rate of successful trades as a string representation of a float.
- average_profit (str): The average profit of trades as a string representation of a float.
**Returns:** str - A summary of the trade performance including the success rate and average profit.

**Raises:**

- ValueError: If the input success rate or average profit cannot be converted to a float.
- TypeError: If the input types are not strings.
**Examples:**

```python
>>> generate_performance_summary(success_rate='0.8', average_profit='100.5')
'Trade performance summary: 80.0% success rate, average profit: $100.50'
```

```python
>>> generate_performance_summary(success_rate='0.9', average_profit='200.75')
'Trade performance summary: 90.0% success rate, average profit: $200.75'
```

