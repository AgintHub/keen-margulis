# validate_node_names PRD

## Description
Validates the names of two nodes to ensure they are properly formatted and valid for connection.


## Conceptual Info

This shim function is responsible for validating the names of two nodes before they are connected in a DAG.

## Docstring

### Summary
Validates the names of two nodes to ensure they are valid for connection.

### Parameters

- **node1_name** (str): The name of the first node to be validated.
- **node2_name** (str): The name of the second node to be validated.

### Returns

str: A string indicating the validation result of the node names.

### Raises

- ValueError: If either node name is empty or contains invalid characters.
- TypeError: If either node name is not a string.

### Examples

```python
>>> validate_node_names(node1_name='valid_node1', node2_name='valid_node2')
'Node names are valid'
```

```python
>>> validate_node_names(node1_name='', node2_name='valid_node2')
ValueError: 'Node name cannot be empty'
```
