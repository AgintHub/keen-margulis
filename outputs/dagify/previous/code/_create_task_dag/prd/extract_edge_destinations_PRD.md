# extract_edge_destinations PRD

## Description
Extracts the destination task identifiers from a string representation of parsed dependency tuples.


## Conceptual Info

This shim serves as the bridge between parsed dependency data and the DAG construction logic by isolating the extraction of destination nodes from dependency tuples.

## Docstring

### Summary
Extracts destination task identifiers from a string representation of parsed dependency tuples.

### Parameters

- **parsed_dependencies** (str): String representation of parsed dependency tuples, each tuple containing a source and destination task identifier.

### Returns

LIST_STR: A list of destination task identifiers (e.g., ['TaskB', 'TaskC']) extracted from the parsed dependencies.

### Raises

- ValueError: Raised when the input string cannot be parsed into a list of tuple pairs.
- TypeError: Raised when the input is not a string.

### Examples

```python
>>> deps = "[(\'TaskA\', \'TaskB\'), (\'TaskB\', \'TaskC\')]"
>>> print(extract_edge_destinations(deps))
['TaskB', 'TaskC']
```

```python
>>> deps = "[]"
>>> print(extract_edge_destinations(deps))
[]
```
