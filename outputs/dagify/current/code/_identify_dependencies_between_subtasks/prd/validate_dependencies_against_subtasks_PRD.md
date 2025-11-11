# validate_dependencies_against_subtasks PRD

## Description
Validates a list of dependencies against a list of subtasks to ensure they are valid and properly formatted.


## Conceptual Info

This shim function validates a list of dependencies against a list of subtasks to ensure they are valid and properly formatted.

## Docstring

### Summary
Validates a list of dependencies against a list of subtasks.

### Parameters

- **dependencies** (str): A string representation of a list of dependencies, where each dependency is represented as 'subtask_id_1 -> subtask_id_2'
- **subtask_list** (str): A string representation of a list of subtasks

### Returns

List[str]: A list of validated dependencies

### Raises

- ValueError: When a dependency is invalid or does not exist in the subtask list
- TypeError: When the input types are incorrect

### Examples

```python
>>> validate_dependencies_against_subtasks(dependencies='A -> B', subtask_list='A,B,C')
['A -> B']
```

```python
>>> validate_dependencies_against_subtasks(dependencies='A -> D', subtask_list='A,B,C')
[]
```
