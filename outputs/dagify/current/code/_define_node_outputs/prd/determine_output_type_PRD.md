# determine_output_type PRD

## Description
Determines the output type for a given task based on predefined criteria or rules.


## Conceptual Info

This shim node plays a crucial role in determining the appropriate output type for tasks generated during the decomposition process. It acts as a bridge between task generation and output structure creation, ensuring each task's output is correctly typed.

## Docstring

### Summary
Determines the output type for a given task.

### Parameters

- **task** (str): The task for which to determine the output type.

### Returns

str: The determined output type as a string.

### Raises

- ValueError: If the task is invalid or cannot be processed.
- TypeError: If the task is not of type string.

### Examples

```python
>>> determine_output_type(task='classification_task')
'categorical'
```

```python
>>> determine_output_type(task='regression_task')
'continuous'
```
