# refine_dag PRD

## Description
Refine the DAG to maximize concurrency and ensure acyclicity.


## Conceptual Info

This node takes a previously constructed DAG and optimizes it for maximum concurrent execution by reordering independent tasks and ensuring no cycles.

## Docstring

### Summary
Optimizes a DAG for maximum concurrency while preserving acyclicity.

### Parameters

- **dag_nodes** (List[str]): Ordered list of task identifiers in the DAG.
- **dag_edges** (List[str]): List of edges representing dependencies, formatted as "TaskA->TaskB".
- **is_acyclic** (bool): Indicates whether the input DAG is acyclic.

### Returns

Tuple[List[str], bool, bool, int]: A tuple containing (refined_dag_edges, is_acyclic, is_concurrent, max_concurrency).

### Raises

- ValueError: Raised if dag_edges is empty or if the input graph is cyclic.

### Examples

```python
>>> dag_nodes = ['A', 'B', 'C'],
>>> dag_edges = ['A->B', 'B->C'],
>>> is_acyclic = True,
>>> refined = refine_dag(dag_nodes, dag_edges, is_acyclic),
>>> print(refined)
(['A->B', 'B->C'], True, False, 1)
```

```python
>>> dag_nodes = ['A', 'B', 'C'],
>>> dag_edges = ['A->C'],
>>> is_acyclic = True,
>>> refined = refine_dag(dag_nodes, dag_edges, is_acyclic),
>>> print(refined)
(['A->C'], True, True, 2)
```
