# generate_summary PRD

## Description
Generates a short textual summary of the workflow based on its validity, whether adjustments were made, and if cycles were removed.


## Conceptual Info

The shim encapsulates the logic for creating a concise human‑readable description of the finalized workflow’s state. It takes three boolean flags indicating whether the workflow is valid, whether any adjustments were performed during finalization, and whether cycles were removed, and produces a single string that summarizes these conditions in natural language.

## Docstring

### Summary
Create a summary string for a finalized workflow.

### Parameters

- **is_valid** (bool): True if the finalized workflow is valid (acyclic and all dependencies resolved).
- **adjustments_made** (bool): True if any adjustments (e.g., cycle removal or dependency resolution) were applied during finalization.
- **cycles_removed** (bool): True if one or more cycles were detected and removed from the original DAG.

### Returns

str: A human‑readable summary stating the workflow’s validity, whether adjustments were made, and if cycles were removed.

### Raises

- TypeError: Raised when any of the arguments is not a bool.
- ValueError: Raised if any boolean argument is None.

### Examples

```python
>>> generate_summary(is_valid=True, adjustments_made=False, cycles_removed=False)
"The workflow is valid. No adjustments were made."
```

```python
>>> generate_summary(is_valid=False, adjustments_made=True, cycles_removed=True)
"The workflow is invalid. Adjustments were made: cycles removed."
```
