# validate_input PRD

## Description
Validates chess piece positions and side to move, returning a success message or raising errors if invalid.


## Conceptual Info

The validate_input shim verifies that the provided list of piece positions and the side-to-move string are syntactically correct and conform to basic chess rules before proceeding to more complex analysis functions.

## Docstring

### Summary
Validate chess piece positions and side-to-move string, returning a confirmation message or raising appropriate errors.

### Parameters

- **piece_positions** (List[str]): A list of strings representing the positions of all pieces on the board in standard algebraic notation (e.g., 'e4', 'g8').
- **side_to_move** (str): The side that is to move, either 'white' or 'black' (case-insensitive).

### Returns

str: A confirmation message such as 'Validation successful.' when inputs are valid.

### Raises

- ValueError: Raised when any piece position is not a valid square (e.g., 'i9') or when the side_to_move is not 'white' or 'black'.
- TypeError: Raised when piece_positions is not a list or when side_to_move is not a string.

### Examples

```python
>>> validate_input(['e4', 'd5', 'g2'], 'white')
"Validation successful."
```

```python
>>> try:
...     validate_input(['e4', 'x9', 'g2'], 'black')
>>> except Exception as e:
...     print(e)
"ValueError: Invalid piece position 'x9'."
```
