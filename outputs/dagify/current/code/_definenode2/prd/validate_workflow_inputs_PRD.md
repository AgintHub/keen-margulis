# validate_workflow_inputs PRD

## Description
Validates workflow inputs based on the provided workflow ID and name.


## Conceptual Info

This shim node is responsible for validating workflow inputs, specifically checking if the provided workflow ID and name are valid.

## Docstring

### Summary
Validates the workflow inputs based on the provided workflow ID and name.

### Parameters

- **workflow_id** (str): The unique identifier for the workflow to be validated.
- **workflow_name** (str): The name of the workflow to be validated.

### Returns

bool: True if the workflow inputs are valid, False otherwise.

### Raises

- TypeError: If the input types are incorrect, such as non-string inputs for workflow_id or workflow_name.

### Examples

```python
>>> validate_workflow_inputs(workflow_id='wf_123', workflow_name='example_workflow')
True
```

```python
>>> validate_workflow_inputs(workflow_id='', workflow_name='invalid_workflow')
False
```
