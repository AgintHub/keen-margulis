# extract_task_list PRD

## Description
Extracts a list of tasks from the given dependency map and node outputs.


## Conceptual Info

This shim is responsible for extracting a list of tasks based on the dependency map and node outputs provided.

## Docstring

### Summary
Extracts a list of tasks from the given dependency map and node outputs.

### Parameters

- **dependency_map** (str): A string representing the dependency map between tasks.
- **node_outputs** (str): A string containing output structures for each node.

### Returns

List[str]: A list of task names extracted from the dependency map and node outputs.

### Raises

- ValueError: If the input dependency map or node outputs are invalid or malformed.
- TypeError: If the input types are not as expected (e.g., not strings).

### Examples

```python
>>> dependency_map = 'task1:task2,task3;task2:task4'
>>> node_outputs = 'task1:out1;task2:out2;task3:out3'
>>> extract_task_list(dependency_map=dependency_map, node_outputs=node_outputs)
['task1', 'task2', 'task3', 'task4']
```

```python
>>> dependency_map = 'A:B,C;B:D'
>>> node_outputs = 'A:1;B:2;C:3;D:4'
>>> extract_task_list(dependency_map=dependency_map, node_outputs=node_outputs)
['A', 'B', 'C', 'D']
```
