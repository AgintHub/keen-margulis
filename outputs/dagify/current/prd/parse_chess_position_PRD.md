# parse_chess_position PRD

## Description
Convert chess position notation into a usable data structure


## Conceptual Info

This node converts chess position notation into a structured data format that includes piece positions, castling rights, en passant square, and the side to move.

## Docstring

### Summary
Parses a given chess position in standard algebraic notation (FEN) into a structured format.

### Parameters

- **fen_notation** (str): The chess position in FEN notation to be parsed.

### Returns

dict: A dictionary containing piece positions, castling rights, en passant square, and side to move.

### Raises

- ValueError: If the input FEN notation is invalid or malformed.

### Examples

```python
>>> fen_notation = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
>>> parse_chess_position(fen_notation)
{'piece_positions': ['e2', 'e4', ...], 'castling_rights': [true, true], 'en_passant_square': 'e3', 'side_to_move': 'white'}
```

```python
>>> fen_notation = '8/8/8/8/8/8/8/8 b - - 0 1'
>>> parse_chess_position(fen_notation)
{'piece_positions': [], 'castling_rights': [false, false], 'en_passant_square': None, 'side_to_move': 'black'}
```
