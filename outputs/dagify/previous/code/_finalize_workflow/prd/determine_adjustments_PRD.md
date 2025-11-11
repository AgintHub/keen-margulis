# determine_adjustments PRD

## Description
Determines which nodes need adjustment based on concurrency and acyclicity flags.


## Conceptual Info

This shim is responsible for deciding which workflow nodes must be modified when the DAG is either intended to run concurrently or must remain acyclic. The function receives the concurrency and acyclicity flags, validates them, and returns a list of node identifiers that require adjustment.

## Docstring

### Summary
Return a list of node names that require adjustment based on the `is_concurrent` and `is_acyclic` flags.

### Parameters

- **is_concurrent** (str): Flag indicating whether the DAG should allow concurrent execution. Expected values: 'True' or 'False'.
- **is_acyclic** (str): Flag indicating whether the DAG is acyclic. Expected values: 'True' or 'False'.

### Returns

LIST_STR: A list of node names (strings) that need to be adjusted. If no adjustments are necessary, an empty list is returned.

### Raises

- ValueError: Raised when either `is_concurrent` or `is_acyclic` is not one of the accepted string values ('True', 'False').
- TypeError: Raised when either `is_concurrent` or `is_acyclic` is not a string.

### Examples

```python
>>> determine_adjustments("True", "True")
[]
```

```python
>>> determine_adjustments("False", "True")
["Task1", "Task2"]
```
