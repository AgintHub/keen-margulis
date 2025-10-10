# generate_final_dag_representation PRD

## Description
This shim generates the final string representation of the DAG after optimization.


## Conceptual Info

This shim is responsible for generating the final string representation of the DAG after it has been optimized.

## Docstring

### Summary
Generates the final DAG representation as a string based on the input DAG structure.

### Parameters

- **dag** (str): The input DAG structure that needs to be represented as a string.

### Returns

str: The final DAG representation as a string.

### Raises

- ValueError: If the input DAG is not a valid string representation.
- TypeError: If the input DAG is not of type string.

### Examples

```python
>>> final_dag = generate_final_dag_representation(dag='node1->node2;node2->node3')
>>> print(final_dag)
'digraph { node1 -> node2; node2 -> node3; }'
```

```python
>>> generate_final_dag_representation(dag='invalid_dag_structure')
>>> print(final_dag)
ValueError: Invalid DAG structure
```
