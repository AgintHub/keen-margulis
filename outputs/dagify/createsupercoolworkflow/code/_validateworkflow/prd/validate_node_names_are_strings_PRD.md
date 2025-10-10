# validate_node_names_are_strings PRD

## Description
Validates that the provided connected node names are strings.


## Conceptual Info

This shim function is responsible for validating that all connected node names provided to it are indeed strings. It plays a crucial role in ensuring data consistency and preventing potential errors downstream in the workflow validation process.

## Docstring

### Summary
Validates that all connected node names are strings.

### Parameters

- **connected_nodes** (List[str]): A list of node names to be validated as strings.

### Returns

str: A message indicating whether the validation was successful or not.

### Raises

- TypeError: If any of the node names in the list are not strings.

### Examples

```python
>>> validate_node_names_are_strings(connected_nodes=['node1', 'node2'])
'Validation successful'
```

```python
>>> validate_node_names_are_strings(connected_nodes=['node1', 2])
TypeError: All node names must be strings.
```
