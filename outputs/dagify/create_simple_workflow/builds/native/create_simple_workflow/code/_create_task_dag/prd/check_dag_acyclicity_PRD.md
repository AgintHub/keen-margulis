# check_dag_acyclicity PRD

## Description
Checks whether a directed graph defined by tasks and edge lists contains any cycles, returning a boolean result.


## Conceptual Info

This shim determines the acyclicity of a task dependency DAG by examining the list of tasks and the corresponding source–destination edge pairs.

## Docstring

### Summary
Determine if a directed graph, specified by tasks and edge lists, contains a cycle.

### Parameters

- **tasks** (List[str]): A list of unique task identifiers that form the nodes of the graph.
- **edge_sources** (List[str]): A list of source task identifiers for each directed edge in the graph.
- **edge_destinations** (List[str]): A list of destination task identifiers for each directed edge in the graph.

### Returns

bool: Returns True if the graph contains no cycles (is acyclic); otherwise returns False.

### Raises

- TypeError: Raised when any of the arguments is not a list of strings.
- ValueError: Raised when the lengths of edge_sources and edge_destinations differ, or when a source/destination is not present in tasks.

### Examples

```python
>>> check_dag_acyclicity([
...     "A", "B", "C"
>>> ], [
...     "A", "B"
>>> ], [
...     "B", "C"
>>> ])
True
```

```python
>>> check_dag_acyclicity([
...     "A", "B", "C"
>>> ], [
...     "A", "B", "C"
>>> ], [
...     "B", "C", "A"
>>> ])
False
```
