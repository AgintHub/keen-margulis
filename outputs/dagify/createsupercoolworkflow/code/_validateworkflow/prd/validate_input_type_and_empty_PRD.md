# validate_input_type_and_empty PRD

## Description
Validates that the input is a non-empty list of strings.


## Conceptual Info

This shim node validates the input connected_nodes to ensure it is a non-empty list of strings, which is crucial for subsequent workflow validation steps.

## Docstring

### Summary
Validates that the input connected_nodes is a non-empty list of strings.

### Parameters

- **connected_nodes** (List[str]): List of connected node names to be validated.

### Returns

str: Output indicating the validation result or an error message.

### Raises

- ValueError: If the input list is empty.
- TypeError: If the input is not a list or if any element in the list is not a string.

### Examples

```python
>>> validate_input_type_and_empty(connected_nodes=['node1', 'node2'])
'Validation successful'
```

```python
>>> validate_input_type_and_empty(connected_nodes=[])
ValueError: Input list is empty
```

```python
>>> validate_input_type_and_empty(connected_nodes=['node1', 2])
TypeError: All elements in the list must be strings
```
