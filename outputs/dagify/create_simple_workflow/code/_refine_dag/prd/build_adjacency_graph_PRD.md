# build_adjacency_graph PRD

## Description
Constructs an adjacency graph representation from a list of node identifiers and dependency edges.


## Conceptual Info

The build_adjacency_graph shim takes raw DAG information and transforms it into a graph structure that the rest of the system can consume for validation, topology analysis, and execution planning.

## Docstring

### Summary
Builds an adjacency graph from a list of node identifiers and dependency edges.

### Parameters

- **dag_nodes** (str): Comma‑separated string of unique task identifiers.
- **dag_edges** (str): Comma‑separated string of directed edges in the format 'source->target'.

### Returns

str: A string representation of a dictionary mapping each node id to a list of its downstream node ids.

### Raises

- ValueError: Raised when an edge references a node not present in dag_nodes or when the edge format is invalid.
- TypeError: Raised when dag_nodes or dag_edges are not of type str.

### Examples

```python
>>> dag_nodes = "A,B,C"
>>> dag_edges = "A->B,B->C"
>>> graph_str = build_adjacency_graph(dag_nodes, dag_edges)
>>> print(graph_str)
'{'A': ['B'], 'B': ['C'], 'C': []}'
```

```python
>>> dag_nodes = "X,Y"
>>> dag_edges = ""
>>> print(build_adjacency_graph(dag_nodes, dag_edges))
'{'X': [], 'Y': []}'
```
