# define_task_objective PRD

## Description
Define the primary objective or task that the workflow will accomplish.


## Conceptual Info

This node is responsible for defining the primary task or objective of the workflow DAG.

## Docstring

### Summary
This function takes no inputs and returns a task objective and its description based on user input.

### Returns

dict: A dictionary containing the task objective and its description.

### Raises

- ValueError: If the user input is empty or invalid.

### Examples

```python
>>> task_objective = define_task_objective()
>>> print(task_objective['task_objective'])  # Output: 'Train a machine learning model'
>>> print(task_objective['task_description'])  # Output: 'The goal is to train a model that can predict user behavior.'
{'task_objective': 'Train a machine learning model', 'task_description': 'The goal is to train a model that can predict user behavior.'}
```
