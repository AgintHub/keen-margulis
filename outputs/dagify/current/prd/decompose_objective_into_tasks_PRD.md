# decompose_objective_into_tasks PRD

## Description
Captures the high‑level purpose of a workflow as a single natural‑language sentence, ensuring clarity and consistency for downstream decomposition.


## Conceptual Info

This node serves as the foundational description of a workflow. By accepting a human‑friendly prompt and validating it, it guarantees that downstream nodes start from a well‑formed objective, reducing ambiguity and improving maintainability.

## Docstring

### Summary
Return a validated objective string.

### Parameters

- **general_input** (str): Human‑readable description of the desired workflow.

### Returns

DefineWorkflowObjectiveOutput: A pydantic model containing the validated objective.

### Raises

- ValueError: If the input is empty, non‑string, or only whitespace.

### Examples

```python
>>> from your_package import define_workflow_objective
>>> objective_output = define_workflow_objective("Automate the ingestion, transformation, and reporting of sales data.")
>>> print(objective_output.objective)
"Automate the ingestion, transformation, and reporting of sales data."
```
