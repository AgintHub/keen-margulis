# format_dependencies PRD

## Description
Formats a list of dependency tuples into human‑readable strings describing task dependencies.


## Conceptual Info

The format_dependencies shim converts raw dependency pairs into readable strings for downstream usage.

## Docstring

### Summary
Converts a list of task dependency pairs into formatted strings.

### Parameters

- **dependency_pairs** (list[tuple[str, str]]): A list where each element is a 2‑tuple (TaskA, TaskB) indicating that TaskA depends on TaskB.

### Returns

list[str]: A list of strings, each in the form 'TaskA depends on TaskB', preserving the order of the input pairs.

### Raises

- TypeError: If dependency_pairs is not a list or its elements are not tuples of strings.
- ValueError: If any tuple does not contain exactly two elements.

### Examples

```python
>>> format_dependencies([('TaskA', 'TaskB'), ('TaskC', 'TaskD')])
['TaskA depends on TaskB', 'TaskC depends on TaskD']
```

```python
>>> format_dependencies([])
[]
```
