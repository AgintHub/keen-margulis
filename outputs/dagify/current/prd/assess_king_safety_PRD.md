# assess_king_safety PRD

## Description
Assess king safety and potential vulnerabilities


## Conceptual Info

This node assesses the safety of the kings on a chessboard by analyzing their positions, surrounding pieces, and potential threats.

## Docstring

### Summary
Assess king safety based on position and threats.

### Parameters

- **piece_positions** (List[str]): Positions of all pieces on the board from parse_chess_position.
- **castling_rights** (List[bool]): Castling rights for both white and black from parse_chess_position.
- **en_passant_square** (str): En passant square if available from parse_chess_position.
- **side_to_move** (str): Side to move (white or black) from parse_chess_position.

### Returns

Tuple[float, List[str]]: A tuple containing the king safety score and a list of potential threats.

### Raises

- ValueError: If piece_positions is not a valid list of chess positions.

### Examples

```python
>>> piece_positions = ['e1', 'e8', 'e2', 'e7']
>>> castling_rights = [True, False]
>>> en_passant_square = 'e3'
>>> side_to_move = 'white'
>>> result = assess_king_safety(piece_positions, castling_rights, en_passant_square, side_to_move)
(0.7, ['Queen on d5', 'Knight on f3'])
```

```python
>>> piece_positions = ['e1', 'e8', 'd4', 'd5']
>>> castling_rights = [False, True]
>>> en_passant_square = None
>>> side_to_move = 'black'
>>> result = assess_king_safety(piece_positions, castling_rights, en_passant_square, side_to_move)
(0.4, ['Rook on e1', 'Bishop on c4'])
```
