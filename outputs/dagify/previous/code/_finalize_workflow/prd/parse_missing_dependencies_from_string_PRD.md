# parse_missing_dependencies_from_string PRD

## Description
Parses a comma‑separated string of missing dependency names and returns a list of cleaned dependency identifiers.


## Conceptual Info

This shim extracts and normalizes missing dependency identifiers from a comma‑separated string representation provided by the DAG validation step.

## Docstring

### Summary
Parses a string of missing dependency names and returns them as a list of cleaned strings.

### Parameters

- **deps_str** (str): Comma‑separated string of missing dependency names, possibly with surrounding whitespace.

### Returns

List[str]: A list of dependency names with whitespace trimmed; an empty list if the input is empty or contains only whitespace.

### Raises

- ValueError: If the input string contains invalid characters (e.g., non‑printable characters).
- TypeError: If deps_str is not of type str.

### Examples

```python
>>> parse_missing_dependencies_from_string('task_a, task_b, task_c')
['task_a', 'task_b', 'task_c']
```

```python
>>> parse_missing_dependencies_from_string('   ')
[]
```
