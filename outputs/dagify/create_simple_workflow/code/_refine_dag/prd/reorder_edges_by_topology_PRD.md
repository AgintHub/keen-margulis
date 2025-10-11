# reorder_edges_by_topology PRD

## Description
Reorders a list of DAG edges according to their topological levels, returning the edges sorted by source task level.


## Conceptual Info

This shim reorders raw DAG edges so that execution can be staged level‑by‑level, supporting concurrency analysis downstream.

## Docstring

### Summary
Reorders edges by topological source levels.

### Parameters

- **dag_edges** (str): A comma‑separated string of edges formatted as 'source->target'.
- **level_structure** (str): A JSON string mapping each node to its topological level (int).

### Returns

List[str]: Edges sorted in ascending order of the source node's level.

### Raises

- ValueError: If the input strings cannot be parsed or an edge references an undefined node.
- TypeError: If either argument is not a string.

### Examples

```python
>>> edges = 'A->B,B->C,D->E'
>>> levels = '{"A":0,"B":1,"C":2,"D":0,"E":1}'
>>> result = reorder_edges_by_topology(dag_edges=edges, level_structure=levels)
>>> print(result)
['A->B', 'D->E', 'B->C']
```

```python
>>> edges = 'X->Y,Y->Z,Z->W'
>>> levels = '{"X":0,"Y":1,"Z":2,"W":3}'
>>> print(reorder_edges_by_topology(dag_edges=edges, level_structure=levels))
['X->Y', 'Y->Z', 'Z->W']
```
