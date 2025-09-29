# validate_input_analyses PRD

## Description
Validates that the material balance, pawn structure, and king safety analysis outputs contain all required fields and correct data types.


## Conceptual Info

This shim acts as a gatekeeper before synthesis, ensuring that the analysis results from material balance, pawn structure, and king safety nodes are structurally sound and type‑correct.

## Docstring

### Summary
Validate input analysis outputs and return a confirmation string.

### Parameters

- **material_balance** (EvaluateMaterialBalanceOutput): Pydantic model containing material score and piece counts.
- **pawn_structure** (AnalyzePawnStructureOutput): Pydantic model detailing pawn chain analysis, isolated and passed pawns.
- **king_safety** (AssessKingSafetyOutput): Pydantic model with king safety score and potential threats.

### Returns

str: A confirmation string such as 'Validation successful.' when inputs satisfy all constraints.

### Raises

- ValueError: Raised if any of the input models lack required fields or contain invalid data.
- TypeError: Raised if any of the arguments are not instances of the expected Pydantic models.

### Examples

```python
>>> from pydantic import BaseModel, Field
>>> class EvaluateMaterialBalanceOutput(BaseModel):
...     material_score: float = Field(...)
...     piece_counts: int = Field(...)
>>> class AnalyzePawnStructureOutput(BaseModel):
...     pawn_chain_analysis: list[str] = Field(...)
...     isolated_pawns: list[str] = Field(...)
...     passed_pawns: list[str] = Field(...)
>>> class AssessKingSafetyOutput(BaseModel):
...     king_safety_score: float = Field(...)
...     threats: str = Field(...)
>>> mb = EvaluateMaterialBalanceOutput(material_score=2.5, piece_counts=5)
>>> ps = AnalyzePawnStructureOutput(pawn_chain_analysis=['a2-b3'], isolated_pawns=['c4'], passed_pawns=['h6'])
>>> ks = AssessKingSafetyOutput(king_safety_score=1.8, threats='none')
>>> print(validate_input_analyses(material_balance=mb, pawn_structure=ps, king_safety=ks))
'Validation successful.'
```

```python
>>> mb = EvaluateMaterialBalanceOutput(material_score=2.5, piece_counts=5)
>>> ps = AnalyzePawnStructureOutput(pawn_chain_analysis=['a2-b3'], isolated_pawns=['c4'], passed_pawns=['h6'])
>>> ks = AssessKingSafetyOutput(king_safety_score=1.8, threats='none')
>>> try:
...     validate_input_analyses(material_balance=mb, pawn_structure=ps, king_safety=None)
>>> except Exception as e:
...     print(repr(e))
'TypeError: Expected instance of AssessKingSafetyOutput but received NoneType'
```
