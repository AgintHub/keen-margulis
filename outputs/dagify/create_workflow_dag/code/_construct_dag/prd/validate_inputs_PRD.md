# validate_inputs PRD

## Description
Validates the inputs for constructing a DAG, checking dependency map and node outputs for correctness.


## Conceptual Info

This shim node is responsible for validating the inputs required for constructing a Directed Acyclic Graph (DAG). It checks the dependency map and node outputs to ensure they are correctly formatted and consistent.

## Docstring

### Summary
Validates the dependency map and node outputs for DAG construction.

### Parameters

- **dependency_map** (str): A string representing the dependency map between tasks.
- **node_outputs** (str): A string containing output structures for each node.

### Returns

str: A string indicating the result of the validation.

### Raises

- ValueError: If the dependency map or node outputs are invalid or inconsistent.
- TypeError: If the input types are incorrect.

### Examples

```python
>>> validate_inputs(dependency_map='task1:task2,task3', node_outputs='task1:out1,task2:out2')
>>> print(output)
'Validation successful'
```

```python
>>> validate_inputs(dependency_map='invalid_map', node_outputs='task1:out1')
>>> print(output)
'Validation failed: Invalid dependency map'
```
