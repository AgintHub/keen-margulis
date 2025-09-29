# validate_piece_positions PRD

## Description
Validate chess piece positions for syntax and legality, returning a cleaned list of positions.


## Conceptual Info

This shim ensures that the piece positions supplied to the chess engine are syntactically correct and represent legal squares on a chessboard, providing a sanitized list for downstream analysis.

## Docstring

### Summary
Validate and sanitize chess piece positions, returning a list of legal squares.

### Parameters

- **positions** (List[str]): List of chess position strings (e.g., ['e4', 'd5']) to be validated.

### Returns

List[str]: A list containing only valid chess positions.

### Raises

- ValueError: Raised when a position string is not a valid chess square (e.g., 'e9', 'z3').
- TypeError: Raised when the input is not a list of strings.

### Examples

```python
>>> validate_piece_positions(['e4', 'd5'])
['e4', 'd5']
```

```python
>>> validate_piece_positions(['e9'])
ValueError: Invalid chess position: e9
```
