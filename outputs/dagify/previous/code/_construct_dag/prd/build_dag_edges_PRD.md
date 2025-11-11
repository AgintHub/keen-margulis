# build_dag_edges PRD

## Description
This shim node generates a list of edges representing the DAG structure based on the provided dependencies.


## Conceptual Info

The build_dag_edges shim is crucial for constructing the Directed Acyclic Graph (DAG) structure by generating edges based on task dependencies.

## Docstring

### Summary
Generates a list of edges for the DAG based on the provided dependencies.

### Parameters

- **dependencies** (List[tuple]): A list of tuples representing the dependencies between tasks.

### Returns

List[str]: A list of strings representing the edges in the DAG, where each edge is in the format 'task1 -> task2'.

### Raises

- ValueError: If the dependencies are malformed or inconsistent.
- TypeError: If the input dependencies are not a list of tuples.

### Examples

```python
>>> dependencies = [('A', 'B'), ('B', 'C'), ('A', 'C')]
>>> dag_edges = build_dag_edges(dependencies=dependencies)
['A -> B', 'B -> C', 'A -> C']
```

```python
>>> dependencies = [('task1', 'task2'), ('task2', 'task3')]
>>> dag_edges = build_dag_edges(dependencies=dependencies)
['task1 -> task2', 'task2 -> task3']
```
