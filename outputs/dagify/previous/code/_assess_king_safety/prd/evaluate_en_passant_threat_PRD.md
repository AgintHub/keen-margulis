# evaluate_en_passant_threat PRD

## Description
Evaluates the threat posed by an en passant square on the current king's safety and returns a numeric threat score.


## Conceptual Info

The shim calculates a float score that quantifies the potential danger of an en passant capture to the king, integrating this metric into overall king safety assessment.

## Docstring

### Summary
Computes a numeric score representing how much an en passant square threatens the king’s safety.

### Parameters

- **en_passant_square** (str): Algebraic notation of the en passant square (e.g., 'e3') or an empty string if no en passant is available.
- **king_position** (str): Algebraic notation of the king’s current position (e.g., 'e1').

### Returns

float: A non‑negative float where a higher value indicates a greater threat to the king from the en passant square.

### Raises

- ValueError: If `en_passant_square` is not a valid algebraic square or is not applicable for the given king position.
- TypeError: If either `en_passant_square` or `king_position` is not a string.

### Examples

```python
>>> >>> evaluate_en_passant_threat('e3', 'e1')
>>> 0.0
0.0
```

```python
>>> >>> evaluate_en_passant_threat('d4', 'e1')
>>> 0.5
0.5
```
