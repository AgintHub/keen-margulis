# check_final_dag_validity PRD

## Description
Determines the final validity of a DAG based on its original validity and whether adjustments were made.


## Conceptual Info

This shim evaluates whether a Directed Acyclic Graph (DAG) remains valid after optional corrective operations. It accepts the original validation status and a flag indicating if any adjustments were applied, returning a single boolean that indicates the overall validity.

## Docstring

### Summary
Return the final validity of a DAG based on its original validity and whether adjustments were made.

### Parameters

- **is_originally_valid** (bool): Indicates if the DAG was valid before any adjustments were attempted.
- **adjustments_made** (bool): True if any corrective changes (e.g., cycle removal or missing dependency resolution) were applied to the DAG.

### Returns

bool: True if the DAG is considered valid after adjustments; False otherwise.

### Raises

- ValueError: Raised when either input is not of boolean type.
- TypeError: Raised when inputs are of incorrect type (not bool).

### Examples

```python
>>> check_final_dag_validity(True, False)
True
```

```python
>>> check_final_dag_validity(False, True)
True
```

```python
>>> check_final_dag_validity(False, False)
False
```
