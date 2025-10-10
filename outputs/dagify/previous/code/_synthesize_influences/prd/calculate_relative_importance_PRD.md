# calculate_relative_importance PRD

## Description
Computes a normalized list of four floats representing the relative importance of social, political, economic, and cultural influences based on their respective analysis outputs.


## Conceptual Info

This shim aggregates the impact assessments from the four influence categories into a single weight vector that can be used by downstream synthesis functions to balance their contributions in narrative generation.

## Docstring

### Summary
Calculate the relative importance of social, political, economic, and cultural influence categories.

### Parameters

- **social_input** (AnalyzeSocialInfluencesOutput): Pydantic model containing social influence analysis results.
- **political_input** (AnalyzePoliticalInfluencesOutput): Pydantic model containing political influence analysis results.
- **economic_input** (AnalyzeEconomicInfluencesOutput): Pydantic model containing economic influence analysis results.
- **cultural_input** (AnalyzeCulturalInfluencesOutput): Pydantic model containing cultural influence analysis results.

### Returns

List[float]: A list of four floats (social, political, economic, cultural) that sum to 1.0.

### Raises

- ValueError: Raised when any of the input models lack required data or produce an invalid weight distribution.
- TypeError: Raised when the provided arguments are not instances of the expected Pydantic models.

### Examples

```python
>>> social = AnalyzeSocialInfluencesOutput(1, "FactorA", 0.9, "Social summary")
>>> political = AnalyzePoliticalInfluencesOutput(["DecisionA"], ["PolicyA"], ["LeaderA"], "Political summary")
>>> economic = AnalyzeEconomicInfluencesOutput("FactorE", "Economic summary", "SourceA", 0.7, "1900-1910", True)
>>> cultural = AnalyzeCulturalInfluencesOutput(["CulturalA"], ["Norm"], ["Description"], [0.6], [True])
>>> print(calculate_relative_importance(social_input=social, political_input=political, economic_input=economic, cultural_input=cultural))
[0.25, 0.25, 0.25, 0.25]
```

```python
>>> social = AnalyzeSocialInfluencesOutput(3, "A,B,C", 0.8, "S")
>>> political = AnalyzePoliticalInfluencesOutput(["D1"], ["P1"], ["L1"], "P")
>>> economic = AnalyzeEconomicInfluencesOutput("E1", "ES", "Src1", 0.9, "1900-1910", True)
>>> cultural = AnalyzeCulturalInfluencesOutput(["C1"], ["Norm1"], ["Desc1"], [0.2], [True])
>>> print(calculate_relative_importance(social_input=social, political_input=political, economic_input=economic, cultural_input=cultural))
[0.25, 0.25, 0.35, 0.15]
```
