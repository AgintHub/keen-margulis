# combine_piece_counts PRD

## Description
Combines two lists of piece counts (white and black) into a single list by summing corresponding piece type counts.


## Conceptual Info

This shim aggregates the counts of each chess piece type from both the white and black sides to provide a unified view of material distribution.

## Docstring

### Summary
Combine piece counts from two sides of a chess position.

### Parameters

- **white_counts** (List[int]): List of integers representing the count of each piece type for white, ordered consistently with `black_counts`.
- **black_counts** (List[int]): List of integers representing the count of each piece type for black, ordered consistently with `white_counts`.

### Returns

List[int]: A list of integers where each element is the sum of the corresponding elements from `white_counts` and `black_counts`.

### Raises

- TypeError: Raised if either `white_counts` or `black_counts` is not a list or contains non-integer elements.
- ValueError: Raised if `white_counts` and `black_counts` are of different lengths.

### Examples

```python
>>> combine_piece_counts(white_counts=[5, 2, 1, 0, 0, 0],
...                       black_counts=[3, 1, 2, 0, 0, 0])
[8, 3, 3, 0, 0, 0]
```

```python
>>> combine_piece_counts(white_counts=[0, 0, 0, 0, 0, 0],
...                       black_counts=[1, 1, 1, 1, 1, 1])
[1, 1, 1, 1, 1, 1]
```
