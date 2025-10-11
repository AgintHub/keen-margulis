# validate_dag_input PRD

## Description
Validates that the provided DAG node and edge lists represent a well‑formed DAG with no cycles or invalid references.


## Conceptual Info

The shim ensures that DAG inputs supplied to higher‑level orchestration functions are syntactically and semantically correct before any graph operations are performed.

## Docstring

### Summary
Validate DAG node and edge specifications and return a success message or raise errors.

### Parameters

- **dag_nodes** (str): JSON string representing a list of unique task identifiers, e.g. '["A", "B", "C"]'.
- **dag_edges** (str): JSON string representing a list of directed edges in the form 'source->target', e.g. '["A->B", "B->C"]'.

### Returns

str: A string such as "Validation succeeded" confirming that the DAG input is valid.

### Raises

- ValueError: If the node list contains duplicates, if an edge references an unknown node, or if the graph contains a cycle.
- TypeError: If either dag_nodes or dag_edges is not a string or cannot be parsed as JSON.

### Examples

```python
>>> output = validate_dag_input(dag_nodes='["A", "B", "C"]', dag_edges='["A->B", "B->C"]')
"Validation succeeded"
```

```python
>>> try:
...     validate_dag_input(dag_nodes='["A", "B"]', dag_edges='["A->B", "B->A"]')
>>> except ValueError as e:
...     print(e)
"Cycle detected: A->B->A"
```
