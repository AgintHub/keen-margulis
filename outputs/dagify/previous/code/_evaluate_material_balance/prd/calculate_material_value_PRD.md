# calculate_material_value PRD

## Description
Computes the material value of a side based on piece counts.


## Conceptual Info

This shim calculates a numeric value representing the material advantage of a chess side by weighting each piece type with standard chess piece values and summing the result based on the provided counts.

## Docstring

### Summary
Calculates the material value of a side based on the counts of each piece type.

### Parameters

- **piece_counts** (List[int]): A list of integers representing the number of each piece type in the order [pawn, knight, bishop, rook, queen, king].

### Returns

float: The total material value as a float. Positive values indicate an advantage for the side, while negative values indicate a disadvantage.

### Raises

- ValueError: Raised when the input list is not exactly six elements long.
- TypeError: Raised when any element in the list is not an integer.
- ValueError: Raised when any count is negative.

### Examples

```python
>>> calculate_material_value(piece_counts=[8, 2, 2, 2, 1, 1])
39.0
```

```python
>>> calculate_material_value(piece_counts=[0, 2, 2, 2, 1, 1])
17.0
```
