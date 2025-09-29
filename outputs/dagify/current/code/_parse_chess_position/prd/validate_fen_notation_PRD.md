# validate_fen_notation PRD

## Description
Validates a FEN string, ensuring it follows the standard chess notation format, and returns a canonical form if valid.


## Conceptual Info

This shim ensures that any FEN string passed to the chess parsing pipeline is syntactically and semantically correct, providing a clean, canonical representation for downstream functions.

## Docstring

### Summary
Validate a FEN string according to the FEN specification and return the canonical form if valid.

### Parameters

- **fen** (str): The FEN string to be validated.

### Returns

str: The canonical FEN string if the input is valid.

### Raises

- ValueError: Raised when the FEN string is syntactically or semantically invalid.
- TypeError: Raised when the input is not a string.

### Examples

```python
>>> validate_fen_notation('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
```

```python
>>> validate_fen_notation('invalid fen')
ValueError: Invalid FEN string
```
