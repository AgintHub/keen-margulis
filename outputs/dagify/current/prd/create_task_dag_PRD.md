# create_task_dag PRD

## Description
Create a Directed Acyclic Graph (DAG) of tasks.


## Conceptual Info

Builds a topological representation of tasks based on identified dependencies, ensuring no cycles exist and producing an execution order.

## Docstring

### Summary
Constructs a Directed Acyclic Graph (DAG) of tasks from dependency information, returning an ordered list of tasks, the edge list, and an acyclicity flag.

### Parameters

- **task_names** (List[str]): All task identifiers identified from decomposition.
- **dependency_pairs** (List[str]): Dependency relationships in the format 'TaskA -> TaskB', indicating TaskA must complete before TaskB.
- **dependency_count** (int): Total number of dependency relationships identified.

### Returns

Tuple[List[str], List[str], bool]: A tuple containing the ordered list of tasks, the formatted edge list, and a boolean indicating if the DAG is acyclic.

### Raises

- ValueError: If the provided dependencies contain a cycle or if input lists are inconsistent.

### Examples

```python
>>> dag_nodes, dag_edges, is_acyclic = create_task_dag(
    ['A', 'B', 'C'],
    ['A -> B', 'B -> C'],
    2
)
>>> print(dag_nodes, dag_edges, is_acyclic)
(['A', 'B', 'C'], ['A->B', 'B->C'], True)
```

```python
>>> try:
...     create_task_dag(['A', 'B'], ['A -> B', 'B -> A'], 2)
>>> except ValueError as e:
...     print(e)
"Cycle detected in task dependencies: ['A -> B', 'B -> A']"
```
