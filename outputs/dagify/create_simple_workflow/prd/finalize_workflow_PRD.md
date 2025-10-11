# finalize_workflow PRD

## Description
Finalize the workflow DAG


## Conceptual Info

The `finalize_workflow` node validates the refined DAG for completeness, acyclicity, and optimal concurrency. It performs any last‑minute adjustments such as re‑ordering parallel branches or inserting dummy synchronization nodes, and produces a concise summary of the final graph.

## Docstring

### Summary
Finalize and validate a workflow DAG, ensuring it is complete, concurrent, and acyclic.

### Parameters

- **dag_edges** (List[str]): Directed edges of the refined DAG, formatted as 'TaskA->TaskB'.
- **is_acyclic** (bool): True if the refined DAG contains no cycles.
- **is_concurrent** (bool): True if the refined DAG already supports maximum concurrency.
- **max_concurrency** (int): Maximum number of tasks that can run concurrently in the refined DAG.

### Returns

dict: A dictionary with keys `dag_is_complete`, `dag_is_concurrent`, `dag_is_acyclic`, `adjusted_node_list`, and `dag_summary`.

### Raises

- ValueError: If `dag_edges` is empty or malformed.
- RuntimeError: If the DAG cannot be made acyclic or fully concurrent after adjustments.

### Examples

```python
>>> result = finalize_workflow(dag_edges=['A->B', 'B->C'], is_acyclic=True, is_concurrent=False, max_concurrency=2)
>>> print(result)
{'dag_is_complete': True, 'dag_is_concurrent': True, 'dag_is_acyclic': True, 'adjusted_node_list': ['B'], 'dag_summary': 'DAG has 3 nodes and 2 edges. Concurrency adjusted to 2.'}
```

```python
>>> try:
...     finalize_workflow(dag_edges=[], is_acyclic=True, is_concurrent=True, max_concurrency=1)
>>> except ValueError as e:
...     print(e)
'dag_edges list is empty or contains malformed entries.'
```
