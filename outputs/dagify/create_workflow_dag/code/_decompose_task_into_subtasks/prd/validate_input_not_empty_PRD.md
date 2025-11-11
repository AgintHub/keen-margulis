# validate_input_not_empty PRD

## Description
Validates that the input task objective and description are not empty.


## Conceptual Info

The validate_input_not_empty shim ensures that the task objective and description are not empty before proceeding with further processing.

## Docstring

### Summary
Validates that the input task objective and description are not empty.

### Parameters

- **task_objective** (str): The primary objective or task that the workflow will accomplish.
- **task_description** (str): A detailed description of the task or objective.

### Returns

str: Output message indicating the result of the validation.

### Raises

- ValueError: When either the task objective or description is empty.
- TypeError: When either the task objective or description is not a string.

### Examples

```python
>>> validate_input_not_empty(task_objective='Example task', task_description='This is an example task.')
'Validation successful'
```

```python
>>> validate_input_not_empty(task_objective='', task_description='This is an example task.')
Validation failed: Task objective cannot be empty.
```
