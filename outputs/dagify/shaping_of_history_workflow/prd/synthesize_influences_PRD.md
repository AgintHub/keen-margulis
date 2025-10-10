# synthesize_influences PRD

## Description
Combine the analyses of various social, political, economic, and cultural influences to produce a comprehensive synthesis, identifying how these factors interacted, where they converged, and their relative importance.


## Conceptual Info

This node aggregates the detailed findings from four distinct analytical modules—social, political, economic, and cultural—to produce a unified narrative of influence. It extracts salient themes, highlights cross‑sector interactions, and quantifies the relative weight of each sector in shaping the historical event.

## Docstring

### Summary
Synthesize social, political, economic, and cultural analyses into a coherent set of insights.

### Parameters

- **social_analysis** (dict): Dictionary containing outputs from `analyze_social_influences`. Expected keys: `number_of_factors`, `social_factors`, `impact_scores`, `summary`.
- **political_analysis** (dict): Dictionary containing outputs from `analyze_political_influences`. Expected keys: `political_decisions`, `policies_influenced`, `leadership_figures`, `summary`.
- **economic_analysis** (dict): Dictionary containing outputs from `analyze_economic_influences`. Expected keys: `economic_factor_name`, `impact_summary`, `evidence_sources`, `impact_strength`, `time_period_affected`, `is_consensus`.
- **cultural_analysis** (dict): Dictionary containing outputs from `analyze_cultural_influences`. Expected keys: `cultural_factors`, `factor_categories`, `factor_descriptions`, `influence_scores`, `is_significant`.

### Returns

dict: A dictionary with keys `social_insights`, `economic_insights`, `political_insights`, `cultural_insights`, `synthesis_summary`, `interaction_points`, and `importance_scores`.

### Raises

- ValueError: Raised if any required key is missing from one of the input analysis dictionaries.

### Examples

```python
>>> social_analysis = {
...     "number_of_factors": 3,
...     "social_factors": ["Urbanization", "Labor Movements", "Education Reform"],
...     "impact_scores": [0.8, 0.6, 0.5],
...     "summary": "Rapid urban growth spurred labor activism and educational reforms that reshaped social norms."
>>> }
>>> political_analysis = {
...     "political_decisions": ["Industrial Policy Act 1920", "Labor Law Reform 1935"],
...     "policies_influenced": ["Minimum Wage", "Workplace Safety Regulations"],
...     "leadership_figures": ["Prime Minister A", "Senator B"],
...     "summary": "Government policies institutionalized labor rights and industrial oversight."
>>> }
>>> economic_analysis = {
...     "economic_factor_name": "Post‑War Reconstruction",
...     "impact_summary": "Reconstruction spending accelerated industrial output and urban migration.",
...     "evidence_sources": ["Census 1941", "Trade Reports 1945"],
...     "impact_strength": 0.9,
...     "time_period_affected": "1945–1955",
...     "is_consensus": true
>>> }
>>> cultural_analysis = {
...     "cultural_factors": ["Modernist Art Movement", "Literary Boom"],
...     "factor_categories": ["Art", "Literature"],
...     "factor_descriptions": ["Challenged traditional aesthetics", "Explored new narrative forms"],
...     "influence_scores": [0.4, 0.3],
...     "is_significant": [true, true]
>>> }
>>> from synthesize_influences import synthesize_influences
>>> result = synthesize_influences(social_analysis, political_analysis, economic_analysis, cultural_analysis)
>>> print(result["synthesis_summary"])
"The post‑war reconstruction boom fueled urbanization, creating a labor pool that empowered social movements. Government policies codified labor rights, while modernist art and literature reflected and reinforced the era’s transformative ethos. Together, these intertwined forces accelerated industrial growth and reshaped societal structures.
"
```

```python
>>> # Minimal example focusing on relative importance scoring
>>> social_analysis = {"number_of_factors":1,"social_factors":["Migration"],"impact_scores":[0.7],"summary":"Population shifts reshaped communities."}
>>> political_analysis = {"political_decisions":[],"policies_influenced":[],"leadership_figures":[],"summary":"Political stability maintained."}
>>> economic_analysis = {"economic_factor_name":"Export Boom","impact_summary":"Exports surged, boosting GDP.","evidence_sources":[],"impact_strength":0.8,"time_period_affected":"1980s","is_consensus":true}
>>> cultural_analysis = {"cultural_factors":[],"factor_categories":[],"factor_descriptions":[],"influence_scores":[],"is_significant":[]}
>>> result = synthesize_influences(social_analysis, political_analysis, economic_analysis, cultural_analysis)
>>> print(result["importance_scores"])
[0.7, 0.1, 0.8, 0.0]
```
