# identify_validation_issues PRD

## Description
This shim function identifies validation issues based on the DAG structure validation result, prompt quality score, and description completeness score.


## Conceptual Info

The identify_validation_issues shim plays a crucial role in the workflow validation process by analyzing the DAG structure, prompt quality, and description completeness to identify potential issues.

## Docstring

### Summary
Identifies validation issues based on the DAG structure validation result, prompt quality score, and description completeness score.

### Parameters

- **dag_valid** (str): A string indicating whether the DAG structure is valid.
- **prompt_score** (str): A string representing the prompt quality score.
- **description_score** (str): A string representing the description completeness score.

### Returns

List[str]: A list of strings representing the validation issues found.

### Raises

- ValueError: If the input parameters are invalid or inconsistent.
- TypeError: If the input parameters are of incorrect type.

### Examples

```python
>>> validation_issues = identify_validation_issues(dag_valid='True', prompt_score='0.8', description_score='0.9')
['No issues found']
```

```python
>>> validation_issues = identify_validation_issues(dag_valid='False', prompt_score='0.2', description_score='0.1')
['DAG structure is invalid', 'Prompt quality score is low', 'Description completeness score is low']
```
