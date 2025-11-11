# format_digraph PRD

## Description
Formats the given edges into a digraph structure.


## Conceptual Info

This shim function is responsible for taking a list of edges representing a directed graph and formatting them into a string that represents the digraph structure.

## Docstring

### Summary
Formats the given edges into a digraph structure represented as a string.

### Parameters

- **edges** (str): A string representing the edges of the digraph, expected to be in a format that can be processed into a digraph structure.

### Returns

str: A string representing the formatted digraph structure.

### Raises

- ValueError: If the input edges cannot be properly formatted into a digraph.
- TypeError: If the input edges are not of the expected type.

### Examples

```python
>>> format_digraph(edges='A->B;B->C')
'digraph { A -> B; B -> C }'
```

```python
>>> format_digraph(edges='X->Y;Y->Z;Z->X')
'digraph { X -> Y; Y -> Z; Z -> X }'
```
