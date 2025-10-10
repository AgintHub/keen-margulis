# create_simple_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'create_simple_workflow' module.

## Table of Contents

- [create_task_dag](#create_task_dag)

- [decompose_objective_into_tasks](#decompose_objective_into_tasks)

- [define_workflow_objective](#define_workflow_objective)

- [finalize_workflow](#finalize_workflow)

- [identify_task_dependencies](#identify_task_dependencies)

- [validate_dag](#validate_dag)



---

## create_task_dag

### Description
Create a DAG representing the tasks and their dependencies

### Conceptual Info

Builds a directed acyclic graph (DAG) from a list of task identifiers and dependency relations, producing node identifiers, edge lists, and a validity flag.

### Docstring

**Summary:** Constructs a DAG from given tasks and dependency relations.

**Parameters:**

- tasks (List[str]): A list of task identifiers that will become the DAG nodes.
- dependencies (List[str]): Each string represents a dependency in the format 'TaskA depends on TaskB'.
**Returns:** dict - A dictionary with four keys: task_ids (List[str]), edge_sources (List[str]), edge_destinations (List[str]), and is_valid (bool).

**Raises:**

- ValueError: Raised when a dependency refers to a task not present in the `tasks` list.
- ValueError: Raised when a dependency string does not match the expected 'TaskA depends on TaskB' pattern.
**Examples:**

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



---

## decompose_objective_into_tasks

### Description
Break down the workflow objective into individual tasks

### Conceptual Info

Transforms a high‑level workflow goal into a concrete sequence of actionable tasks, enabling downstream dependency analysis and DAG construction.

### Docstring

**Summary:** Breaks down a workflow objective into discrete tasks.

**Parameters:**

- workflow_objective (str): A concise statement describing the primary goal of the workflow.
**Returns:** Tuple[List[str], int] - A tuple containing (1) a list of task descriptions and (2) the count of tasks.

**Raises:**

- ValueError: Raised when `workflow_objective` is empty or consists only of whitespace.
**Examples:**

```python
>>> tasks, count = decompose_objective_into_tasks('Build a machine learning pipeline for predicting house prices')
(['Collect and clean data', 'Split dataset', 'Select model', 'Train model', 'Evaluate model', 'Deploy model'], 6)
```

```python
>>> tasks, count = decompose_objective_into_tasks('Write a report')
(['Plan report structure', 'Collect data', 'Write draft', 'Revise', 'Finalize'], 5)
```



---

## define_workflow_objective

### Description
Define the objective of the workflow

### Conceptual Info

Captures the high‑level purpose of the workflow, providing a clear goal that drives the subsequent task decomposition, dependency analysis, and DAG construction.

### Docstring

**Summary:** Generate a concise objective statement for the workflow based on the user’s intent.

**Returns:** str - Concise objective of the workflow.

**Raises:**

- ValueError: If the generated objective is empty or exceeds an acceptable length.
**Examples:**

```python
>>> objective = define_workflow_objective()
'Implement an automated data ingestion pipeline for real‑time analytics'
```

```python
>>> objective = define_workflow_objective()
'Develop a user‑friendly mobile application for inventory management'
```



---

## finalize_workflow

### Description
Finalize the workflow DAG

### Conceptual Info

The finalize_workflow node takes a validated DAG, checks for any remaining inconsistencies such as missing dependencies or cycles, applies necessary adjustments, and produces a clean, ordered representation ready for execution.

### Docstring

**Summary:** Finalize a workflow DAG by validating its structure, resolving missing dependencies, removing cycles, and ordering tasks.

**Parameters:**

- task_ids (List[str]): Unique identifiers of all tasks in the DAG.
- edge_sources (List[str]): Source task identifiers for each directed edge.
- edge_destinations (List[str]): Destination task identifiers for each directed edge.
- is_valid (bool): Result of the validation step (True if the DAG passed all checks).
- node_count (int): Total number of nodes in the DAG.
- edge_count (int): Total number of directed edges in the DAG.
- cycles_detected (List[str]): List of cycle identifiers found during validation.
- missing_dependencies (List[str]): List of node names that reference non‑existent dependencies.
- errors (List[str]): Detailed error messages from the validation step.
**Returns:** Dict[str, Any] - A dictionary containing the finalized DAG representation and metadata: dag_representation (str), is_valid (bool), adjustments_made (bool), adjusted_task_order (List[str]), missing_dependencies (List[str]), cycles_detected (List[str]), warnings (List[str]), and summary (str).

**Raises:**

- ValueError: If any required input lists are empty or lengths of edge_sources and edge_destinations mismatch.
**Examples:**

```python
>>> dag = finalize_workflow(

...     task_ids=['A', 'B', 'C'],

...     edge_sources=['A', 'B'],

...     edge_destinations=['B', 'C'],

...     is_valid=True,

...     node_count=3,

...     edge_count=2,

...     cycles_detected=[],

...     missing_dependencies=[],

...     errors=[]

>>> )
{'dag_representation': 'A -> B -> C', 'is_valid': True, 'adjustments_made': False, 'adjusted_task_order': ['A', 'B', 'C'], 'missing_dependencies': [], 'cycles_detected': [], 'warnings': [], 'summary': 'DAG finalized successfully.'}
```

```python
>>> dag = finalize_workflow(

...     task_ids=['A', 'B', 'C'],

...     edge_sources=['A', 'B', 'C'],

...     edge_destinations=['B', 'C', 'A'],

...     is_valid=False,

...     node_count=3,

...     edge_count=3,

...     cycles_detected=['A->B->C->A'],

...     missing_dependencies=[],

...     errors=['Cycle detected']

>>> )
{'dag_representation': 'A -> B -> C', 'is_valid': False, 'adjustments_made': True, 'adjusted_task_order': ['A', 'B', 'C'], 'missing_dependencies': [], 'cycles_detected': ['A->B->C->A'], 'warnings': ['Cycle removed: A->B->C->A'], 'summary': 'DAG finalized with cycle removal.'}
```



---

## identify_task_dependencies

### Description
Identify dependencies between tasks

### Conceptual Info

This node processes a list of task descriptions produced by the decomposition step and infers direct dependencies between tasks. It returns the original list of tasks, a concise list of dependency strings, and a flag indicating whether any dependencies exist.

### Docstring

**Summary:** Infers direct dependencies between tasks from a list of task descriptions.

**Parameters:**

- tasks (List[str]): Task descriptions generated by decompose_objective_into_tasks.
**Returns:** Dict[str, Any] - A dictionary with keys 'tasks', 'dependencies', and 'dependency_exists' matching the node's output structure.

**Raises:**

- ValueError: If the input `tasks` is not a list of strings or is empty.
**Examples:**

```python
>>> tasks_input = ["Collect data", "Preprocess data", "Train model", "Evaluate model"]
>>> # Assuming the following simple dependency logic:
>>> # 'Preprocess data' depends on 'Collect data'
>>> # 'Train model' depends on 'Preprocess data'
>>> # 'Evaluate model' depends on 'Train model'
>>> result = identify_task_dependencies(tasks_input)
>>> print(result)
{'tasks': ['Collect data', 'Preprocess data', 'Train model', 'Evaluate model'], 'dependencies': ['Preprocess data depends on Collect data', 'Train model depends on Preprocess data', 'Evaluate model depends on Train model'], 'dependency_exists': True}
```

```python
>>> tasks_input = ["Generate report", "Publish report"]
>>> # No explicit dependencies specified
>>> result = identify_task_dependencies(tasks_input)
>>> print(result)
{'tasks': ['Generate report', 'Publish report'], 'dependencies': [], 'dependency_exists': False}
```



---

## validate_dag

### Description
Validate the created DAG for correctness and acyclicity

### Conceptual Info

The `validate_dag` node verifies that a workflow DAG is well‑formed, acyclic, and internally consistent. It acts as a safety net before the workflow is finalized, catching missing dependencies and logical cycles that could cause runtime failures.

### Docstring

**Summary:** Validates a Directed Acyclic Graph (DAG) representation for correctness, acyclicity, and missing dependencies.

**Parameters:**

- task_ids (List[str]): List of unique identifiers for all tasks in the workflow.
- edge_sources (List[str]): List of task identifiers representing the source of each directed edge.
- edge_destinations (List[str]): List of task identifiers representing the destination of each directed edge.
- is_valid_input (bool): (Optional) A flag from `create_task_dag` indicating preliminary validity. It is used only as a hint; full validation is performed regardless.
**Returns:** dict - Dictionary containing validation results:
- `is_valid` (bool): Overall validity.
- `node_count` (int): Number of nodes.
- `edge_count` (int): Number of directed edges.
- `cycles_detected` (List[str]): Descriptions of any detected cycles.
- `missing_dependencies` (List[str]): Tasks that reference undefined dependencies.
- `errors` (List[str]): Human‑readable error messages for all failures.

**Raises:**

- ValueError: If `edge_sources` and `edge_destinations` lists are not of the same length.
- ValueError: If `task_ids` contains duplicate identifiers.
**Examples:**

```python
>>> task_ids = ['A', 'B', 'C']
>>> edge_sources = ['A', 'B']
>>> edge_destinations = ['B', 'C']
>>> result = validate_dag(task_ids, edge_sources, edge_destinations)
>>> print(result)
{'is_valid': True, 'node_count': 3, 'edge_count': 2, 'cycles_detected': [], 'missing_dependencies': [], 'errors': []}
```

```python
>>> task_ids = ['A', 'B', 'C']
>>> edge_sources = ['A', 'B', 'C']
>>> edge_destinations = ['B', 'C', 'A']
>>> result = validate_dag(task_ids, edge_sources, edge_destinations)
>>> print(result)
{'is_valid': False, 'node_count': 3, 'edge_count': 3, 'cycles_detected': ['A -> B -> C -> A'], 'missing_dependencies': [], 'errors': ['Cycle detected: A -> B -> C -> A']}
```

