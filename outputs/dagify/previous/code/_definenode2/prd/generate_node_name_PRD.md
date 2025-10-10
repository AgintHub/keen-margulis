# generate_node_name PRD

## Description
Generates a node name based on the workflow context and node position.


## Conceptual Info

This shim generates a node name based on the provided workflow context and node position, playing a crucial role in workflow node definition.

## Docstring

### Summary
Generates a node name by combining workflow context and node position information.

### Parameters

- **workflow_context** (str): The workflow context containing relevant information for node naming.
- **node_position** (str): The position of the node within the workflow, used to differentiate node names.

### Returns

str: The generated node name, formatted appropriately based on the workflow context and node position.

### Raises

- ValueError: If the workflow context or node position is invalid or missing required information.
- TypeError: If the input types for workflow context or node position are not as expected.

### Examples

```python
>>> generate_node_name(workflow_context='InitializeworkflowOutput(workflow_id="wf_123", workflow_name="example_workflow")', node_position='2')
'node_2'
```

```python
>>> generate_node_name(workflow_context='InitializeworkflowOutput(workflow_id="wf_456", workflow_name="another_workflow")', node_position='3')
'node_3'
```
