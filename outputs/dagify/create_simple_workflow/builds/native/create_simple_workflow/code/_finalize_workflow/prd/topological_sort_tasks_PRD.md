# topological_sort_tasks PRD

## Description
Computes an ordered list of task identifiers for a DAG given node and edge counts.


## Conceptual Info

The topological_sort_tasks shim is responsible for translating raw DAG metrics (node and edge counts) into a deterministic ordering of tasks, which later steps use for serialization, validation, and dependency resolution.

## Docstring

### Summary
Generate a topological ordering of task identifiers based on node and edge counts.

### Parameters

- **node_count** (str): Total number of nodes in the DAG, expressed as a string that can be parsed into an integer.
- **edge_count** (str): Total number of directed edges in the DAG, expressed as a string that can be parsed into an integer.

### Returns

str: A string representation of a list of task identifiers sorted in topological order. The list contains one identifier per node.

### Raises

- ValueError: Raised when node_count or edge_count is negative or represents an infeasible DAG configuration.
- TypeError: Raised when either node_count or edge_count is not convertible to an integer.

### Examples

```python
>>> topological_sort_tasks(node_count='3', edge_count='2')
['task1', 'task2', 'task3']
```

```python
>>> topological_sort_tasks(node_count='2', edge_count='1')
['taskA', 'taskB']
```
