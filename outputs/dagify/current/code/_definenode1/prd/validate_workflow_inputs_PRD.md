# validate_workflow_inputs PRD

## Description
Validates workflow inputs based on the provided workflow ID and name.


## Conceptual Info

This shim node is responsible for validating the inputs required for a workflow, ensuring that both the workflow ID and name are correctly provided and valid.

## Docstring

### Summary
Validates workflow inputs based on the provided workflow ID and name, returning a validation result.

### Parameters

- **workflow_id** (str): The unique identifier for the workflow to be validated.
- **workflow_name** (str): The name of the workflow to be validated.

### Returns

str: A string indicating the outcome of the validation process.

### Raises

- ValueError: If either the workflow ID or name is invalid or missing.
- TypeError: If the input types for workflow ID or name are not strings.

### Examples

```python
>>> validate_workflow_inputs(workflow_id='wf_123', workflow_name='example_workflow')
'Validation successful'
```

```python
>>> validate_workflow_inputs(workflow_id='', workflow_name='invalid_workflow')
ValueError: Workflow ID is required.
```
