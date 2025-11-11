# parse_dependency_string PRD

## Description
Parses a dependency string into a list of tuples representing the dependencies.


## Conceptual Info

The parse_dependency_string shim function takes a string representing dependencies between tasks and parses it into a structured format that can be used for further processing.

## Docstring

### Summary
Parses a dependency string into a list of tuples representing the dependencies.

### Parameters

- **dependency_string** (str): Input string representing the dependencies, where each dependency is represented as 'subtask_id_1 -> subtask_id_2'.

### Returns

List[tuple]: List of tuples representing the dependencies, where each tuple contains two strings representing the dependent and independent tasks.

### Raises

- ValueError: When the input string is not in the correct format.
- TypeError: When the input is not a string.

### Examples

```python
>>> parse_dependency_string('A -> B, C -> D')
[('A', 'B'), ('C', 'D')]
```

```python
>>> parse_dependency_string('E -> F, G -> H, I -> J')
[('E', 'F'), ('G', 'H'), ('I', 'J')]
```
