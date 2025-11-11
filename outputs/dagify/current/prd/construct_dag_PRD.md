# construct_dag PRD

## Description
Construct the workflow DAG using the decomposed tasks and their dependencies


## Conceptual Info

This node constructs a Directed Acyclic Graph (DAG) representing the workflow based on the decomposed tasks, their dependencies, and output structures.

## Docstring

### Summary
Constructs the workflow DAG using the task list, dependency map, and node outputs.

### Parameters

- **task_list** (List[str]): List of decomposed tasks or steps derived from the objective.
- **dependency_map** (List[str]): List representing the dependency map between tasks.
- **node_outputs** (List[str]): List containing output structures for each node.

### Returns

str: The constructed workflow DAG structure represented as a string.

### Raises

- ValueError: If the task list, dependency map, or node outputs are inconsistent or malformed.

### Examples

```python
>>> task_list = ['task1', 'task2', 'task3']
>>> dependency_map = [('task1', 'task2'), ('task2', 'task3')]
>>> node_outputs = [{'task1': 'output1'}, {'task2': 'output2'}, {'task3': 'output3'}]
>>> dag_structure = construct_dag(task_list, dependency_map, node_outputs)
digraph G { task1 -> task2; task2 -> task3; }
```

```python
>>> task_list = ['A', 'B', 'C']
>>> dependency_map = [('A', 'B'), ('B', 'C')]
>>> node_outputs = [{'A': 'resultA'}, {'B': 'resultB'}, {'C': 'resultC'}]
>>> dag_structure = construct_dag(task_list, dependency_map, node_outputs)
digraph G { A -> B; B -> C; }
```
