# determine_overall_evaluation PRD

## Description
Returns a textual overall evaluation of the chess position based on weighted scores of material, king safety, and pawn structure.


## Conceptual Info

This shim analyses a set of pre‑computed weighted scores to produce a human‑readable overall assessment of a chess position.

## Docstring

### Summary
Generate a concise overall evaluation of a chess position from weighted material, king safety, and pawn structure scores.

### Parameters

- **weighted_scores** (dict): Dictionary containing numeric keys: 'material_score', 'king_safety_score', and 'pawn_structure_score'. Values are floats representing the weighted contribution of each factor.

### Returns

str: A single string summarizing the overall position (e.g., 'Advantage White', 'Equal', or 'Advantage Black').

### Raises

- ValueError: Raised when required keys are missing from `weighted_scores`.
- TypeError: Raised when `weighted_scores` is not a dict or contains non‑numeric values.

### Examples

```python
>>> weighted_scores = {"material_score": 1.2, "king_safety_score": 0.8, "pawn_structure_score": 0.5}
>>> determine_overall_evaluation(weighted_scores)
"Advantage White"
```

```python
>>> weighted_scores = {"material_score": -0.5, "king_safety_score": -1.0, "pawn_structure_score": -0.3}
>>> determine_overall_evaluation(weighted_scores)
"Advantage Black"
```
