# extract_task_objective PRD

## Description
Extracts the primary objective or task from a given user input string.


## Conceptual Info

This shim function plays a crucial role in task definition by identifying the primary objective from user-provided input, which is essential for workflow initialization and execution.

## Docstring

### Summary
Extracts the task objective from a user-provided input string, returning the objective as a string.

### Parameters

- **user_input** (str): The input string from which the task objective will be extracted.

### Returns

str: The extracted task objective.

### Raises

- ValueError: If the input string is empty or does not contain a valid task objective.
- TypeError: If the input is not a string.

### Examples

```python
>>> extract_task_objective('The primary goal is to complete project X.')
'complete project X'
```

```python
>>> extract_task_objective('Objective: Finish all tasks by the end of the week.')
'Finish all tasks by the end of the week'
```
