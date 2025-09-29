# count_pieces_by_type PRD

## Description
Counts the number of each chess piece type from a list of piece symbols and returns a list of counts in the order king, queen, rook, bishop, knight, pawn.


## Conceptual Info

This shim aggregates the quantity of each chess piece type for a single side, providing a foundation for material evaluation and board analysis.

## Docstring

### Summary
Counts chess pieces by type.

### Parameters

- **pieces** (List[str]): A list of piece symbols (e.g., 'K', 'Q', 'R', 'B', 'N', 'P') representing the pieces of one side.

### Returns

List[int]: A list of six integers: [king_count, queen_count, rook_count, bishop_count, knight_count, pawn_count].

### Raises

- TypeError: Raised if `pieces` is not a list.
- ValueError: Raised if any element in `pieces` is not a valid chess piece symbol.

### Examples

```python
>>> count_pieces_by_type(['K', 'P', 'P', 'Q', 'R', 'B', 'N', 'P'])
[1, 1, 1, 1, 1, 3]
```

```python
>>> count_pieces_by_type([])
[0, 0, 0, 0, 0, 0]
```
