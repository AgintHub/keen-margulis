# merge_dependency_sources PRD

## Description
Combines semantic and keyword dependency match lists into a single list of dependency tuples.


## Conceptual Info

The function merges two sources of dependency information (semantic and keyword based) to produce a consolidated dependency graph that can be further processed by downstream steps such as duplicate filtering.

## Docstring

### Summary
Merges semantic and keyword dependency lists into a single dependency list.

### Parameters

- **semantic_matches** (List[tuple]): List of dependency pairs detected by semantic analysis. Each pair is a tuple `(parent_task, child_task)`.
- **keyword_matches** (List[tuple]): List of dependency pairs detected by keyword-based analysis. Each pair is a tuple `(parent_task, child_task)`.

### Returns

List[tuple]: A list of unique dependency pairs combining both semantic and keyword sources. The order preserves the original lists' order and removes duplicates.

### Raises

- ValueError: If either `semantic_matches` or `keyword_matches` is empty or not a list.
- TypeError: If the elements of `semantic_matches` or `keyword_matches` are not tuples of length 2.

### Examples

```python
>>> merge_dependency_sources(
...     semantic_matches=[('TaskA', 'TaskB')],
...     keyword_matches=[('TaskB', 'TaskC')]
>>> )
[('TaskA', 'TaskB'), ('TaskB', 'TaskC')]
```

```python
>>> merge_dependency_sources(
...     semantic_matches=[('TaskA', 'TaskB')],
...     keyword_matches=[('TaskA', 'TaskB'), ('TaskC', 'TaskD')]
>>> )
[('TaskA', 'TaskB'), ('TaskC', 'TaskD')]
```
