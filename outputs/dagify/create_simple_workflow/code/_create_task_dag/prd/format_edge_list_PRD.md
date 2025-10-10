# format_edge_list PRD

## Description
Formats a list of edge identifiers into a comma-separated string representation.


## Conceptual Info

Converts a list of directed edge identifiers into a compact string for serialization or display, ensuring consistent formatting across the system.

## Docstring

### Summary
Create a comma‑separated string from a list of edge identifiers.

### Parameters

- **edges** (List[str]): A list of edge identifiers to format.

### Returns

str: A single string containing all edge identifiers separated by commas, with no additional whitespace or delimiters.

### Raises

- TypeError: Raised when `edges` is not a list.
- ValueError: Raised when any element in `edges` is not a string.

### Examples

```python
>>> format_edge_list(['taskA', 'taskB', 'taskC'])
'taskA,taskB,taskC'
```

```python
>>> format_edge_list([])
''
```

```python
>>> format_edge_list(['single'])
'single'
```
