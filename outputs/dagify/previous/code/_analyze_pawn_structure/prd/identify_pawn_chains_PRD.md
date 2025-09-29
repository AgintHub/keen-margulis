# identify_pawn_chains PRD

## Description
Returns a list of pawn chain strings derived from the provided pawn positions.


## Conceptual Info

The identify_pawn_chains shim processes a string of pawn positions, grouping them into connected chains based on their relative file and rank relationships, and outputs each chain as a formatted string.

## Docstring

### Summary
Identify pawn chains from a string of pawn positions.

### Parameters

- **pawn_positions** (str): A space-separated string of pawn square identifiers (e.g., 'a2 b2 c3').

### Returns

List[str]: A list where each element is a string representation of a pawn chain, with squares joined by hyphens.

### Raises

- ValueError: If pawn_positions is empty or contains invalid square notation.
- TypeError: If pawn_positions is not a string.

### Examples

```python
>>> identify_pawn_chains('a2 b2 c3')
['a2-b2', 'c3']
```

```python
>>> identify_pawn_chains('d4 e5 f6')
['d4-e5-f6']
```
