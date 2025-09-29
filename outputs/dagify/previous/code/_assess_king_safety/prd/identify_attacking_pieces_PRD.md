# identify_attacking_pieces PRD

## Description
This shim returns a list of piece identifiers from piece_positions that are attacking the specified target king, taking into account the side to move.


## Conceptual Info

The identify_attacking_pieces shim is responsible for analyzing a board state represented by piece positions and determining which pieces pose an immediate threat to a given king. It abstracts the chess engine logic of attack detection, enabling higher-level safety assessments without requiring a full engine integration.

## Docstring

### Summary
Return a list of pieces from the provided board representation that are attacking the specified king square.

### Parameters

- **piece_positions** (List[str]): A list of strings representing all pieces on the board in the form of "<piece><square>" (e.g., "Ke1", "Qg5").
- **target_king** (str): The board square of the king to evaluate, expressed as a two‑character coordinate (e.g., "e1").
- **side_to_move** (str): The side that is to move, either "white" or "black".

### Returns

List[str]: A list of strings, each describing a piece that is attacking the target king. The format matches the input representation.

### Raises

- ValueError: Raised when side_to_move is not one of "white" or "black", or when target_king is not a valid square.
- TypeError: Raised when any input parameter has an incorrect type.

### Examples

```python
>>> pieces = ["Ke1", "Qd4", "Ra8", "Bh3", "Ng6", "pd2", "pb7", "pc7"]
>>> attacking = identify_attacking_pieces(piece_positions=pieces, target_king="e1", side_to_move="black")
>>> print(attacking)
["Qd4", "Bh3"]
```

```python
>>> pieces = ["Ke8", "Qa7", "Nc6", "Pf7", "Pg6"]
>>> attacking = identify_attacking_pieces(piece_positions=pieces, target_king="e8", side_to_move="white")
>>> print(attacking)
["Qa7", "Nc6"]
```
