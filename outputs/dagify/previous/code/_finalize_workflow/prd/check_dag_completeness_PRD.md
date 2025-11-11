# check_dag_completeness PRD

## Description
Determines whether a directed graph with the given number of nodes and edges is complete (contains the maximum possible edges).


## Conceptual Info

This shim verifies that the DAG is fully defined by ensuring the number of edges equals the maximum possible for a directed graph of the specified node count, indicating that every potential task relationship has been specified.

## Docstring

### Summary
Check if a directed graph is complete based on node and edge counts.

### Parameters

- **node_count** (int): The number of unique nodes in the DAG.
- **edge_count** (int): The number of directed edges present in the DAG.

### Returns

bool: True when edge_count equals node_count * (node_count - 1) (i.e., the graph is complete), otherwise False.

### Raises

- ValueError: Raised if edge_count is negative or greater than the maximum possible for the given node_count.
- TypeError: Raised if node_count or edge_count are not integers.

### Examples

```python
>>> check_dag_completeness(3, 6)
True
```

```python
>>> check_dag_completeness(4, 10)
False
```

```python
>>> check_dag_completeness(-1, 5)
ValueError: edge_count cannot be negative
```
