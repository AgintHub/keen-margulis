# validate_dag_format PRD

## Description
Validates the format of a DAG structure represented as a string of edges.


## Conceptual Info

This shim node is responsible for validating the format of a DAG (Directed Acyclic Graph) structure represented as a string of edges. It ensures that the input DAG structure conforms to expected formatting rules.

## Docstring

### Summary
Validates the format of the input DAG structure represented by the given edges.

### Parameters

- **parsed_edges** (str): A string representing the edges of the DAG structure to be validated.

### Returns

str: A message indicating whether the DAG format is valid or not.

### Raises

- ValueError: If the input DAG structure is not well-formed or does not conform to expected formatting rules.
- TypeError: If the input type is not a string.

### Examples

```python
>>> validate_dag_format(parsed_edges='A->B,B->C,C->D')
>>> validate_dag_format(parsed_edges='A->B,B->C,C->D,A->D')
'DAG format is valid'
```

```python
>>> validate_dag_format(parsed_edges='A->B,B->C,C->A')
'DAG format is invalid: cyclic detected'
```
