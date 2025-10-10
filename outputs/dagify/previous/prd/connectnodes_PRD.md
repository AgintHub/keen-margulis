# connectnodes PRD

## Description
Establish the connections between the nodes.


## Conceptual Info

This node establishes the connections between the defined nodes to create a workflow Directed Acyclic Graph (DAG).

## Docstring

### Summary
Connects the defined nodes in the workflow.

### Parameters

- **node1_name** (str): Name of the first node from definenode1 output.
- **node2_name** (str): Name of the second node from definenode2 output.

### Returns

List[str]: A list containing the names of the connected nodes.

### Raises

- ValueError: If either node1_name or node2_name is empty or not a string.
- ConnectionError: If the nodes cannot be connected due to a cyclic dependency.

### Examples

```python
>>> node1 = 'node_a'
>>> node2 = 'node_b'
>>> connect_nodes(node1, node2)
['node_a', 'node_b']
```

```python
>>> node1 = 'data_processing'
>>> node2 = 'data_analysis'
>>> connect_nodes(node1, node2)
['data_processing', 'data_analysis']
```
