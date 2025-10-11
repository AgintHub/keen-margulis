# define_workflow_objective PRD

## Description
Creates a clear, single-sentence statement that defines the primary goal of the entire workflow, serving as a guiding beacon for downstream task decomposition.


## Conceptual Info

Captures the high-level purpose of the workflow in a single natural-language sentence, ensuring all downstream tasks align with a clear, actionable goal.

## Docstring

### Summary
Defines the workflow’s primary objective statement.

### Parameters

- **general_input** (str): High‑level description or context used to generate the objective.

### Returns

DefineWorkflowObjectiveOutput: Object containing the primary goal sentence.

### Raises

- ValueError: If the input is empty or consists only of whitespace.

### Examples

```python
>>> output = define_workflow_objective("automate data ingestion and reporting")
>>> print(output.objective)
"The primary objective of this workflow is to automate data ingestion and reporting."
```
