# format_dependency_list PRD

## Description
Formats a list of dependencies into a string representation.


## Conceptual Info

The format_dependency_list shim function formats a list of dependencies into a string representation, which can be used to describe the dependencies between subtasks.

## Docstring

### Summary
Formats a list of dependencies into a string representation.

### Parameters

- **dependencies** (str): A list of dependencies where each dependency is represented as 'subtask_id_1 -> subtask_id_2'.

### Returns

str: The formatted dependency list as a string.

### Raises

- ValueError: When the input dependencies are invalid or empty.
- TypeError: When the input type is incorrect.

### Examples

```python
>>> format_dependency_list(dependencies=['A -> B', 'B -> C'])
'A -> B, B -> C'
```

```python
>>> format_dependency_list(dependencies=[])
''
```
