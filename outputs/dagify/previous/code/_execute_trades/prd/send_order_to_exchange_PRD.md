# send_order_to_exchange PRD

## Description
Sends a trading signal to the exchange and returns the result of the order.


## Conceptual Info

This shim function acts as an intermediary between the trading signal generation and the actual execution on the exchange, encapsulating the complexity of order submission.

## Docstring

### Summary
Sends a trading signal to the exchange and returns the result.

### Parameters

- **signal** (str): The trading signal to be sent to the exchange, indicating the action to be taken (e.g., 'buy', 'sell').

### Returns

str: A string representation of a dictionary containing the result of the order, including details such as order ID, status, and any relevant metadata.

### Raises

- ValueError: If the signal is not one of the recognized trading signals (e.g., 'buy', 'sell', 'hold').
- ConnectionError: If there is an issue connecting to the exchange or sending the order.

### Examples

```python
>>> result = send_order_to_exchange(signal='buy')
>>> print(result)
{'order_id': 12345, 'status': 'success', 'message': 'Order executed successfully'}
```

```python
>>> result = send_order_to_exchange(signal='invalid_signal')
>>> print(result)
ValueError: Invalid trading signal 'invalid_signal'
```
