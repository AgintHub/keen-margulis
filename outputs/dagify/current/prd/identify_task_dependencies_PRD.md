# identify_task_dependencies PRD

## Description
Generates an ordered dependency list by detecting references between task descriptions, supporting downstream DAG construction.


## Conceptual Info

This node analyzes the semantic content of task descriptions to discover logical precedence. It supports automated workflow generation by turning free‑form text into a deterministic DAG.

## Docstring

### Summary
Detects precedence relationships among decomposed tasks using text‑matching heuristics.

### Parameters

- **decompose_objective_into_tasks_input** (DecomposeObjectiveIntoTasksOutput): Pydantic model containing task names and their descriptions.

### Returns

IdentifyTaskDependenciesOutput: Model with the original task list, a list of dependency pairs, and their count.

### Raises

- ValueError: If input lists are empty or mis‑aligned.

### Examples

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
