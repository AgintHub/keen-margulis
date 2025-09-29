# process_order_result PRD

## Description
Processes the result of an order sent to the exchange and returns the outcome as a string.


## Conceptual Info

This shim node processes the result of an order sent to the exchange, interpreting the outcome and returning it as a string that can be used to determine the next steps in trade execution.

## Docstring

### Summary
Processes the order result from the exchange and returns the outcome as a string.

### Parameters

- **result** (str): The order result received from the exchange, expected to be in a format that can be processed into a string outcome.

### Returns

str: The outcome of the order processing, which could indicate success, failure, or other relevant statuses.

### Raises

- ValueError: If the input 'result' is not in an expected format or contains invalid data.
- TypeError: If the input 'result' is not of type str or cannot be converted to str.

### Examples

```python
>>> process_order_result(result='{"status": "success", "orderId": 12345}')
'Order processed successfully'
```

```python
>>> process_order_result(result='{"status": "failed", "error": "insufficient funds"}')
'Order failed: insufficient funds'
```
