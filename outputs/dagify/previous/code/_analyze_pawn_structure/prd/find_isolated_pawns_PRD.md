# find_isolated_pawns PRD

## Description
Finds isolated pawn positions from a list of pawn positions.


## Conceptual Info

This shim identifies all pawns on a chessboard that have no allied pawns on the files immediately to their left or right, thereby isolating them. It is used within pawn structure analysis to flag potential weaknesses in a player's pawn formation.

## Docstring

### Summary
Return the list of isolated pawn positions from the provided pawn list.

### Parameters

- **pawn_positions** (List[str]): A list of chessboard square identifiers (e.g., 'e4') representing the positions of all pawns of the side to move.

### Returns

List[str]: A list containing the square identifiers of all isolated pawns. If no isolated pawns are found, an empty list is returned.

### Raises

- ValueError: Raised when any element of `pawn_positions` is not a valid 2‑character algebraic notation (e.g., 'i9' or 'a10').
- TypeError: Raised when `pawn_positions` is not a list or contains non‑string elements.

### Examples

```python
>>> find_isolated_pawns(['c2', 'd2', 'e2'])
[]
```

```python
>>> find_isolated_pawns(['a2', 'c2', 'e2', 'g2'])
['a2', 'c2', 'e2', 'g2']
```

```python
>>> find_isolated_pawns(['b2', 'd3', 'f4', 'h5'])
['b2', 'd3', 'f4', 'h5']
```
