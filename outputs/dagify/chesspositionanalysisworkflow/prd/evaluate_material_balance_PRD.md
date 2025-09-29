# evaluate_material_balance PRD

## Description
Assess material advantage or disadvantage


## Conceptual Info

This node evaluates the material balance between white and black in a given chess position, providing a score that indicates the material advantage or disadvantage.

## Docstring

### Summary
Evaluates the material balance in a chess position based on piece positions.

### Parameters

- **piece_positions** (List[str]): Positions of all pieces on the board, obtained from parse_chess_position.

### Returns

Tuple[float, List[int]]: A tuple containing the material score (float) and the count of each piece type for both sides (List[int]).

### Raises

- ValueError: If the input piece_positions are invalid or not in the expected format.

### Examples

```python
>>> piece_positions = ['e2', 'e4', 'Nb1', 'c3']
>>> result = evaluate_material_balance(piece_positions)
(0.5, [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
```

```python
>>> piece_positions = ['d2', 'd4', 'd7', 'd5']
>>> result = evaluate_material_balance(piece_positions)
(0.0, [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0])
```
