# format_edges_for_output PRD

## Description
Formats a list of parsed dependencies into a list of strings representing edges in a DAG.


## Conceptual Info

The format_edges_for_output shim function takes a list of parsed dependencies and formats them into a list of strings representing edges in a DAG. This is necessary to provide a standardized output format for the create_dag_structure function.

## Docstring

### Summary
Formats a list of parsed dependencies into a list of strings representing edges in a DAG.

### Parameters

- **dependencies** (str): A string representation of a list of parsed dependencies, where each dependency is a tuple of two node names.

### Returns

List[str]: A list of strings representing edges in a DAG, where each edge is in the format 'node1->node2'.

### Raises

- ValueError: When the input dependencies are invalid or malformed.
- TypeError: When the input dependencies are not of the correct type.

### Examples

```python
>>> format_edges_for_output(dependencies=[('A', 'B'), ('B', 'C')])
['A->B', 'B->C']
```

```python
>>> format_edges_for_output(dependencies=[('D', 'E'), ('E', 'F')])
['D->E', 'E->F']
```
