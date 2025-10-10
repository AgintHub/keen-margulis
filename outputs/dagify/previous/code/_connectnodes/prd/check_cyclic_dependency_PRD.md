# check_cyclic_dependency PRD

## Description
Checks if there's a cyclic dependency between two given nodes in a directed graph.


## Conceptual Info

This shim function is crucial for validating the structural integrity of a directed acyclic graph (DAG) when connecting nodes. It ensures that adding an edge between two nodes does not introduce a cycle, which is essential for maintaining the DAG property.

## Docstring

### Summary
Checks if connecting two nodes creates a cyclic dependency in a DAG.

### Parameters

- **node1_name** (str): The name of the first node.
- **node2_name** (str): The name of the second node.

### Returns

str: A message indicating whether a cyclic dependency exists.

### Raises

- ValueError: If either node name is invalid or empty.
- TypeError: If node names are not strings.

### Examples

```python
>>> check_cyclic_dependency(node1_name='nodeA', node2_name='nodeB')
>>> check_cyclic_dependency(node1_name='nodeC', node2_name='nodeD')
'No cyclic dependency detected.'
```

```python
>>> check_cyclic_dependency(node1_name='nodeE', node2_name='nodeF')
'Cyclic dependency detected.'
```
