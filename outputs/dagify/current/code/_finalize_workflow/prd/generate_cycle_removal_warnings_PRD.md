# generate_cycle_removal_warnings PRD

## Description
Creates human‑readable warnings describing cycles that were removed from a directed acyclic graph.


## Conceptual Info

This shim translates a list of removed cycle identifiers into user‑friendly warning messages, ensuring downstream components are informed of the adjustments made to the workflow graph.

## Docstring

### Summary
Generate human‑readable warnings for cycles removed from a DAG.

### Parameters

- **cycles** (str): A comma‑separated string where each element represents a cycle (e.g., "A->B->A, C->D->E->C").

### Returns

str: A single string containing one warning per cycle, formatted as "Warning: removed cycle [cycle]".

### Raises

- ValueError: Raised when `cycles` is an empty string or contains only whitespace.
- TypeError: Raised when `cycles` is not a string.

### Examples

```python
>>> warnings = generate_cycle_removal_warnings('A->B->A, C->D->E->C')
>>> print(warnings)
"Warning: removed cycle A->B->A\nWarning: removed cycle C->D->E->C"
```

```python
>>> warnings = generate_cycle_removal_warnings('X->Y->Z->X')
>>> print(warnings)
"Warning: removed cycle X->Y->Z->X"
```
