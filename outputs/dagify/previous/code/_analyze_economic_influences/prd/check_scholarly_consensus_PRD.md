# check_scholarly_consensus PRD

## Description
Check if there is scholarly consensus for the specified economic factor name.


## Conceptual Info

The shim verifies whether academic literature agrees on the significance of a named economic factor, serving as a decision point in historical analysis pipelines.

## Docstring

### Summary
Return a boolean indicating the presence of scholarly consensus on the significance of a specified economic factor.

### Parameters

- **factor_name** (str): The name of the economic factor to evaluate for scholarly consensus.

### Returns

bool: True if a consensus exists, False otherwise.

### Raises

- ValueError: Raised when factor_name is an empty string.
- TypeError: Raised when factor_name is not of type str.

### Examples

```python
>>> check_scholarly_consensus('Inflation')
True
```

```python
>>> check_scholarly_consensus('UnusualEvent')
False
```
