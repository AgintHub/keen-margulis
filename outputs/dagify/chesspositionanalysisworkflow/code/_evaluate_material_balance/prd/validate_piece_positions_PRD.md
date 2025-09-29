# validate_piece_positions PRD

## Description
Validates a list of chess position strings, ensuring each is a legal coordinate and normalizes formatting.


## Conceptual Info

The shim acts as a gatekeeper for position data, ensuring downstream functions receive well-formed coordinates.

## Docstring

### Summary
Validate and normalize a list of chess board position strings.

### Parameters

- **piece_positions** (List[str]): A list of strings each representing a square on the chessboard (e.g., 'e4', 'A1').

### Returns

List[str]: The input list with each position converted to lowercase and trimmed; positions are guaranteed to be valid squares.

### Raises

- TypeError: If `piece_positions` is not a list or contains non-string elements.
- ValueError: If any string does not match a valid chess coordinate (files a-h and ranks 1-8).

### Examples

```python
>>> validate_piece_positions(['E4', 'a1', 'H8'])
['e4', 'a1', 'h8']
```

```python
>>> try:
...     validate_piece_positions(['e9', 'b2'])
>>> except ValueError as e:
...     print(e)
Invalid chess position: e9
```
