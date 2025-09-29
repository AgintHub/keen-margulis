# extract_white_pieces PRD

## Description
Extracts and returns a list of white piece identifiers from a list of chess piece positions.


## Conceptual Info

This shim isolates the logic for filtering white chess pieces from a mixed list of piece positions, enabling downstream evaluation nodes to work with a clean subset.

## Docstring

### Summary
Return a list of chess piece positions that represent white pieces.

### Parameters

- **piece_positions** (List[str]): A list of strings where each string encodes a board square followed by a piece identifier (e.g., 'e4N', 'd3q'). White pieces are represented by uppercase letters.

### Returns

List[str]: All input strings whose piece identifier is uppercase, preserving the original order.

### Raises

- ValueError: If any element of `piece_positions` is not a string or does not contain at least a file, rank, and a piece identifier.
- TypeError: If `piece_positions` is not a list or its elements are not strings.

### Examples

```python
>>> extract_white_pieces(['e4N', 'd3Q', 'a1k', 'c5P'])
['e4N', 'd3Q', 'c5P']
```

```python
>>> extract_white_pieces(['b2p', 'g8R', 'h7q'])
['g8R']
```
