# calculate_concurrency_stats PRD

## Description
Calculates whether a directed acyclic graph has concurrent tasks and reports the maximum concurrency level based on its topological level structure.


## Conceptual Info

This shim computes concurrency metrics for a DAG, determining if concurrent execution is possible and the maximum number of tasks that can run simultaneously, based on the provided topological level mapping.

## Docstring

### Summary
Determine concurrency availability and maximum concurrency from a DAG's topological level structure.

### Parameters

- **level_structure** (str): JSON string representing a dictionary mapping each node identifier to its topological level (an integer).

### Returns

str: A JSON string containing two keys: 'is_concurrent' (bool) indicating if any level contains more than one node, and 'max_concurrency' (int) representing the highest node count observed across all levels.

### Raises

- ValueError: Raised if the JSON cannot be parsed or required structure is missing.
- TypeError: Raised if the input is not a string.

### Examples

```python
>>> level_structure = '{"A":0, "B":0, "C":1, "D":1}'
>>> print(calculate_concurrency_stats(level_structure))
"{\"is_concurrent\": true, \"max_concurrency\": 2}"
```

```python
>>> level_structure = '{"X":0, "Y":0, "Z":0}'
>>> print(calculate_concurrency_stats(level_structure))
"{\"is_concurrent\": true, \"max_concurrency\": 3}"
```
