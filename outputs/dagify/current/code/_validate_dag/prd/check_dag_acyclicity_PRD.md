# check_dag_acyclicity PRD

## Description
Checks if a given DAG represented as a graph is acyclic.


## Conceptual Info

This shim function checks if a Directed Acyclic Graph (DAG) represented as a graph is acyclic, playing a crucial role in validating workflow structures.

## Docstring

### Summary
Checks if a given DAG is acyclic by analyzing its graph representation.

### Parameters

- **graph** (str): The input graph representation as a string that needs to be checked for acyclicity.

### Returns

bool: True if the DAG is acyclic, False otherwise.

### Raises

- ValueError: If the input graph is not a valid representation of a DAG.
- TypeError: If the input graph is not of type string.

### Examples

```python
>>> graph_repr = 'A->B; B->C; C->D'
>>> is_acyclic = check_dag_acyclicity(graph=graph_repr)
True
```

```python
>>> graph_repr = 'A->B; B->C; C->A'
>>> is_acyclic = check_dag_acyclicity(graph=graph_repr)
False
```
