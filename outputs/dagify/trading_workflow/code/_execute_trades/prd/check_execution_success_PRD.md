# check_execution_success PRD

## Description
Evaluates the success status of trade execution results.


## Conceptual Info

This shim node assesses the outcome of trade executions to determine overall success.

## Docstring

### Summary
Checks if trade execution was successful based on the provided results.

### Parameters

- **results** (List[dict]): List of dictionaries containing trade execution results and details.

### Returns

bool: True if all trades were executed successfully, False otherwise.

### Raises

- ValueError: If the input results are not in the expected format.
- TypeError: If the input type is not a list of dictionaries.

### Examples

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
