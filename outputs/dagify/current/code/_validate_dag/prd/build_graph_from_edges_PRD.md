# build_graph_from_edges PRD

## Description
Constructs a graph representation from a given list of edges.


## Conceptual Info

This shim function is responsible for transforming a list of edges into a graph representation, which is crucial for further analysis such as checking for acyclicity and validating the well-formedness of the graph.

## Docstring

### Summary
Builds a graph representation from a given list of edges.

### Parameters

- **edges** (str): A string representing the list of edges in the graph, where edges are typically represented as pairs of nodes.

### Returns

str: A string representing the constructed graph.

### Raises

- ValueError: If the input edges string is malformed or cannot be parsed correctly.
- TypeError: If the input edges is not a string.

### Examples

```python
>>> edges = '[(1, 2), (2, 3), (3, 4)]'
>>> graph = build_graph_from_edges(edges=edges)
'Graph with nodes: [1, 2, 3, 4] and edges: [(1, 2), (2, 3), (3, 4)]'
```

```python
>>> edges = '[(A, B), (B, C)]'
>>> graph = build_graph_from_edges(edges=edges)
'Graph with nodes: [A, B, C] and edges: [(A, B), (B, C)]'
```
