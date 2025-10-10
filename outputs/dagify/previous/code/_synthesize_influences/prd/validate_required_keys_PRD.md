# validate_required_keys PRD

## Description
Validates that all required fields are present and non‑null in the social, political, economic, and cultural input data before synthesis.


## Conceptual Info

This shim ensures the integrity of the four influence analysis inputs by verifying that each required attribute exists and holds a value before proceeding to synthesize insights.

## Docstring

### Summary
Validate the presence and non‑nullness of all required keys in the social, political, economic, and cultural input objects.

### Parameters

- **social_input** (Any): Instance of AnalyzeSocialInfluencesOutput containing social influence data.
- **political_input** (Any): Instance of AnalyzePoliticalInfluencesOutput containing political influence data.
- **economic_input** (Any): Instance of AnalyzeEconomicInfluencesOutput containing economic influence data.
- **cultural_input** (Any): Instance of AnalyzeCulturalInfluencesOutput containing cultural influence data.

### Returns

str: A confirmation string, e.g., 'Validation passed', if all keys are present; otherwise a ValueError is raised.

### Raises

- ValueError: Raised when any required key is missing or its value is None.
- TypeError: Raised when an input argument is not an instance of the expected influence model.

### Examples

```python
>>> validate_required_keys(
...     social_input=AnalyzeSocialInfluencesOutput(
...         number_of_factors=3, social_factors='A,B,C', impact_scores=0.8, summary='summary' )
...     , political_input=AnalyzePoliticalInfluencesOutput(
...         political_decisions=['dec1'], policies_influenced=['pol1'], leadership_figures=['lead1'], summary='political summary' )
...     , economic_input=AnalyzeEconomicInfluencesOutput(
...         economic_factor_name='fact', impact_summary='sum', evidence_sources='src', impact_strength=0.5, time_period_affected='1800s', is_consensus=True )
...     , cultural_input=AnalyzeCulturalInfluencesOutput(
...         cultural_factors=['fac1'], factor_categories=['cat1'], factor_descriptions=['desc1'], influence_scores=[0.7], is_significant=[True] )
>>> )
'Validation passed'
```

```python
>>> validate_required_keys(
...     social_input=AnalyzeSocialInfluencesOutput(
...         number_of_factors=2, social_factors='A,B', impact_scores=None, summary='summary' )
...     , political_input=AnalyzePoliticalInfluencesOutput(
...         political_decisions=['dec1'], policies_influenced=['pol1'], leadership_figures=['lead1'], summary='political summary' )
...     , economic_input=AnalyzeEconomicInfluencesOutput(
...         economic_factor_name='fact', impact_summary='sum', evidence_sources='src', impact_strength=0.5, time_period_affected='1800s', is_consensus=True )
...     , cultural_input=AnalyzeCulturalInfluencesOutput(
...         cultural_factors=['fac1'], factor_categories=['cat1'], factor_descriptions=['desc1'], influence_scores=[0.7], is_significant=[True] )
>>> )
ValueError: Missing required keys in social_input: impact_scores
```
