# validate_task_references PRD

## Description
Checks that every task referenced in the parsed dependencies exists in the provided task list and reports any missing references.


## Conceptual Info

Validates that all tasks referenced in dependency tuples are defined in the task list, preventing dangling references before DAG construction.

## Docstring

### Summary
Validate that every task in `parsed_dependencies` exists in `tasks`. If any reference is missing, a `ValueError` is raised.

### Parameters

- **tasks** (List[str]): A list of all task identifiers that are considered valid.
- **parsed_dependencies** (List[Tuple[str, str]]): A list of dependency tuples in the form (source_task, target_task).

### Returns

str: A message stating that all references are valid, or a list of missing task identifiers.

### Raises

- ValueError: If any task in a dependency tuple is not present in `tasks`.
- TypeError: If the input arguments are not of the expected types (`list` of `str` and `list` of `tuple`).

### Examples

```python
>>> validate_task_references(
    tasks=['TaskA', 'TaskB', 'TaskC'],
    parsed_dependencies=[('TaskA', 'TaskB'), ('TaskB', 'TaskC')]
)
'All task references are valid.'
```

```python
>>> try:
...     validate_task_references(
    	tasks=['TaskA', 'TaskB'],
    	parsed_dependencies=[('TaskA', 'TaskC')]
    )
>>> except ValueError as e:
...     print(e)
"Missing task reference(s) found: TaskC"
```
