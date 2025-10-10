# validate_task_list PRD

## Description
Validates a given task list to ensure it conforms to the expected format and content requirements.


## Conceptual Info

This shim node is responsible for validating a task list, ensuring it is properly formatted and contains valid tasks, which is crucial for subsequent dependency analysis.

## Docstring

### Summary
Validates a task list to ensure it is in the correct format and contains valid tasks.

### Parameters

- **task_list** (str): The task list to be validated, expected to be a string representation that can be parsed into a list of tasks.

### Returns

List[str]: A list of validated tasks.

### Raises

- ValueError: If the task list is not properly formatted or contains invalid tasks.
- TypeError: If the input task list is not of type string.

### Examples

```python
>>> task_list = 'task1, task2, task3'
>>> validated_tasks = validate_task_list(task_list=task_list)
['task1', 'task2', 'task3']
```

```python
>>> task_list = 'task1, invalid_task, task3'
>>> try:
...     validated_tasks = validate_task_list(task_list=task_list)
>>> except ValueError as e:
...     print(e)
'task_list' contains invalid tasks.
```
