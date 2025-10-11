# generate_dependency_warnings PRD

## Description
Generates warning messages for each missing dependency supplied as a comma‑separated string.


## Conceptual Info

This shim transforms a comma‑separated list of missing dependency names into human‑readable warning messages that are later included in workflow validation reports.

## Docstring

### Summary
Creates a newline‑separated string of warnings for each missing dependency provided as a comma‑separated string.

### Parameters

- **missing_deps** (str): A comma‑separated string of task identifiers that are missing dependencies.

### Returns

str: A string containing a warning for each missing dependency, one per line.

### Raises

- ValueError: If missing_deps is an empty string or None.
- TypeError: If missing_deps is not of type str.

### Examples

```python
>>> generate_dependency_warnings('task1,task2')
Warning: task1 has missing dependencies.\nWarning: task2 has missing dependencies.
```

```python
>>> generate_dependency_warnings('taskA')
Warning: taskA has missing dependencies.
```
