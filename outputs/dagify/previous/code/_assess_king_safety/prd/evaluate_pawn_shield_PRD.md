# evaluate_pawn_shield PRD

## Description
Calculates a numeric score that quantifies the effectiveness of the pawn shield protecting the king for the side to move.


## Conceptual Info

The evaluate_pawn_shield shim is responsible for evaluating how well a king’s pawn shield protects it from direct attacks. It interprets the board state, locates the king and friendly pawns, and returns a float score that is used by higher‑level safety calculations.

## Docstring

### Summary
Return a float score representing the pawn shield strength for the king of the side to move.

### Parameters

- **piece_positions** (str): Comma‑separated list of piece descriptors in the format "<piece>@<square>", e.g., "P@e2,p@d3".
- **king_position** (str): Algebraic notation of the king’s square (e.g., "e1" for White king).
- **side_to_move** (str): The side whose pawn shield is being evaluated, either "white" or "black".

### Returns

float: A score in the range 0.0 to 1.0 indicating how well the king is protected by its pawns.

### Raises

- ValueError: Raised when the input strings cannot be parsed into a valid board representation or contain illegal piece descriptors.
- TypeError: Raised when any of the input arguments is not of type str.

### Examples

```python
>>> score = evaluate_pawn_shield('P@e2,P@d2,P@f2', 'e1', 'white')
>>> print(round(score, 2))
0.87
```

```python
>>> score = evaluate_pawn_shield('P@e2,P@d3,P@f3', 'e1', 'white')
>>> print(round(score, 2))
0.65
```
