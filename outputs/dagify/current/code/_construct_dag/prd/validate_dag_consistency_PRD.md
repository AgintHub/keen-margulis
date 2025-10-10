# validate_dag_consistency PRD

## Description
Validates the consistency of a Directed Acyclic Graph (DAG) given task list, dependencies, and node outputs.


## Conceptual Info

This shim node plays a crucial role in ensuring the integrity of the DAG structure by validating its consistency against the provided task list, dependencies, and node outputs.

## Docstring

### Summary
Validates the DAG consistency by checking if the task list, dependencies, and node outputs are coherent.

### Parameters

- **task_list** (str): A string representing the list of tasks in the DAG.
- **dependencies** (str): A string representing the dependencies between tasks in the DAG.
- **node_outputs** (str): A string representing the outputs of each node in the DAG.

### Returns

str: A string indicating whether the DAG is consistent. Returns 'DAG is consistent' if valid, otherwise raises an exception.

### Raises

- ValueError: If the task list, dependencies, or node outputs are invalid or inconsistent.
- TypeError: If the input types are not as expected (e.g., not strings).

### Examples

```python
>>> validate_dag_consistency(task_list='task1,task2,task3', dependencies='task1->task2,task2->task3', node_outputs='task1:out1,task2:out2,task3:out3')
'DAG is consistent'
```

```python
>>> validate_dag_consistency(task_list='task1,task2', dependencies='task1->task2,task2->task3', node_outputs='task1:out1,task2:out2')
ValueError: Inconsistent DAG structure detected.
```
