# validateworkflow PRD

## Description
Check the workflow for any errors or inconsistencies.


## Conceptual Info

This node validates the workflow created by the connected nodes, checking for any errors or inconsistencies.

## Docstring

### Summary
Validate the workflow to ensure it is correct and functional.

### Parameters

- **connected_nodes** (List[str]): List of connected node names from the 'connectnodes' node.

### Returns

Tuple[bool, str]: A tuple containing the validation result (bool) and a message indicating the outcome of the validation (str).

### Raises

- ValueError: If the input 'connected_nodes' is not a list or is empty.
- TypeError: If the 'connected_nodes' list contains non-string values.

### Examples

```python
>>> connected_nodes = ['node1', 'node2']
>>> validation_result, validation_message = validateworkflow(connected_nodes)
(True, 'Workflow is valid.')
```

```python
>>> connected_nodes = []
>>> try:
...     validation_result, validation_message = validateworkflow(connected_nodes)
>>> except ValueError as e:
...     print(e)
'connected_nodes' cannot be empty.
```
