# compute_material_score PRD

## Description
Calculates the material score by subtracting black's material value from white's material value.


## Conceptual Info

The shim computes a numeric score representing the material advantage of the white side over the black side by comparing their aggregated material values.

## Docstring

### Summary
Return the material score as a float by subtracting the black material value from the white material value.

### Parameters

- **white_value** (float): Total material value of the white side, as returned by calculate_material_value.
- **black_value** (float): Total material value of the black side, as returned by calculate_material_value.

### Returns

float: The material score (white_value minus black_value). A positive value indicates a white advantage, zero indicates parity, and negative indicates a black advantage.

### Raises

- TypeError: Raised when either `white_value` or `black_value` is not of type float.
- ValueError: Raised when either `white_value` or `black_value` is negative, since material values should be non‑negative.

### Examples

```python
>>> compute_material_score(white_value=9.0, black_value=5.0)
4.0
```

```python
>>> compute_material_score(white_value=6.0, black_value=6.0)
0.0
```
