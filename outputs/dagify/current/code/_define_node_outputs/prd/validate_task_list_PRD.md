# validate_task_list PRD

## Description
Validates a given list of tasks to ensure they are properly formatted and contain valid content.


## Conceptual Info

This shim is responsible for validating a list of tasks derived from decomposing an objective, ensuring they are correctly formatted and contain appropriate content before further processing.

## Docstring

### Summary
Validates a list of tasks to ensure they meet specific format and content requirements.

### Parameters

- **task_list** (str): A string representation of a list of tasks to be validated.

### Returns

List[str]: A list of tasks that have been validated.

### Raises

- ValueError: If the task list is not properly formatted or contains invalid tasks.
- TypeError: If the input task list is not of type str.

### Examples

```python
>>> validate_task_list(task_list='["task1", "task2"]')
['task1', 'task2']
```

```python
>>> validate_task_list(task_list='[]')
[]
```
