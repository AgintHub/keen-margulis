# parse_dependency_map PRD

## Description
Parses a given dependency map string into a list of tuples representing task dependencies.


## Conceptual Info

This shim function is crucial for converting a string representation of task dependencies into a structured format that can be used for constructing a Directed Acyclic Graph (DAG) in workflow management systems.

## Docstring

### Summary
Parses a dependency map string into a list of tuples, where each tuple represents a dependency between tasks.

### Parameters

- **dependency_map** (str): A string representing the dependency map between tasks.

### Returns

List[tuple]: A list of tuples, where each tuple contains information about task dependencies.

### Raises

- ValueError: If the input dependency map string is malformed or cannot be parsed.
- TypeError: If the input is not a string.

### Examples

```python
>>> dependency_map_str = 'task1:task2,task3;task2:task4'
>>> parsed_dependencies = parse_dependency_map(dependency_map=dependency_map_str)
[('task1', ['task2', 'task3']), ('task2', ['task4'])]
```

```python
>>> dependency_map_str = 'A:B,C;B:D'
>>> parsed_dependencies = parse_dependency_map(dependency_map=dependency_map_str)
[('A', ['B', 'C']), ('B', ['D'])]
```
