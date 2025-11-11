# identify_dependencies PRD

## Description
Identify dependencies between the decomposed tasks


## Conceptual Info

This node analyzes the decomposed tasks from the 'decompose_objective' node to identify dependencies between them, producing a dependency map.

## Docstring

### Summary
Identify dependencies between decomposed tasks.

### Parameters

- **task_list** (List[str]): List of decomposed tasks or steps from the 'decompose_objective' node.

### Returns

List[str]: List representing the dependency map between tasks.

### Raises

- ValueError: If the task_list is empty or malformed.

### Examples

```python
>>> task_list = ['task1', 'task2', 'task3']
>>> dependency_map = identify_dependencies(task_list)
['task1->task2', 'task2->task3']
```

```python
>>> task_list = ['init', 'process', 'finalize']
>>> dependency_map = identify_dependencies(task_list)
['init->process', 'process->finalize']
```
