# create_simple_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'create_simple_workflow' module.

## Table of Contents

- [create_task_dag](#create_task_dag)

- [decompose_objective_into_tasks](#decompose_objective_into_tasks)

- [define_workflow_objective](#define_workflow_objective)

- [finalize_workflow](#finalize_workflow)

- [identify_task_dependencies](#identify_task_dependencies)

- [refine_dag](#refine_dag)



---

## create_task_dag

### Description
Create a Directed Acyclic Graph (DAG) of tasks.

### Conceptual Info

Builds a topological representation of tasks based on identified dependencies, ensuring no cycles exist and producing an execution order.

### Docstring

**Summary:** Constructs a Directed Acyclic Graph (DAG) of tasks from dependency information, returning an ordered list of tasks, the edge list, and an acyclicity flag.

**Parameters:**

- task_names (List[str]): All task identifiers identified from decomposition.
- dependency_pairs (List[str]): Dependency relationships in the format 'TaskA -> TaskB', indicating TaskA must complete before TaskB.
- dependency_count (int): Total number of dependency relationships identified.
**Returns:** Tuple[List[str], List[str], bool] - A tuple containing the ordered list of tasks, the formatted edge list, and a boolean indicating if the DAG is acyclic.

**Raises:**

- ValueError: If the provided dependencies contain a cycle or if input lists are inconsistent.
**Examples:**

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



---

## decompose_objective_into_tasks

### Description
Break down the workflow objective into fundamental tasks.

### Conceptual Info

This node transforms a high‑level workflow goal into a concrete, actionable set of tasks. It interprets the objective text, extracts meaningful sub‑tasks, and returns an ordered list of task names, short descriptions, and the overall count. The decomposition is intentionally kept self‑contained so that downstream nodes can establish dependencies and construct a DAG.

### Docstring

**Summary:** Decomposes a workflow objective string into a list of task names, descriptions, and a task count.

**Parameters:**

- objective (str): Primary goal statement of the workflow provided by `define_workflow_objective`.
**Returns:** tuple[List[str], List[str], int] - A tuple containing: 1) list of task names, 2) list of brief task descriptions, 3) integer count of tasks.

**Raises:**

- ValueError: Raised when the `objective` string is empty or cannot be parsed into distinct tasks.
**Examples:**

```python
>>> result = decompose_objective_into_tasks("Process customer orders and generate invoices")
{'task_names': ['Process orders', 'Generate invoices'], 'task_descriptions': ['Handle incoming orders from sales', 'Create and send invoices to customers'], 'num_tasks': 2}
```

```python
>>> result = decompose_objective_into_tasks("Collect data, clean data, and train a machine learning model")
{'task_names': ['Collect data', 'Clean data', 'Train ML model'], 'task_descriptions': ['Gather raw data from sources', 'Perform data cleaning and preprocessing', 'Train a predictive model on cleaned data'], 'num_tasks': 3}
```



---

## define_workflow_objective

### Description
Define the objective of the workflow

### Conceptual Info

The node captures the high‑level purpose of the entire workflow, producing a single natural‑language sentence that guides downstream task decomposition.

### Docstring

**Summary:** Generate a concise primary goal statement for the workflow.

**Returns:** str - A natural‑language statement describing the workflow’s overall objective.

**Raises:**

- ValueError: If the generated objective is empty or consists only of whitespace.
**Examples:**

```python
>>> # Example 1: Basic workflow objective
>>> objective = define_workflow_objective()
>>> print(objective)
'Automate the ingestion, transformation, and reporting of sales data.'
```

```python
>>> # Example 2: High‑level objective for a data science pipeline
>>> objective = define_workflow_objective()
>>> print(objective)
'Deliver actionable insights from customer behavior data through automated analysis and visualization.'
```



---

## finalize_workflow

### Description
Finalize the workflow DAG

### Conceptual Info

The `finalize_workflow` node validates the refined DAG for completeness, acyclicity, and optimal concurrency. It performs any last‑minute adjustments such as re‑ordering parallel branches or inserting dummy synchronization nodes, and produces a concise summary of the final graph.

### Docstring

**Summary:** Finalize and validate a workflow DAG, ensuring it is complete, concurrent, and acyclic.

**Parameters:**

- dag_edges (List[str]): Directed edges of the refined DAG, formatted as 'TaskA->TaskB'.
- is_acyclic (bool): True if the refined DAG contains no cycles.
- is_concurrent (bool): True if the refined DAG already supports maximum concurrency.
- max_concurrency (int): Maximum number of tasks that can run concurrently in the refined DAG.
**Returns:** dict - A dictionary with keys `dag_is_complete`, `dag_is_concurrent`, `dag_is_acyclic`, `adjusted_node_list`, and `dag_summary`.

**Raises:**

- ValueError: If `dag_edges` is empty or malformed.
- RuntimeError: If the DAG cannot be made acyclic or fully concurrent after adjustments.
**Examples:**

```python
>>> result = finalize_workflow(dag_edges=['A->B', 'B->C'], is_acyclic=True, is_concurrent=False, max_concurrency=2)
>>> print(result)
{'dag_is_complete': True, 'dag_is_concurrent': True, 'dag_is_acyclic': True, 'adjusted_node_list': ['B'], 'dag_summary': 'DAG has 3 nodes and 2 edges. Concurrency adjusted to 2.'}
```

```python
>>> try:
...     finalize_workflow(dag_edges=[], is_acyclic=True, is_concurrent=True, max_concurrency=1)
>>> except ValueError as e:
...     print(e)
'dag_edges list is empty or contains malformed entries.'
```



---

## identify_task_dependencies

### Description
Determines precedence relationships among tasks produced by the decomposition step, producing an explicit list of dependency pairs.

### Conceptual Info

This node takes the set of tasks generated by the decomposition step and infers which tasks must precede others, producing a set of explicit dependency pairs that can be used to construct a DAG.

### Docstring

**Summary:** Identify dependencies between decomposed tasks and return a list of dependency pairs.

**Parameters:**

- task_names (List[str]): Names of the individual tasks produced by the decomposition step.
- task_descriptions (List[str]): Brief textual descriptions of each task corresponding to task_names.
**Returns:** Dict[str, Any] - A dictionary containing three keys:

- 'task_names' (List[str]): The original list of task names.
- 'dependency_pairs' (List[str]): Explicit dependencies formatted as 'TaskA -> TaskB'.
- 'dependency_count' (int): Total number of dependencies identified.

**Raises:**

- ValueError: If task_names and task_descriptions are of different lengths, or if either list is empty.
**Examples:**

```python
>>> task_names = ['Collect Data', 'Clean Data', 'Analyze Data']
>>> task_descriptions = ['Gather raw data', 'Remove noise', 'Run statistical models']
>>> result = identify_task_dependencies(task_names, task_descriptions)
>>> print(result['dependency_pairs'])
['Collect Data -> Clean Data', 'Clean Data -> Analyze Data']
```

```python
>>> task_names = ['Design Model', 'Train Model', 'Validate Model', 'Deploy Model']
>>> task_descriptions = ['Create architecture', 'Fit parameters', 'Evaluate performance', 'Release to production']
>>> result = identify_task_dependencies(task_names, task_descriptions)
>>> print(result['dependency_count'])
3
```



---

## refine_dag

### Description
Refine the DAG to maximize concurrency and ensure acyclicity.

### Conceptual Info

This node takes a previously constructed DAG and optimizes it for maximum concurrent execution by reordering independent tasks and ensuring no cycles.

### Docstring

**Summary:** Optimizes a DAG for maximum concurrency while preserving acyclicity.

**Parameters:**

- dag_nodes (List[str]): Ordered list of task identifiers in the DAG.
- dag_edges (List[str]): List of edges representing dependencies, formatted as "TaskA->TaskB".
- is_acyclic (bool): Indicates whether the input DAG is acyclic.
**Returns:** Tuple[List[str], bool, bool, int] - A tuple containing (refined_dag_edges, is_acyclic, is_concurrent, max_concurrency).

**Raises:**

- ValueError: Raised if dag_edges is empty or if the input graph is cyclic.
**Examples:**

```python
>>> dag_nodes = ['A', 'B', 'C'],
>>> dag_edges = ['A->B', 'B->C'],
>>> is_acyclic = True,
>>> refined = refine_dag(dag_nodes, dag_edges, is_acyclic),
>>> print(refined)
(['A->B', 'B->C'], True, False, 1)
```

```python
>>> dag_nodes = ['A', 'B', 'C'],
>>> dag_edges = ['A->C'],
>>> is_acyclic = True,
>>> refined = refine_dag(dag_nodes, dag_edges, is_acyclic),
>>> print(refined)
(['A->C'], True, True, 2)
```

