# get_current_side_king PRD

## Description
Return the king position belonging to the side to move given the two king positions.


## Conceptual Info

Provides the current side's king location based on parsed board positions, enabling subsequent safety assessments.

## Docstring

### Summary
Return the king square belonging to the side specified to move.

### Parameters

- **king_positions** (List[str]): A list containing exactly two elements: the square notation of the white king and the black king, e.g., ['e1', 'e8'].
- **side_to_move** (str): The side to move; must be either 'white' or 'black'.

### Returns

str: The square notation (e.g., 'e1' or 'e8') of the king belonging to the side to move.

### Raises

- ValueError: Raised when the side_to_move is not 'white' or 'black', or when king_positions does not contain the expected king for the given side.
- TypeError: Raised when king_positions is not a list of strings or side_to_move is not a string.

### Examples

```python
>>> king_positions = ['e1', 'e8']
>>> side_to_move = 'white'
>>> print(get_current_side_king(king_positions, side_to_move))
'e1'
```

```python
>>> king_positions = ['e1', 'e8']
>>> side_to_move = 'black'
>>> print(get_current_side_king(king_positions, side_to_move))
'e8'
```
