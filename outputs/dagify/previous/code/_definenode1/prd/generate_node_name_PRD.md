# generate_node_name PRD

## Description
Generates a node name based on the provided workflow name.


## Conceptual Info

This shim generates a node name based on the workflow name provided, serving as a unique identifier for a node within a workflow.

## Docstring

### Summary
Generates a node name based on the workflow name.

### Parameters

- **workflow_name** (str): The name of the workflow for which to generate a node name.

### Returns

str: The generated node name based on the workflow name.

### Raises

- ValueError: If the workflow name is empty or not a string.
- TypeError: If the workflow name is not of type string.

### Examples

```python
>>> generate_node_name('example_workflow')
'example_workflow_node'
```

```python
>>> generate_node_name('another_workflow')
'another_workflow_node'
```
