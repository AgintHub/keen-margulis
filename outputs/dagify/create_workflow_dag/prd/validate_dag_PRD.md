# validate_dag PRD

## Description
Validate the constructed workflow DAG for correctness and acyclicity


## Conceptual Info

This node validates the constructed workflow DAG for correctness and ensures it is acyclic.

## Docstring

### Summary
Validate the constructed workflow DAG for correctness and acyclicity.

### Parameters

- **dag_structure** (str): The constructed workflow DAG structure from the construct_dag node.

### Returns

bool: Whether the DAG is valid and acyclic.

### Raises

- ValueError: If the DAG structure is malformed or contains cycles.

### Examples

```python
>>> validate_dag('A->B;B->C')
True
```

```python
>>> validate_dag('A->B;B->A')
False
```
