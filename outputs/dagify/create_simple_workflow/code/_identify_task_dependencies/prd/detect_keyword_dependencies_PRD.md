# detect_keyword_dependencies PRD

## Description
Detect keyword-based dependencies between tasks by analyzing task names and descriptions.


## Conceptual Info

This shim identifies implicit task dependencies by matching keyword patterns in task descriptions, returning ordered pairs of task names that indicate a prerequisite relationship.

## Docstring

### Summary
Detect keyword-based dependencies between two lists of task names and descriptions.

### Parameters

- **task_names** (List[str]): List of task names to analyze.
- **descriptions** (List[str]): Corresponding list of natural‑language descriptions for each task.

### Returns

List[tuple]: A list of tuples (predecessor_task, dependent_task) representing dependencies inferred from keyword matches.

### Raises

- ValueError: Raised when either input list is empty or the two lists have differing lengths.
- TypeError: Raised when input types are not lists of strings or contain non-string elements.

### Examples

```python
>>> detect_keyword_dependencies(['Clean data', 'Analyze data'], ['Clean the raw data before analysis', 'Analyze the cleaned data'])
[('Clean data', 'Analyze data')]
```

```python
>>> detect_keyword_dependencies(['Read book', 'Write summary'], ['Read the book', 'Write a summary of the book'])
[]
```
