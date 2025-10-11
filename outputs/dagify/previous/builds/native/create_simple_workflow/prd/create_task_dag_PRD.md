# create_task_dag PRD

## Description
Create a DAG representing the tasks and their dependencies


## Conceptual Info

Builds a directed acyclic graph (DAG) from a list of task identifiers and dependency relations, producing node identifiers, edge lists, and a validity flag.

## Docstring

### Summary
Constructs a DAG from given tasks and dependency relations.

### Parameters

- **tasks** (List[str]): A list of task identifiers that will become the DAG nodes.
- **dependencies** (List[str]): Each string represents a dependency in the format 'TaskA depends on TaskB'.

### Returns

dict: A dictionary with four keys: task_ids (List[str]), edge_sources (List[str]), edge_destinations (List[str]), and is_valid (bool).

### Raises

- ValueError: Raised when a dependency refers to a task not present in the `tasks` list.
- ValueError: Raised when a dependency string does not match the expected 'TaskA depends on TaskB' pattern.

### Examples

```python
>>> tasks = ['A', 'B', 'C']
>>> dependencies = ['B depends on A', 'C depends on B']
>>> result = create_task_dag(tasks, dependencies)
>>> print(result)
{'task_ids': ['A', 'B', 'C'], 'edge_sources': ['A', 'B'], 'edge_destinations': ['B', 'C'], 'is_valid': True}
```

```python
>>> tasks = ['A', 'B']
>>> dependencies = ['A depends on B', 'B depends on A']
>>> result = create_task_dag(tasks, dependencies)
>>> print(result)
{'task_ids': ['A', 'B'], 'edge_sources': ['B', 'A'], 'edge_destinations': ['A', 'B'], 'is_valid': False}
```
