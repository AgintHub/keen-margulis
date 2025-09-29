# analyze_pawn_structure PRD

## Description
Examine pawn chain, isolated pawns, and other structural elements.


## Conceptual Info

This node analyzes the pawn structure of a given chess position to identify strengths and weaknesses.

## Docstring

### Summary
Analyze the pawn structure from the parsed chess position.

### Parameters

- **piece_positions** (List[str]): Positions of all pieces on the board, provided by the parse_chess_position node.
- **side_to_move** (str): Side to move (white or black), provided by the parse_chess_position node.

### Returns

Tuple[List[str], List[str], List[str]]: A tuple containing the analysis of pawn chains, positions of isolated pawns, and positions of passed pawns.

### Raises

- ValueError: If the piece_positions list is empty or if side_to_move is not 'white' or 'black'.

### Examples

```python
>>> piece_positions = ['e2', 'e4', 'd4', 'c3']
>>> side_to_move = 'white'
>>> result = analyze_pawn_structure(piece_positions, side_to_move)
(['Pawn chain on d4 and c3 is strong'], ['b2'], ['e4'])
```

```python
>>> piece_positions = ['e7', 'd5', 'c6']
>>> side_to_move = 'black'
>>> result = analyze_pawn_structure(piece_positions, side_to_move)
(['Pawn chain on d5 and c6 is flexible'], ['a7'], ['d5'])
```
