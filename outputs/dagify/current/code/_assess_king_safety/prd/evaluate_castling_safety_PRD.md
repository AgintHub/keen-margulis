# evaluate_castling_safety PRD

## Description
Evaluates a numeric bonus based on the given castling rights and the side to move, indicating how safe castling is for that side.


## Conceptual Info

This shim is used within the king safety assessment pipeline to provide a quantitative measure of how favorable castling is for the current side, based on the available castling rights. The returned bonus influences the overall safety score of the king.

## Docstring

### Summary
Computes a castling safety bonus from castling rights and the side to move.

### Parameters

- **castling_rights** (str): A four‑character string representing castling rights in standard chess notation (e.g., 'KQkq', 'KQ', 'kq', or '--').
- **side_to_move** (str): The side to move, either 'white' or 'black'.

### Returns

float: A non‑negative float bonus; higher values indicate safer castling opportunities.

### Raises

- ValueError: Raised when `castling_rights` is not a 4‑character string or contains invalid characters.
- TypeError: Raised when either `castling_rights` or `side_to_move` is not of type `str`.

### Examples

```python
>>> evaluate_castling_safety(castling_rights='KQkq', side_to_move='white')
1.0
```

```python
>>> evaluate_castling_safety(castling_rights='kq', side_to_move='black')
0.5
```
