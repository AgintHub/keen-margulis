# extract_unique_nodes PRD

## Description
Extracts a list of unique nodes from a given set of dependencies.


## Conceptual Info

The extract_unique_nodes shim function takes a set of dependencies as input and returns a list of unique nodes present in those dependencies.

## Docstring

### Summary
Extracts a list of unique nodes from a given set of dependencies.

### Parameters

- **dependencies** (List[tuple]): A list of tuples, where each tuple represents a dependency between two nodes.

### Returns

List[str]: A list of unique node names extracted from the dependencies.

### Raises

- TypeError: When the input dependencies are not in the expected format.
- ValueError: When the input dependencies are invalid or malformed.

### Examples

```python
>>> dependencies = [('A', 'B'), ('B', 'C'), ('A', 'C')]
>>> extract_unique_nodes(dependencies=dependencies)
['A', 'B', 'C']
```

```python
>>> dependencies = [('Node1', 'Node2'), ('Node2', 'Node3'), ('Node1', 'Node3')]
>>> extract_unique_nodes(dependencies=dependencies)
['Node1', 'Node2', 'Node3']
```
