# finalizeworkflow PRD

## Description
Complete the workflow creation process.


## Conceptual Info

The finalizeworkflow node completes the workflow creation process by confirming its creation and functionality based on the validation result from the validateworkflow node.

## Docstring

### Summary
Finalize the workflow creation process based on the validation result.

### Parameters

- **validation_result** (bool): Result of the workflow validation from the validateworkflow node.
- **validation_message** (str): Message indicating the outcome of the validation from the validateworkflow node.

### Returns

Tuple[str, str]: A tuple containing the status of the workflow and the URL or identifier for accessing the workflow.

### Raises

- ValueError: If the validation result is False, indicating the workflow is not valid.

### Examples

```python
>>> validation_result = True
>>> validation_message = 'Workflow is valid and functional.'
>>> workflow_status, workflow_url = finalizeworkflow(validation_result, validation_message)
('success', 'https://example.com/workflow/123')
```

```python
>>> validation_result = False
>>> validation_message = 'Workflow contains errors.'
>>> try:
...     workflow_status, workflow_url = finalizeworkflow(validation_result, validation_message)
>>> except ValueError as e:
...     print(e)
'Workflow is not valid.'
```
