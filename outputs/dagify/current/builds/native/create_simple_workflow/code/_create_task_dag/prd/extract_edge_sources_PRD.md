# extract_edge_sources PRD

## Description
Extracts a list of source task identifiers from a string representation of parsed dependency pairs.


## Conceptual Info

The shim isolates the logic for extracting source task names from a dependency string, enabling reuse in DAG construction and simplifying unit tests.

## Docstring

### Summary
Parse a string of dependency tuples and return the list of source task identifiers.

### Parameters

- **parsed_dependencies** (str): A string containing comma‑separated tuples in the form "('TaskA', 'TaskB'), ('TaskC', 'TaskD')" or a similar format where each tuple represents a dependency "source" → "destination".

### Returns

List[str]: A list of the source task identifiers extracted from each dependency tuple.

### Raises

- TypeError: If `parsed_dependencies` is not a string.
- ValueError: If the input string cannot be parsed into a sequence of valid two‑element tuples or if any tuple is malformed.

### Examples

```python
>>> output = extract_edge_sources("('TaskA', 'TaskB'), ('TaskC', 'TaskD')")
['TaskA', 'TaskC']
```

```python
>>> output = extract_edge_sources("('Deploy', 'Test'), ('Build', 'Deploy')")
['Deploy', 'Build']
```
