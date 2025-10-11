# validate_dag_edges PRD

## Description
Validates a list of directed edges for syntax, uniqueness, and acyclicity, returning a cleaned list of edges.


## Conceptual Info

The validate_dag_edges shim ensures that the edges supplied to the workflow refinement process conform to the expected syntax and represent an acyclic graph, providing a safe set of edges for subsequent processing.

## Docstring

### Summary
Validate a list of directed edges, ensuring each edge is formatted correctly, unique, and that the resulting graph is acyclic. Returns a cleaned list of edges or raises an error if validation fails.

### Parameters

- **edges** (list[str]): A list of edge strings formatted as 'NodeA->NodeB'.
- **logger** (logging.Logger): Logger instance used for debug and error logging.

### Returns

List[str]: A list of validated edge strings, deduplicated and in the same order as the first appearance.

### Raises

- ValueError: Raised when an edge is malformed, refers to an undefined node, or if the edge set introduces a cycle.
- TypeError: Raised when the `edges` argument is not a list of strings or the `logger` is not a logging.Logger instance.

### Examples

```python
>>> edges = ['Task1->Task2', 'Task2->Task3']
>>> validated = validate_dag_edges(edges, logger)
>>> print(validated)
['Task1->Task2', 'Task2->Task3']
```

```python
>>> edges = ['Task1->Task2', 'Task2->Task1']
>>> validate_dag_edges(edges, logger)
ValueError: Cyclic dependency detected in edges.
```
