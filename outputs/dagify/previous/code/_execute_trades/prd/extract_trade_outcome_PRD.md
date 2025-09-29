# extract_trade_outcome PRD

## Description
Extracts the trade outcome from the trade execution result dictionary.


## Conceptual Info

This shim function is designed to extract the trade outcome from the result of a trade execution, which is expected to be in a dictionary format. It plays a crucial role in processing trade execution results and providing the outcome for further processing or logging.

## Docstring

### Summary
Extracts the trade outcome from a trade execution result dictionary.

### Parameters

- **result** (str): A string representation of a dictionary containing the trade execution result.

### Returns

str: The extracted trade outcome as a string.

### Raises

- ValueError: If the input string is not a valid dictionary representation or if the dictionary does not contain the expected 'outcome' key.
- TypeError: If the input is not a string.

### Examples

```python
>>> extract_trade_outcome(result="{'outcome': 'success', 'details': 'Trade executed successfully'}")
'success'
```

```python
>>> extract_trade_outcome(result="{'outcome': 'failure', 'error': 'Insufficient funds'}")
'failure'
```
