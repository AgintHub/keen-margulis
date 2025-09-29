# extract_black_pieces PRD

## Description
Extracts black piece positions from a list of chess piece positions.


## Conceptual Info

This shim isolates the logic for filtering black chess pieces from a given set of piece positions, allowing the rest of the material balance evaluation to operate on a clean subset of data.

## Docstring

### Summary
Extracts the positions of all black pieces from the given list of chess piece positions.

### Parameters

- **piece_positions** (List[str]): A list of chess piece position strings, e.g., ['e4', 'B5', 'c6', 'D1'].

### Returns

List[str]: A list containing only the positions of black pieces.

### Raises

- TypeError: Raised when `piece_positions` is not a list or contains non-string elements.
- ValueError: Raised when any element in `piece_positions` is an empty string or does not conform to expected format.

### Examples

```python
>>> extract_black_pieces(['e4', 'B5', 'c6', 'D1'])
['e4', 'c6']
```

```python
>>> extract_black_pieces([])
[]
```
