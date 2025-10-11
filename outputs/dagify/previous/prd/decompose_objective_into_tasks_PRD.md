# decompose_objective_into_tasks PRD

## Description
Break down the workflow objective into fundamental tasks.


## Conceptual Info

This node transforms a high‑level workflow goal into a concrete, actionable set of tasks. It interprets the objective text, extracts meaningful sub‑tasks, and returns an ordered list of task names, short descriptions, and the overall count. The decomposition is intentionally kept self‑contained so that downstream nodes can establish dependencies and construct a DAG.

## Docstring

### Summary
Decomposes a workflow objective string into a list of task names, descriptions, and a task count.

### Parameters

- **objective** (str): Primary goal statement of the workflow provided by `define_workflow_objective`.

### Returns

tuple[List[str], List[str], int]: A tuple containing: 1) list of task names, 2) list of brief task descriptions, 3) integer count of tasks.

### Raises

- ValueError: Raised when the `objective` string is empty or cannot be parsed into distinct tasks.

### Examples

```python
>>> result = decompose_objective_into_tasks("Process customer orders and generate invoices")
{'task_names': ['Process orders', 'Generate invoices'], 'task_descriptions': ['Handle incoming orders from sales', 'Create and send invoices to customers'], 'num_tasks': 2}
```

```python
>>> result = decompose_objective_into_tasks("Collect data, clean data, and train a machine learning model")
{'task_names': ['Collect data', 'Clean data', 'Train ML model'], 'task_descriptions': ['Gather raw data from sources', 'Perform data cleaning and preprocessing', 'Train a predictive model on cleaned data'], 'num_tasks': 3}
```
