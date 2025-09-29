# split_fen_components PRD

## Description
Splits a validated FEN string into its six component fields and returns them as a list of strings.


## Conceptual Info

This shim takes a validated FEN string and splits it into its constituent parts so that downstream parsers can operate on each field separately.

## Docstring

### Summary
Splits a FEN string into its six components.

### Parameters

- **fen** (str): A validated FEN string containing exactly six fields separated by spaces.

### Returns

LIST_STR: A list of six strings representing the FEN components in the order: board, active color, castling rights, en passant target, half‑move clock, and full‑move number.

### Raises

- TypeError: If the input is not a string.
- ValueError: If the input string does not contain exactly six space‑separated parts.

### Examples

```python
>>> split_fen_components('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", "w", "KQkq", "-", "0", "1"]
```

```python
>>> split_fen_components('8/8/8/8/8/8/8/8 w - - 0 1')
["8/8/8/8/8/8/8/8", "w", "-", "-", "0", "1"]
```
