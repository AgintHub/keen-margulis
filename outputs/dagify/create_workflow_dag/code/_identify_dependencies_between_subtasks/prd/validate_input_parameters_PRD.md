# validate_input_parameters PRD

## Description
Validates the input parameters subtask_list and sequencing_requirements to ensure they are in the correct format and contain the necessary information.


## Conceptual Info

The validate_input_parameters shim is responsible for validating the input parameters to ensure they are in the correct format and contain the necessary information for the subsequent nodes to function correctly.

## Docstring

### Summary
Validate the input parameters subtask_list and sequencing_requirements.

### Parameters

- **subtask_list** (list[str]): List of subtasks or steps to achieve the task objective.
- **sequencing_requirements** (str): Description of any sequencing or ordering requirements between subtasks.

### Returns

str: Output indicating whether the input parameters are valid or not.

### Raises

- ValueError: When input validation fails due to incorrect format or missing information.
- TypeError: When input types are incorrect.

### Examples

```python
>>> validate_input_parameters(subtask_list=['task1', 'task2'], sequencing_requirements='task1 -> task2')
'Input parameters are valid'
```

```python
>>> validate_input_parameters(subtask_list=[], sequencing_requirements='')
'Input parameters are invalid'
```
