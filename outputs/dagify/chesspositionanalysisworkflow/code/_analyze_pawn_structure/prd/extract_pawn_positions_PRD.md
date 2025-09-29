# extract_pawn_positions PRD

## Description
Returns the list of board coordinates occupied by the pawns of a specified side from a list of all piece positions.


## Conceptual Info

This shim isolates the pawn locations on the board for a given side, enabling downstream analysis of pawn structure such as chains, isolation, and passing.

## Docstring

### Summary
Extracts the positions of all pawns for a specified side from a list of all piece positions.

### Parameters

- **piece_positions** (List[str]): A list of strings representing all piece positions on the board (e.g., ['e4', 'd5', 'c3']). Each string follows standard algebraic notation without piece type identifiers.
- **side** (str): The side whose pawn positions should be returned; expected values are 'white' or 'black'.

### Returns

List[str]: A list of position strings corresponding to the pawns belonging to the specified side.

### Raises

- ValueError: Raised when `side` is not 'white' or 'black', or when `piece_positions` contains an invalid board coordinate.
- TypeError: Raised when `piece_positions` is not a list of strings or when `side` is not a string.

### Examples

```python
>>> extract_pawn_positions(['a2', 'b2', 'c3', 'd5', 'e4'], 'white')
['a2', 'b2']
```

```python
>>> extract_pawn_positions(['a7', 'b6', 'c5', 'd4', 'e3'], 'black')
['a7', 'b6', 'c5']
```
