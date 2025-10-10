# decompose_objective PRD

## Description
Decompose the objective into smaller, manageable tasks or steps


## Conceptual Info

This node takes the defined objective from its parent node 'define_objective' and breaks it down into smaller, manageable tasks or steps.

## Docstring

### Summary
Decomposes the given objective into a list of tasks or steps.

### Parameters

- **objective** (str): The defined objective or task description obtained from the 'define_objective' node.

### Returns

List[str]: A list of decomposed tasks or steps derived from the objective.

### Raises

- ValueError: If the objective is empty or not a string.

### Examples

```python
>>> decompose_objective(objective='Create a workflow DAG')
['Define objective', 'Decompose objective', 'Identify dependencies', 'Construct DAG']
```

```python
>>> decompose_objective(objective='Develop a machine learning model')
['Collect data', 'Preprocess data', 'Train model', 'Evaluate model']
```
