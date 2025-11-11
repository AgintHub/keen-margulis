# check_dependencies_exist PRD

## Description
Checks if dependencies exist between subtasks.


## Conceptual Info

The check_dependencies_exist shim function checks if there are any dependencies between subtasks.

## Docstring

### Summary
Checks if dependencies exist between subtasks.

### Parameters

- **dependencies** (str): A string representing dependencies between subtasks.

### Returns

bool: True if dependencies exist, False otherwise.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> check_dependencies_exist('subtask1 -> subtask2')
True
```

```python
>>> check_dependencies_exist('')
False
```
