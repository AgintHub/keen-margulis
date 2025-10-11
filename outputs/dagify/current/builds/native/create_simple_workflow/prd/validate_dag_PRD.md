# validate_dag PRD

## Description
Validate the created DAG for correctness and acyclicity


## Conceptual Info

The `validate_dag` node verifies that a workflow DAG is well‑formed, acyclic, and internally consistent. It acts as a safety net before the workflow is finalized, catching missing dependencies and logical cycles that could cause runtime failures.

## Docstring

### Summary
Validates a Directed Acyclic Graph (DAG) representation for correctness, acyclicity, and missing dependencies.

### Parameters

- **task_ids** (List[str]): List of unique identifiers for all tasks in the workflow.
- **edge_sources** (List[str]): List of task identifiers representing the source of each directed edge.
- **edge_destinations** (List[str]): List of task identifiers representing the destination of each directed edge.
- **is_valid_input** (bool): (Optional) A flag from `create_task_dag` indicating preliminary validity. It is used only as a hint; full validation is performed regardless.

### Returns

dict: Dictionary containing validation results:
- `is_valid` (bool): Overall validity.
- `node_count` (int): Number of nodes.
- `edge_count` (int): Number of directed edges.
- `cycles_detected` (List[str]): Descriptions of any detected cycles.
- `missing_dependencies` (List[str]): Tasks that reference undefined dependencies.
- `errors` (List[str]): Human‑readable error messages for all failures.

### Raises

- ValueError: If `edge_sources` and `edge_destinations` lists are not of the same length.
- ValueError: If `task_ids` contains duplicate identifiers.

### Examples

```python
>>> task_ids = ['A', 'B', 'C']
>>> edge_sources = ['A', 'B']
>>> edge_destinations = ['B', 'C']
>>> result = validate_dag(task_ids, edge_sources, edge_destinations)
>>> print(result)
{'is_valid': True, 'node_count': 3, 'edge_count': 2, 'cycles_detected': [], 'missing_dependencies': [], 'errors': []}
```

```python
>>> task_ids = ['A', 'B', 'C']
>>> edge_sources = ['A', 'B', 'C']
>>> edge_destinations = ['B', 'C', 'A']
>>> result = validate_dag(task_ids, edge_sources, edge_destinations)
>>> print(result)
{'is_valid': False, 'node_count': 3, 'edge_count': 3, 'cycles_detected': ['A -> B -> C -> A'], 'missing_dependencies': [], 'errors': ['Cycle detected: A -> B -> C -> A']}
```
