# extract_nodes_from_edges PRD

## Description
Extracts a set of unique node names from a comma‑separated string of directed DAG edges in the format 'NodeA->NodeB'.


## Conceptual Info

This shim is responsible for parsing DAG edge definitions and identifying all participating nodes to support downstream DAG validation and optimization.

## Docstring

### Summary
Extracts node names from a string of DAG edges.

### Parameters

- **edges** (str): A comma‑separated string of directed edges formatted as 'NodeA->NodeB'.

### Returns

set: A set of unique node names found in the input edges.

### Raises

- ValueError: If any edge does not contain the '->' separator or the input string is empty but not None.
- TypeError: If the input `edges` is not a string.

### Examples

```python
>>> edges = 'TaskA->TaskB,TaskB->TaskC,TaskC->TaskD'
>>> nodes = extract_nodes_from_edges(edges)
>>> print(nodes)
{'TaskA', 'TaskB', 'TaskC', 'TaskD'}
```

```python
>>> edges = ''
>>> nodes = extract_nodes_from_edges(edges)
>>> print(nodes)
{}
```
