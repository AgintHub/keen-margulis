# find_king_positions PRD

## Description
Finds the board positions of the white and black kings from a list of piece position strings.


## Conceptual Info

The shim extracts king locations from a validated list of chess piece positions, ensuring both white and black kings are present and correctly identified.

## Docstring

### Summary
Returns the positions of the white and black kings in the given board representation.

### Parameters

- **piece_positions** (List[str]): A list of strings, each describing a piece on the board in the form "<PieceLetter><Square>", e.g., "Ke1" for the white king on e1.

### Returns

List[str]: A list of two strings containing the king squares, e.g., ["e1", "e8"]. The first element corresponds to the white king, the second to the black king.

### Raises

- TypeError: Raised if `piece_positions` is not a list of strings.
- ValueError: Raised if no king or more than one king of either color is found.

### Examples

```python
>>> positions = ["Ke1", "Qd8", "Ke8", "Nb5"]
>>> find_king_positions(piece_positions=positions)
["e1", "e8"]
```

```python
>>> positions = ["Ke1", "Qd8", "Nb5"]
>>> find_king_positions(piece_positions=positions)
ValueError: No king found for black side.
```
