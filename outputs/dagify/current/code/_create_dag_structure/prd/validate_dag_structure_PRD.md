# validate_dag_structure PRD

## Description
Validates the structure of a Directed Acyclic Graph (DAG) given its nodes, edges, and root nodes.


## Conceptual Info

The validate_dag_structure shim function checks if a given DAG structure, represented by its nodes, edges, and root nodes, is valid. A valid DAG should not contain cycles and should have at least one root node.

## Docstring

### Summary
Validates the structure of a Directed Acyclic Graph (DAG) given its nodes, edges, and root nodes.

### Parameters

- **nodes** (str): A string of comma-separated node names in the DAG
- **edges** (str): A string of comma-separated edges in the DAG, represented as 'node1->node2'
- **roots** (str): A string of comma-separated root node names in the DAG

### Returns

bool: True if the DAG structure is valid, False otherwise

### Raises

- ValueError: When input validation fails
- TypeError: When input types are incorrect

### Examples

```python
>>> validate_dag_structure(nodes='A,B,C', edges='A->B,B->C', roots='A')
True
```

```python
>>> validate_dag_structure(nodes='A,B,C', edges='A->B,B->C,A->C', roots='A')
False
```
