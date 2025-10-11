# generate_dag_representation PRD

## Description
Creates a string representation of a directed acyclic graph from a serialized task order.


## Conceptual Info

The shim turns a serialized list of task identifiers into a textual DAG representation that can be used by downstream nodes such as `finalize_workflow`. It is responsible for interpreting the task order string, validating its format, and producing a concise, machine‑readable description of the graph structure.

## Docstring

### Summary
Generate a string representation of a DAG from a comma‑separated task order.

### Parameters

- **task_order** (str): Comma‑separated list of task identifiers representing a topological ordering of the DAG.

### Returns

str: A string describing the DAG, formatted as an adjacency list where each task points to its successors. Example: ``"A->B, B->C, C->"``.

### Raises

- ValueError: If `task_order` is an empty string or contains malformed entries (e.g., consecutive commas or trailing commas).
- TypeError: If `task_order` is not of type `str`.

### Examples

```python
>>> generate_dag_representation('A,B,C')
"A->B, B->C, C->"
```

```python
>>> generate_dag_representation('X')
"X->"
```
