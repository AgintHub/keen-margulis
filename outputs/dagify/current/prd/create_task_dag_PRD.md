# create_task_dag PRD

## Description
Constructs a directed acyclic graph (DAG) from explicit dependency pairs, performs a topological sort to produce a deterministic execution order, and validates that the graph contains no cycles. The node returns the ordered task list, the dependency edge list in compact form, and a boolean flag indicating acyclicity.


## Conceptual Info

Builds a topological representation of tasks based on identified dependencies, ensuring no cycles exist and producing an execution order.

## Docstring

### Summary
Creates a DAG from dependency pairs and returns an execution order.

### Parameters

- **identify_task_dependencies_input** (IdentifyTaskDependenciesOutput): Output from the identify_task_dependencies node containing task names and dependency pairs.
- **kwargs** (dict): Additional keyword arguments for future extensions.

### Returns

CreateTaskDagOutput: Dataclass containing the ordered task list, edge list, and acyclicity flag.

### Raises

- ValueError: If input validation fails or a cycle is detected in the dependency graph.

### Examples

```python
>>> from your_module import create_task_dag, IdentifyTaskDependenciesOutput
>>> input_data = IdentifyTaskDependenciesOutput(
...     task_names=["A", "B", "C"],
...     dependency_pairs=["A -> B", "B -> C"],
...     dependency_count=2
>>> )
>>> output = create_task_dag(input_data)
>>> print(output.dag_nodes, output.dag_edges, output.is_acyclic)
["A", "B", "C"] ['A->B', 'B->C'] True
```
