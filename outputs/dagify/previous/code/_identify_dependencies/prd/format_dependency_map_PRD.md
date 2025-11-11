# format_dependency_map PRD

## Description
Formats the task relationships into a list of dependency pairs.


## Conceptual Info

This shim function is responsible for transforming task relationships into a structured dependency map format.

## Docstring

### Summary
Formats task relationships into a list representing the dependency map.

### Parameters

- **relationships** (str): A string representing the task relationships to be formatted.

### Returns

List[str]: A list of strings where each string represents a dependency between tasks.

### Raises

- ValueError: If the input relationships are not in the expected format.
- TypeError: If the input type is not a string or if the relationships cannot be processed.

### Examples

```python
>>> format_dependency_map(relationships='task1->task2,task2->task3')
>>> format_dependency_map(relationships='taskA->taskB')
['task1->task2', 'task2->task3']
```

```python
>>> format_dependency_map(relationships='taskX->taskY')
['taskX->taskY']
```
