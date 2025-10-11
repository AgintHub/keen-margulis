# compute_topological_levels PRD

## Description
Computes the topological level of each node in a DAG, returning a mapping of node identifiers to integer levels for use in concurrency analysis and edge reordering.


## Conceptual Info

The shim determines the depth of each task in a directed acyclic graph, enabling downstream components to compute concurrency metrics and reorder edges according to the DAG topology.

## Docstring

### Summary
Return a mapping of each node in the DAG to its topological level.

### Parameters

- **adjacency_data** (dict): A mapping where keys are node identifiers and values are lists of successor node identifiers representing directed edges.
- **dag_nodes** (list[str]): Ordered list of all node identifiers present in the DAG.

### Returns

dict: A dictionary mapping each node identifier (str) to an integer topological level (0 for source nodes).

### Raises

- ValueError: If the DAG contains nodes referenced in adjacency_data that are not present in dag_nodes, or if dag_nodes is empty.
- TypeError: If adjacency_data is not a dict or dag_nodes is not a list of strings.

### Examples

```python
>>> adjacency = {"A": ["B"], "B": ["C"], "C": []}
>>> nodes = ["A", "B", "C"]
>>> print(compute_topological_levels(adjacency, nodes))
{"A": 0, "B": 1, "C": 2}
```

```python
>>> adjacency = {"X": ["Y", "Z"], "Y": ["W"], "Z": ["W"], "W": []}
>>> nodes = ["X", "Y", "Z", "W"]
>>> print(compute_topological_levels(adjacency, nodes))
{"X": 0, "Y": 1, "Z": 1, "W": 2}
```
