# analyze_economic_influences PRD

## Description
Assess the economic factors that contributed to the historical event or period.


## Conceptual Info

Transforms a list of economic factors identified by the parent node into a structured assessment that quantifies each factor's influence on the historical event.

## Docstring

### Summary
Analyzes each economic factor from the input list and returns a structured assessment of its impact on the historical event or period.

### Parameters

- **economic_factors** (List[str]): List of economic factors identified by the `identify_key_factors` node.

### Returns

List[Dict[str, Any]]: A list of dictionaries, each containing structured information about an economic factor.

### Raises

- ValueError: Raised when the `economic_factors` list is empty.
- TypeError: Raised when `economic_factors` is not a list of strings.

### Examples

```python
>>> analyze_economic_influences(['Inflation', 'Trade Embargo'])
[{'economic_factor_name': 'Inflation', 'impact_summary': 'High inflation reduced purchasing power and disrupted domestic markets.', 'evidence_sources': ['Economic Report 1931', 'Historical GDP Data'], 'impact_strength': 0.85, 'time_period_affected': '1931-1933', 'is_consensus': True}, {'economic_factor_name': 'Trade Embargo', 'impact_summary': 'The embargo limited exports, weakening the national economy.', 'evidence_sources': ['Trade Records 1940', 'Diplomatic Correspondence'], 'impact_strength': 0.70, 'time_period_affected': '1940-1945', 'is_consensus': False}]
```

```python
>>> analyze_economic_influences(['Industrial Production Growth'])
[{'economic_factor_name': 'Industrial Production Growth', 'impact_summary': 'Rapid industrial growth fueled wartime manufacturing.', 'evidence_sources': ['Industrial Production Index 1944'], 'impact_strength': 0.90, 'time_period_affected': '1942-1945', 'is_consensus': True}]
```
