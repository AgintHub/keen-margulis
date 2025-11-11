# create_dag_structure PRD

## Description
Create the DAG structure based on the subtasks and their dependencies.


## Conceptual Info

Constructs a Directed Acyclic Graph (DAG) from given subtasks and their dependencies.

## Docstring

### Summary
Creates a DAG structure based on subtasks and their dependencies.

### Parameters

- **subtasks** (List[str]): List of subtask names.
- **dependencies** (List[str]): List of dependencies between subtasks, where each dependency is represented as 'subtask_id_1 -> subtask_id_2'.

### Returns

{dag_nodes: List[str], dag_edges: List[str], root_nodes: List[str], is_valid_dag: bool}: A dictionary containing the DAG nodes, edges, root nodes, and a flag indicating whether the DAG is valid.

### Raises

- ValueError: If the dependencies form a cycle, making it impossible to create a valid DAG.

### Examples

```python
>>> subtasks = ['A', 'B', 'C']
>>> dependencies = ['A -> B', 'B -> C']
>>> create_dag_structure(subtasks, dependencies)
{'dag_nodes': ['A', 'B', 'C'], 'dag_edges': ['A->B', 'B->C'], 'root_nodes': ['A'], 'is_valid_dag': True}
```
