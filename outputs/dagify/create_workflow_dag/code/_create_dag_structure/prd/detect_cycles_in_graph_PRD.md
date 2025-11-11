# detect_cycles_in_graph PRD

## Description
This shim detects whether a cycle exists in a graph represented by a list of nodes and their dependencies.


## Conceptual Info

The detect_cycles_in_graph shim is crucial for validating the structure of a Directed Acyclic Graph (DAG), ensuring it does not contain cycles which would prevent a valid topological sorting.

## Docstring

### Summary
Detects whether a cycle exists in a graph given its nodes and dependencies.

### Parameters

- **nodes** (List[str]): List of node names in the graph.
- **dependencies** (List[tuple]): List of dependencies where each dependency is a tuple of two node names (node1, node2) indicating node1 -> node2.

### Returns

bool: True if a cycle is detected in the graph, False otherwise.

### Raises

- ValueError: If the input graph structure is invalid (e.g., a node references a non-existent node).
- TypeError: If the input types do not match the expected types (list of str for nodes and list of tuples for dependencies).

### Examples

```python
>>> detect_cycles_in_graph(['A', 'B', 'C'], [('A', 'B'), ('B', 'C')])
False
```

```python
>>> detect_cycles_in_graph(['A', 'B', 'C'], [('A', 'B'), ('B', 'C'), ('C', 'A')])
True
```
