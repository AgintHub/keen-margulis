# validate_node_schemas PRD

## Description
Validate the schemas of nodes in a workflow based on their connectivity.


## Conceptual Info

This shim node is responsible for validating the schemas of nodes within a workflow. It takes the names of connected nodes as input and returns a boolean indicating whether their schemas are valid.

## Docstring

### Summary
Validate the schemas of nodes based on their connectivity.

### Parameters

- **connected_nodes** (str): A string representing the names of connected nodes in the workflow.

### Returns

bool: A boolean value indicating whether the schemas of the connected nodes are valid.

### Raises

- ValueError: If the input 'connected_nodes' is not a valid string or is empty.
- TypeError: If the input 'connected_nodes' is not of type string.

### Examples

```python
>>> validate_node_schemas(connected_nodes='node1,node2,node3')
True
```

```python
>>> validate_node_schemas(connected_nodes='invalid_node')
False
```
