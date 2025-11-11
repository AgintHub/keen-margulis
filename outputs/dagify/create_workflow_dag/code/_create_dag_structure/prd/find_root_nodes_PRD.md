# find_root_nodes PRD

## Description
This shim identifies the root nodes in a directed acyclic graph (DAG) given its nodes and dependencies.


## Conceptual Info

The find_root_nodes shim is crucial for constructing a valid DAG by identifying nodes with no incoming edges, which are the starting points of the graph.

## Docstring

### Summary
Finds the root nodes in a DAG given its nodes and dependencies.

### Parameters

- **nodes** (List[str]): A list of node names in the DAG.
- **dependencies** (List[tuple]): A list of dependencies between nodes, where each dependency is a tuple of two node names.

### Returns

List[str]: A list of root node names in the DAG.

### Raises

- ValueError: If the input nodes or dependencies are invalid (e.g., a node has no dependencies but is not a root node).
- TypeError: If the input types are incorrect (e.g., nodes is not a list of strings, dependencies is not a list of tuples).

### Examples

```python
>>> nodes = ['A', 'B', 'C']
>>> dependencies = [('A', 'B'), ('B', 'C')]
>>> root_nodes = find_root_nodes(nodes, dependencies)
['A']
```

```python
>>> nodes = ['X', 'Y', 'Z']
>>> dependencies = [('X', 'Y'), ('Y', 'Z'), ('Z', 'X')]
>>> try:
...     root_nodes = find_root_nodes(nodes, dependencies)
>>> except ValueError as e:
...     print(e)
Dependencies form a cycle, making it impossible to create a valid DAG
```
