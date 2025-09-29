# calculate_weighted_position_scores PRD

## Description
Computes a weighted evaluation dictionary for a chess position based on material advantage, king safety, and pawn structure, and returns it as a JSON-formatted string.


## Conceptual Info

This shim aggregates three core components of a chess position—material balance, king safety, and pawn structure—into a single weighted score dictionary. It is used by the synthesis layer to produce overall evaluations, strategic recommendations, and tactical opportunities.

## Docstring

### Summary
Computes weighted scores for material, king safety, and pawn structure, returning a JSON string.

### Parameters

- **material_score** (str): String representation of the material advantage score (float).
- **king_safety_score** (str): String representation of the king safety score (float).
- **pawn_structure** (str): JSON string of the pawn structure analysis, e.g. {"pawn_chain_analysis": [...], "isolated_pawns": [...], "passed_pawns": [...]}.

### Returns

str: JSON string of a dictionary containing the weighted scores:

{
    "material_weight": float,
    "king_weight": float,
    "pawn_weight": float
}

### Raises

- ValueError: Raised when any of the input strings cannot be parsed into the expected numeric or JSON structures.
- TypeError: Raised when input types are not strings.

### Examples

```python
>>> import json
>>> def example():
...     result = calculate_weighted_position_scores(
...         material_score='0.75',
...         king_safety_score='1.25',
...         pawn_structure=json.dumps({
...             'pawn_chain_analysis': ['e3-f4'],
...             'isolated_pawns': ['d2'],
...             'passed_pawns': ['g7']
...         })
...     )
...     print(result)
"{\"material_weight\":0.3,\"king_weight\":0.5,\"pawn_weight\":0.2}"
```

```python
>>> print(calculate_weighted_position_scores('1.0', '0.8', '{}'))
"{\"material_weight\":0.4,\"king_weight\":0.3,\"pawn_weight\":0.3}"
```
