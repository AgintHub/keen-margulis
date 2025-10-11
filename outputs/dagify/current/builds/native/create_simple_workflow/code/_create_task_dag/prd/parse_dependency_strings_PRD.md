# parse_dependency_strings PRD

## Description
Parses a string of dependency relationships into a list of task source‑destination pairs.


## Conceptual Info

The shim extracts structured dependency pairs from a plain text description, enabling downstream DAG construction and validation.

## Docstring

### Summary
Parse a multiline string of dependency relationships and return them as a list of tuples.

### Parameters

- **dependencies** (str): A string containing dependency descriptions, one per line. Each line must follow the format "SourceTask depends on TargetTask" or "SourceTask,TargetTask".

### Returns

List[Tuple[str, str]]: A list of tuples where each tuple contains the source task name and the target task name.

### Raises

- ValueError: Raised if a line in the input string does not conform to an expected dependency format.
- TypeError: Raised if the input `dependencies` is not of type `str`.

### Examples

```python
>>> parse_dependency_strings('TaskA depends on TaskB\nTaskB depends on TaskC')
[('TaskA', 'TaskB'), ('TaskB', 'TaskC')]
```

```python
>>> parse_dependency_strings('Task1,Task2\nTask3,Task4')
[('Task1', 'Task2'), ('Task3', 'Task4')]
```
