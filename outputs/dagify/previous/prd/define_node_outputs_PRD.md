# define_node_outputs PRD

## Description
Define the output structure for each node or task


## Conceptual Info

This node defines the output structure for each task or node in the workflow DAG.

## Docstring

### Summary
Defines the output structure for each node based on the decomposed tasks.

### Parameters

- **task_list** (List[str]): List of decomposed tasks or steps from the decompose_objective node.

### Returns

List[str]: A list of output structures for each node in the workflow DAG.

### Raises

- ValueError: If the task_list is empty or not a list.

### Examples

```python
>>> task_list = ['task1', 'task2']
>>> node_outputs = define_node_outputs(task_list)
['{"task": "task1", "output_type": "str"}', '{"task": "task2", "output_type": "int"}']
```

```python
>>> task_list = ['data_ingestion', 'data_processing']
>>> node_outputs = define_node_outputs(task_list)
['{"task": "data_ingestion", "output_type": "DataFrame"}', '{"task": "data_processing", "output_type": "DataFrame"}']
```
