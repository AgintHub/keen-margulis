# _synthesize_analysis - Complete PRD Documentation

## Overview
PRDs for nodes in the '_synthesize_analysis' module.

## Table of Contents

- [validate_input_analyses](#validate_input_analyses)

- [calculate_weighted_position_scores](#calculate_weighted_position_scores)

- [determine_overall_evaluation](#determine_overall_evaluation)

- [generate_strategic_recommendations](#generate_strategic_recommendations)

- [identify_tactical_opportunities](#identify_tactical_opportunities)



---

## validate_input_analyses

### Description
Validates that the material balance, pawn structure, and king safety analysis outputs contain all required fields and correct data types.

### Conceptual Info

This shim acts as a gatekeeper before synthesis, ensuring that the analysis results from material balance, pawn structure, and king safety nodes are structurally sound and type‑correct.

### Docstring

**Summary:** Validate input analysis outputs and return a confirmation string.

**Parameters:**

- material_balance (EvaluateMaterialBalanceOutput): Pydantic model containing material score and piece counts.
- pawn_structure (AnalyzePawnStructureOutput): Pydantic model detailing pawn chain analysis, isolated and passed pawns.
- king_safety (AssessKingSafetyOutput): Pydantic model with king safety score and potential threats.
**Returns:** str - A confirmation string such as 'Validation successful.' when inputs satisfy all constraints.

**Raises:**

- ValueError: Raised if any of the input models lack required fields or contain invalid data.
- TypeError: Raised if any of the arguments are not instances of the expected Pydantic models.
**Examples:**

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



---

## calculate_weighted_position_scores

### Description
Computes a weighted evaluation dictionary for a chess position based on material advantage, king safety, and pawn structure, and returns it as a JSON-formatted string.

### Conceptual Info

This shim aggregates three core components of a chess position—material balance, king safety, and pawn structure—into a single weighted score dictionary. It is used by the synthesis layer to produce overall evaluations, strategic recommendations, and tactical opportunities.

### Docstring

**Summary:** Computes weighted scores for material, king safety, and pawn structure, returning a JSON string.

**Parameters:**

- material_score (str): String representation of the material advantage score (float).
- king_safety_score (str): String representation of the king safety score (float).
- pawn_structure (str): JSON string of the pawn structure analysis, e.g. {"pawn_chain_analysis": [...], "isolated_pawns": [...], "passed_pawns": [...]}.
**Returns:** str - JSON string of a dictionary containing the weighted scores:

{
    "material_weight": float,
    "king_weight": float,
    "pawn_weight": float
}

**Raises:**

- ValueError: Raised when any of the input strings cannot be parsed into the expected numeric or JSON structures.
- TypeError: Raised when input types are not strings.
**Examples:**

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



---

## determine_overall_evaluation

### Description
Returns a textual overall evaluation of the chess position based on weighted scores of material, king safety, and pawn structure.

### Conceptual Info

This shim analyses a set of pre‑computed weighted scores to produce a human‑readable overall assessment of a chess position.

### Docstring

**Summary:** Generate a concise overall evaluation of a chess position from weighted material, king safety, and pawn structure scores.

**Parameters:**

- weighted_scores (dict): Dictionary containing numeric keys: 'material_score', 'king_safety_score', and 'pawn_structure_score'. Values are floats representing the weighted contribution of each factor.
**Returns:** str - A single string summarizing the overall position (e.g., 'Advantage White', 'Equal', or 'Advantage Black').

**Raises:**

- ValueError: Raised when required keys are missing from `weighted_scores`.
- TypeError: Raised when `weighted_scores` is not a dict or contains non‑numeric values.
**Examples:**

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



---

## generate_strategic_recommendations

### Description
Generate a list of strategic recommendations for a chess position based on material balance, pawn structure, and king safety.

### Conceptual Info

This shim synthesizes strategic advice for chess positions, aggregating insights from material, pawn, and king safety analyses.

### Docstring

**Summary:** Generate strategic recommendations for a chess position based on material balance, pawn structure, and king safety.

**Parameters:**

- material_balance (str): Serialized representation of material balance (e.g., JSON or key/value string of EvaluateMaterialBalanceOutput).
- pawn_structure (str): Serialized representation of pawn structure (e.g., JSON or key/value string of AnalyzePawnStructureOutput).
- king_safety (str): Serialized representation of king safety (e.g., JSON or key/value string of AssessKingSafetyOutput).
**Returns:** List[str] - A list of strategic recommendations, each as a concise string.

**Raises:**

- ValueError: If any of the serialized inputs are missing required fields or contain invalid data.
- TypeError: If the input parameters are not of type str.
**Examples:**

```python
>>> recommendations = generate_strategic_recommendations(
...     "{\"material_score\":1.5,\"piece_counts\":32}",
...     "{\"pawn_chain_analysis\":[],\"isolated_pawns\":['e5'],\"passed_pawns\":['d6']} ",
...     "{\"king_safety_score\":0.8,\"threats\":\"None\"}"
>>> )
>>> print(recommendations)
['Control center', 'Develop pieces', 'Create passed pawn']
```

```python
>>> recommendations = generate_strategic_recommendations(
...     "{\"material_score\":0.2,\"piece_counts\":30}",
...     "{\"pawn_chain_analysis\":[\"c4-d5\"],\"isolated_pawns\":[],\"passed_pawns\":[]} ",
...     "{\"king_safety_score\":0.4,\"threats\":\"Rook on h1\"}"
>>> )
>>> print(recommendations)
['Hold the center', 'Exchange queens', 'Protect the king with a pawn shield']
```



---

## identify_tactical_opportunities

### Description
Identify tactical opportunities in a chess position from pawn weaknesses, passed pawns and king threats.

### Conceptual Info

This shim analyzes pawn structure weaknesses (isolated pawns), passed pawn possibilities, and direct king threats to generate actionable tactical ideas such as forks, pins, and mating nets. It acts as the tactical analysis layer within the broader synthesis pipeline.

### Docstring

**Summary:** Return a list of tactical opportunities based on pawn weaknesses, passed pawns, and king threats.

**Parameters:**

- pawn_weaknesses (str): Comma‑separated list of squares containing isolated or otherwise weakened pawns.
- passed_pawns (str): Comma‑separated list of squares of passed pawns.
- king_threats (str): Comma‑separated list of squares or patterns representing direct threats to the king (e.g., potential checks, mating nets).
**Returns:** List[str] - A list of descriptive strings, each describing a distinct tactical opportunity that can be pursued from the given position.

**Raises:**

- TypeError: Raised when any of the input parameters is not of type `str`.
- ValueError: Raised when any of the input strings is empty or cannot be parsed into a list of squares.
**Examples:**

```python
>>> opportunities = identify_tactical_opportunities(
...     pawn_weaknesses='c3, e5',
...     passed_pawns='g4',
...     king_threats='h7'"
              ")
>>> print(opportunities)
['Fork on c3', 'Pawn push g4+ leading to mate in 2', 'Pin on h7']
```

```python
>>> opportunities = identify_tactical_opportunities(
...     pawn_weaknesses='b2',
...     passed_pawns='h2, h3',
...     king_threats='f7'"
              ")
>>> print(opportunities)
['Double attack on b2', 'Advance h2 to h3 opening a discovered attack', 'Check on f7 from h5']
```

