# find_passed_pawns PRD

## Description
Identifies passed pawns for a given side based on pawn and piece positions.


## Conceptual Info

The find_passed_pawns shim analyzes the positions of pawns and all pieces on a chess board to determine which pawns are passed for a given side.

## Docstring

### Summary
Return the list of passed pawn positions for the specified side based on the provided pawn and full piece positions.

### Parameters

- **pawn_positions** (str): Comma‑separated string of pawn squares belonging to the side to evaluate (e.g., "a2,b3").
- **all_piece_positions** (str): Comma‑separated string of all piece squares on the board, regardless of color.
- **side** (str): Either "white" or "black" indicating which side's passed pawns to find.

### Returns

LIST_STR: A list of board squares that are passed pawns for the specified side.

### Raises

- ValueError: Raised when `side` is not "white" or "black", or when `pawn_positions` is empty.
- TypeError: Raised when any of the arguments are not of type `str`.

### Examples

```python
>>> find_passed_pawns('a2', 'a2,b3', 'white')
['a2']
```

```python
>>> find_passed_pawns('c7', 'a2,b3,c7,d5', 'black')
['c7']
```
