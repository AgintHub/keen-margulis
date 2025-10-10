# create_workflow_url PRD

## Description
Generates a URL for accessing a workflow based on its unique identifier.


## Conceptual Info

This shim function is responsible for creating a URL that can be used to access a specific workflow based on its unique identifier. It plays a crucial role in the workflow finalization process by providing a reference to the workflow.

## Docstring

### Summary
Creates a URL for accessing a workflow based on its ID.

### Parameters

- **workflow_id** (str): The unique identifier of the workflow for which the URL is to be generated.

### Returns

str: The URL that can be used to access the workflow.

### Raises

- ValueError: If the workflow_id is invalid or empty.
- TypeError: If the workflow_id is not a string.

### Examples

```python
>>> create_workflow_url(workflow_id='wf_12345')
'https://example.com/workflows/wf_12345'
```

```python
>>> create_workflow_url(workflow_id='invalid_id')
Raises ValueError: 'Invalid workflow ID'
```
