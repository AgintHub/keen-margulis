# validate_prayer_inputs PRD

## Description
Validates the inputs related to prayer invocation and connection status.


## Conceptual Info

This shim node is responsible for validating the inputs related to prayer invocation and connection status, ensuring they meet the required criteria before further processing.

## Docstring

### Summary
Validates prayer invocation and connection status inputs.

### Parameters

- **prayer_invocation** (str): The actual invocation or words used in the prayer.
- **connection_status** (str): The status or feeling of connection during the prayer.

### Returns

str: Output indicating whether the inputs are valid.

### Raises

- ValueError: When the prayer invocation or connection status is empty or invalid.
- TypeError: When the input types are not strings.

### Examples

```python
>>> validate_prayer_inputs(prayer_invocation='example invocation', connection_status='connected')
'Inputs are valid'
```

```python
>>> validate_prayer_inputs(prayer_invocation='', connection_status='connected')
'ValueError: Prayer invocation cannot be empty'
```
