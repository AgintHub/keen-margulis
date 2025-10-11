# finalize_workflow PRD

## Description
Finalize the workflow DAG


## Conceptual Info

The finalize_workflow node takes a validated DAG, checks for any remaining inconsistencies such as missing dependencies or cycles, applies necessary adjustments, and produces a clean, ordered representation ready for execution.

## Docstring

### Summary
Finalize a workflow DAG by validating its structure, resolving missing dependencies, removing cycles, and ordering tasks.

### Parameters

- **task_ids** (List[str]): Unique identifiers of all tasks in the DAG.
- **edge_sources** (List[str]): Source task identifiers for each directed edge.
- **edge_destinations** (List[str]): Destination task identifiers for each directed edge.
- **is_valid** (bool): Result of the validation step (True if the DAG passed all checks).
- **node_count** (int): Total number of nodes in the DAG.
- **edge_count** (int): Total number of directed edges in the DAG.
- **cycles_detected** (List[str]): List of cycle identifiers found during validation.
- **missing_dependencies** (List[str]): List of node names that reference non‑existent dependencies.
- **errors** (List[str]): Detailed error messages from the validation step.

### Returns

Dict[str, Any]: A dictionary containing the finalized DAG representation and metadata: dag_representation (str), is_valid (bool), adjustments_made (bool), adjusted_task_order (List[str]), missing_dependencies (List[str]), cycles_detected (List[str]), warnings (List[str]), and summary (str).

### Raises

- ValueError: If any required input lists are empty or lengths of edge_sources and edge_destinations mismatch.

### Examples

```python
>>> dag = finalize_workflow(

...     task_ids=['A', 'B', 'C'],

...     edge_sources=['A', 'B'],

...     edge_destinations=['B', 'C'],

...     is_valid=True,

...     node_count=3,

...     edge_count=2,

...     cycles_detected=[],

...     missing_dependencies=[],

...     errors=[]

>>> )
{'dag_representation': 'A -> B -> C', 'is_valid': True, 'adjustments_made': False, 'adjusted_task_order': ['A', 'B', 'C'], 'missing_dependencies': [], 'cycles_detected': [], 'warnings': [], 'summary': 'DAG finalized successfully.'}
```

```python
>>> dag = finalize_workflow(

...     task_ids=['A', 'B', 'C'],

...     edge_sources=['A', 'B', 'C'],

...     edge_destinations=['B', 'C', 'A'],

...     is_valid=False,

...     node_count=3,

...     edge_count=3,

...     cycles_detected=['A->B->C->A'],

...     missing_dependencies=[],

...     errors=['Cycle detected']

>>> )
{'dag_representation': 'A -> B -> C', 'is_valid': False, 'adjustments_made': True, 'adjusted_task_order': ['A', 'B', 'C'], 'missing_dependencies': [], 'cycles_detected': ['A->B->C->A'], 'warnings': ['Cycle removed: A->B->C->A'], 'summary': 'DAG finalized with cycle removal.'}
```
