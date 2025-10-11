# define_workflow_objective PRD

## Description
Define the objective of the workflow


## Conceptual Info

The node captures the high‑level purpose of the entire workflow, producing a single natural‑language sentence that guides downstream task decomposition.

## Docstring

### Summary
Generate a concise primary goal statement for the workflow.

### Returns

str: A natural‑language statement describing the workflow’s overall objective.

### Raises

- ValueError: If the generated objective is empty or consists only of whitespace.

### Examples

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
