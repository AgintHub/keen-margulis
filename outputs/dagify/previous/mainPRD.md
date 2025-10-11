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
Constructs a directed acyclic graph (DAG) from explicit dependency pairs, performs a topological sort to produce a deterministic execution order, and validates that the graph contains no cycles. The node returns the ordered task list, the dependency edge list in compact form, and a boolean flag indicating acyclicity.

### Conceptual Info

Builds a topological representation of tasks based on identified dependencies, ensuring no cycles exist and producing an execution order.

### Docstring

**Summary:** Creates a DAG from dependency pairs and returns an execution order.

**Parameters:**

- identify_task_dependencies_input (IdentifyTaskDependenciesOutput): Output from the identify_task_dependencies node containing task names and dependency pairs.
- kwargs (dict): Additional keyword arguments for future extensions.
**Returns:** CreateTaskDagOutput - Dataclass containing the ordered task list, edge list, and acyclicity flag.

**Raises:**

- ValueError: If input validation fails or a cycle is detected in the dependency graph.
**Examples:**

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



---

## decompose_objective_into_tasks

### Description
Captures the high‑level purpose of a workflow as a single natural‑language sentence, ensuring clarity and consistency for downstream decomposition.

### Conceptual Info

This node serves as the foundational description of a workflow. By accepting a human‑friendly prompt and validating it, it guarantees that downstream nodes start from a well‑formed objective, reducing ambiguity and improving maintainability.

### Docstring

**Summary:** Return a validated objective string.

**Parameters:**

- general_input (str): Human‑readable description of the desired workflow.
**Returns:** DefineWorkflowObjectiveOutput - A pydantic model containing the validated objective.

**Raises:**

- ValueError: If the input is empty, non‑string, or only whitespace.
**Examples:**

```python
>>> from your_package import define_workflow_objective
>>> objective_output = define_workflow_objective("Automate the ingestion, transformation, and reporting of sales data.")
>>> print(objective_output.objective)
"Automate the ingestion, transformation, and reporting of sales data."
```



---

## define_workflow_objective

### Description
Creates a clear, single-sentence statement that defines the primary goal of the entire workflow, serving as a guiding beacon for downstream task decomposition.

### Conceptual Info

Captures the high-level purpose of the workflow in a single natural-language sentence, ensuring all downstream tasks align with a clear, actionable goal.

### Docstring

**Summary:** Defines the workflow’s primary objective statement.

**Parameters:**

- general_input (str): High‑level description or context used to generate the objective.
**Returns:** DefineWorkflowObjectiveOutput - Object containing the primary goal sentence.

**Raises:**

- ValueError: If the input is empty or consists only of whitespace.
**Examples:**

```python
>>> output = define_workflow_objective("automate data ingestion and reporting")
>>> print(output.objective)
"The primary objective of this workflow is to automate data ingestion and reporting."
```



---

## finalize_workflow

### Description
Validates the refined DAG, ensures completeness, acyclicity, and optimal concurrency, performs any last‑minute adjustments, and returns a concise summary.

### Conceptual Info

The finalize_workflow node is the final validation step in a workflow DAG pipeline. It verifies that the DAG is fully defined, contains no cycles, and is configured for maximum concurrency. If any of these properties are not satisfied, the node records the adjustments it would perform, such as adding a dummy synchronization node or a cycle‑breaking node, and logs the outcome. The node produces a summary that is useful for monitoring and debugging downstream processes.

### Docstring

**Summary:** Finalizes and validates a workflow DAG, performing any necessary adjustments and returning key status flags and a summary.

**Parameters:**

- refine_dag_input (RefineDagOutput): Output from the refine_dag node containing the refined edges, acyclicity flag, concurrency flag, and maximum concurrency count.
**Returns:** FinalizeWorkflowOutput - An object containing completion, concurrency, acyclicity status, list of adjusted nodes, and a textual summary.

**Raises:**

- ValueError: If dag_edges is empty or contains malformed entries.
**Examples:**

```python
>>> from pydantic import BaseModel, Field
>>> from typing import List
>>> class RefineDagOutput(BaseModel):
...     dag_edges: List[str] = Field(..., description="List of directed edges in the refined DAG, formatted as 'TaskA->TaskB'.")
...     is_acyclic: bool = Field(..., description="Indicates whether the refined DAG contains any cycles.")
...     is_concurrent: bool = Field(..., description="Indicates whether the DAG has been adjusted to allow concurrent execution of independent tasks.")
...     max_concurrency: int = Field(..., description="Maximum number of tasks that can run concurrently in the refined DAG.")
>>> class FinalizeWorkflowOutput(BaseModel):
...     dag_is_complete: bool = Field(..., description="Whether the DAG is fully defined and ready")
...     dag_is_concurrent: bool = Field(..., description="Whether the DAG has maximized concurrency")
...     dag_is_acyclic: bool = Field(..., description="Whether the DAG contains no cycles")
...     adjusted_node_list: str = Field(..., description="Comma‑separated list of node names that were adjusted during finalization")
...     dag_summary: str = Field(..., description="Human‑readable summary of the finalized DAG")
>>> def finalize_workflow(refine_dag_input: RefineDagOutput, **kwargs) -> FinalizeWorkflowOutput:
...     import logging
...     import re
...     logger = logging.getLogger(__name__)
...     if not refine_dag_input.dag_edges:
...         logger.error("dag_edges list is empty")
...         raise ValueError("dag_edges list is empty or contains malformed entries")
...     edge_pattern = re.compile(r'^\s*([^\s]+)\s*->\s*([^\s]+)\s*$')
...     nodes = set()
...     for edge in refine_dag_input.dag_edges:
...         m = edge_pattern.match(edge)
...         if not m:
...             logger.error("malformed edge: %s", edge)
...             raise ValueError("dag_edges list is empty or contains malformed entries")
...         src, dst = m.group(1), m.group(2)
...         nodes.update([src, dst])
...     node_count = len(nodes)
...     edge_count = len(refine_dag_input.dag_edges)
...     dag_is_complete = node_count > 0 and edge_count > 0
...     dag_is_concurrent = refine_dag_input.is_concurrent
...     dag_is_acyclic = refine_dag_input.is_acyclic
...     adjusted = []
...     if not dag_is_concurrent:
...         adjusted.append("SyncNode")
...     if not dag_is_acyclic:
...         adjusted.append("CycleBreaker")
...     adjusted_node_list = ",".join(adjusted)
...     dag_summary = f"DAG has {node_count} nodes and {edge_count} edges. Acyclic: {dag_is_acyclic}. Concurrency: {'maximized' if dag_is_concurrent else 'not maximized'}."
...     return FinalizeWorkflowOutput(
...         dag_is_complete=dag_is_complete,
...         dag_is_concurrent=dag_is_concurrent,
...         dag_is_acyclic=dag_is_acyclic,
...         adjusted_node_list=adjusted_node_list,
...         dag_summary=dag_summary
...     )
>>> # Example usage:
>>> refine_output = RefineDagOutput(dag_edges=['A->B', 'B->C'], is_acyclic=True, is_concurrent=False, max_concurrency=2)
>>> result = finalize_workflow(refine_output)
>>> print(result.dag_summary)
DAG has 3 nodes and 2 edges. Acyclic: True. Concurrency: not maximized.
```



---

## identify_task_dependencies

### Description
Generates an ordered dependency list by detecting references between task descriptions, supporting downstream DAG construction.

### Conceptual Info

This node analyzes the semantic content of task descriptions to discover logical precedence. It supports automated workflow generation by turning free‑form text into a deterministic DAG.

### Docstring

**Summary:** Detects precedence relationships among decomposed tasks using text‑matching heuristics.

**Parameters:**

- decompose_objective_into_tasks_input (DecomposeObjectiveIntoTasksOutput): Pydantic model containing task names and their descriptions.
**Returns:** IdentifyTaskDependenciesOutput - Model with the original task list, a list of dependency pairs, and their count.

**Raises:**

- ValueError: If input lists are empty or mis‑aligned.
**Examples:**

```python
>>> from typing import List
>>> class DecomposeObjectiveIntoTasksOutput(BaseModel):
...     task_names: List[str]
...     task_descriptions: List[str]
...     num_tasks: int
>>> class IdentifyTaskDependenciesOutput(BaseModel):
...     task_names: List[str]
...     dependency_pairs: List[str]
...     dependency_count: int
>>> input_data = DecomposeObjectiveIntoTasksOutput(**{
...     'task_names': ['Collect Data', 'Clean Data', 'Analyze Data'],
...     'task_descriptions': ['Gather raw data', 'Remove noise from collected data', 'Run statistical models on cleaned data'],
...     'num_tasks': 3
>>> })
>>> output = identify_task_dependencies(input_data)
>>> print(output.dependency_pairs)
['Collect Data -> Clean Data', 'Clean Data -> Analyze Data']
```



---

## refine_dag

### Description
Refines an existing task DAG to maximize parallel execution by computing level-wise execution groups, ensuring the graph remains acyclic, and producing metrics that indicate potential concurrency.

### Conceptual Info

This node takes a pre‑built DAG and reorganizes it to expose parallelism while guaranteeing that all dependency constraints are honored and that the graph remains a DAG.

### Docstring

**Summary:** Compute level‑based execution plan and concurrency statistics for a task DAG.

**Parameters:**

- create_task_dag_input (CreateTaskDagOutput): Output from the create_task_dag node containing nodes, edges, and acyclicity flag.
**Returns:** RefineDagOutput - Refined DAG with reordered edges and concurrency metrics.

**Raises:**

- ValueError: Raised when the input DAG is empty, malformed, or contains cycles.
**Examples:**

```python
>>> dag = CreateTaskDagOutput(dag_nodes=['A', 'B', 'C'], dag_edges=['A->C'], is_acyclic=True)
>>> result = refine_dag(dag)
>>> print(result.dag_edges, result.is_acyclic, result.is_concurrent, result.max_concurrency)
['A->C'] True True 2
```

