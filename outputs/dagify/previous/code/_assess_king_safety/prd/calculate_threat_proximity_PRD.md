# calculate_threat_proximity PRD

## Description
Calculates a numeric threat proximity score for a king based on the positions of attacking pieces.


## Conceptual Info

The shim is responsible for translating the list of attacking piece coordinates and the king's coordinate into a single numeric value that quantifies how close the king is to being captured. This score is used downstream to compute overall king safety.

## Docstring

### Summary
Returns a threat proximity score for a king given the positions of attacking pieces.

### Parameters

- **attacking_pieces** (str): Comma‑separated chess board coordinates (e.g., "b3,d4,f5") of all pieces that attack the king.
- **king_position** (str): The chess board coordinate of the king being evaluated (e.g., "e1").

### Returns

float: A float in the inclusive range [0.0, 1.0] where 0.0 means no immediate threat and 1.0 indicates that the king is under direct attack.

### Raises

- ValueError: Raised when either `attacking_pieces` or `king_position` cannot be parsed into valid board coordinates.
- TypeError: Raised when input types are not strings.

### Examples

```python
>>> score = calculate_threat_proximity(attacking_pieces='b3,d4,f5', king_position='e1')
>>> print(score)
0.42
```

```python
>>> score = calculate_threat_proximity(attacking_pieces='h8', king_position='e1')
>>> print(score)
0.05
```
