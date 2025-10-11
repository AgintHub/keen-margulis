# refine_dag PRD

## Description
Refines an existing task DAG to maximize parallel execution by computing level-wise execution groups, ensuring the graph remains acyclic, and producing metrics that indicate potential concurrency.


## Conceptual Info

This node takes a pre‑built DAG and reorganizes it to expose parallelism while guaranteeing that all dependency constraints are honored and that the graph remains a DAG.

## Docstring

### Summary
Compute level‑based execution plan and concurrency statistics for a task DAG.

### Parameters

- **create_task_dag_input** (CreateTaskDagOutput): Output from the create_task_dag node containing nodes, edges, and acyclicity flag.

### Returns

RefineDagOutput: Refined DAG with reordered edges and concurrency metrics.

### Raises

- ValueError: Raised when the input DAG is empty, malformed, or contains cycles.

### Examples

```python
>>> dag = CreateTaskDagOutput(dag_nodes=['A', 'B', 'C'], dag_edges=['A->C'], is_acyclic=True)
>>> result = refine_dag(dag)
>>> print(result.dag_edges, result.is_acyclic, result.is_concurrent, result.max_concurrency)
['A->C'] True True 2
```
