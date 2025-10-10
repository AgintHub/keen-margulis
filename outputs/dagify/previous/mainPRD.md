# shaping_of_history_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'shaping_of_history_workflow' module.

## Table of Contents

- [analyze_cultural_influences](#analyze_cultural_influences)

- [analyze_economic_influences](#analyze_economic_influences)

- [analyze_political_influences](#analyze_political_influences)

- [analyze_social_influences](#analyze_social_influences)

- [compile_historical_narrative](#compile_historical_narrative)

- [define_historical_context](#define_historical_context)

- [draw_conclusions](#draw_conclusions)

- [identify_key_factors](#identify_key_factors)

- [synthesize_influences](#synthesize_influences)



---

## analyze_cultural_influences

### Description
Investigate the cultural factors that shaped the historical event or period.

### Conceptual Info

This node transforms the list of cultural factors identified by its parent into a structured, scored representation that highlights each factor's category, description, influence magnitude, and overall significance.

### Docstring

**Summary:** Analyze cultural influences for a historical event and return detailed scores and descriptors.

**Parameters:**

- cultural_factors (List[str]): List of cultural factor names produced by the identify_key_factors node.
**Returns:** dict - Dictionary containing the keys 'cultural_factors', 'factor_categories', 'factor_descriptions', 'influence_scores', and 'is_significant', each mapping to a list of equal length.

**Raises:**

- ValueError: Raised if the input list is empty or contains non-string elements.
**Examples:**

```python
>>> result = analyze_cultural_influences(['Romanticism', 'Buddhism'])
>>> print(result['cultural_factors'])
>>> print(result['factor_categories'])
>>> print(result['influence_scores'])
>>> print(result['is_significant'])
["Romanticism", "Buddhism"]
["Artistic movement", "Religious belief"]
[0.8, 0.6]
[True, True]
```

```python
>>> try:
...     analyze_cultural_influences([])
>>> except ValueError as e:
...     print(e)
"No cultural factors provided. At least one is required."
```



---

## analyze_economic_influences

### Description
Assess the economic factors that contributed to the historical event or period.

### Conceptual Info

Transforms a list of economic factors identified by the parent node into a structured assessment that quantifies each factor's influence on the historical event.

### Docstring

**Summary:** Analyzes each economic factor from the input list and returns a structured assessment of its impact on the historical event or period.

**Parameters:**

- economic_factors (List[str]): List of economic factors identified by the `identify_key_factors` node.
**Returns:** List[Dict[str, Any]] - A list of dictionaries, each containing structured information about an economic factor.

**Raises:**

- ValueError: Raised when the `economic_factors` list is empty.
- TypeError: Raised when `economic_factors` is not a list of strings.
**Examples:**

```python
>>> analyze_economic_influences(['Inflation', 'Trade Embargo'])
[{'economic_factor_name': 'Inflation', 'impact_summary': 'High inflation reduced purchasing power and disrupted domestic markets.', 'evidence_sources': ['Economic Report 1931', 'Historical GDP Data'], 'impact_strength': 0.85, 'time_period_affected': '1931-1933', 'is_consensus': True}, {'economic_factor_name': 'Trade Embargo', 'impact_summary': 'The embargo limited exports, weakening the national economy.', 'evidence_sources': ['Trade Records 1940', 'Diplomatic Correspondence'], 'impact_strength': 0.70, 'time_period_affected': '1940-1945', 'is_consensus': False}]
```

```python
>>> analyze_economic_influences(['Industrial Production Growth'])
[{'economic_factor_name': 'Industrial Production Growth', 'impact_summary': 'Rapid industrial growth fueled wartime manufacturing.', 'evidence_sources': ['Industrial Production Index 1944'], 'impact_strength': 0.90, 'time_period_affected': '1942-1945', 'is_consensus': True}]
```



---

## analyze_political_influences

### Description
Investigate the political factors that shaped the historical event or period.

### Conceptual Info

The node extracts and synthesizes the political dimensions—decisions, policies, and leadership—that directed the course of a historical event.

### Docstring

**Summary:** Generates a structured summary of the political influences affecting a historical event, based on primary political factors identified by the previous node.

**Parameters:**

- political_factors (List[str]): List of primary political factors (e.g., treaties, revolutions, wars) supplied by the identify_key_factors node.
**Returns:** Dict[str, Any] - A dictionary containing four keys:
- political_decisions: List of key decisions.
- policies_influenced: List of policies that were enacted.
- leadership_figures: List of main political leaders.
- summary: A concise narrative describing the political influence.

**Raises:**

- ValueError: Raised if political_factors is empty or None.
- TypeError: Raised if political_factors is not a list.
**Examples:**

```python
>>> result = analyze_political_influences([
...     'Treaty of Versailles',
...     'French Revolution',
...     'Napoleonic Wars'
>>> ])
>>> print(result['summary'])
"The Treaty of Versailles, the French Revolution, and the Napoleonic Wars collectively redefined European borders, governance structures, and international law, setting the stage for the modern nation-state system."
```

```python
>>> result = analyze_political_influences(['Industrial Revolution'])
>>> print(result['political_decisions'])
"['Industrial Revolution']"
```



---

## analyze_social_influences

### Description
Examine the social influences that contributed to the historical event or period.

### Conceptual Info

This node takes the social factors identified by its parent and assigns quantitative impact scores, counts them, and produces a narrative summary of their interaction in the context of the historical event.

### Docstring

**Summary:** Analyze the social influences on a historical event, assigning impact scores and summarizing their combined effect.

**Parameters:**

- input_social_factors (List[str]): List of primary social factors returned by the parent node `identify_key_factors`.
**Returns:** Dict[str, Any] - A dictionary containing the number of factors, the list of social factors, their impact scores, and a summary narrative.

**Raises:**

- ValueError: Raised when `input_social_factors` is empty or None.
**Examples:**

```python
>>> result = analyze_social_influences(["Women’s suffrage", "Urbanization"])
{"number_of_factors": 2, "social_factors": ["Women’s suffrage", "Urbanization"], "impact_scores": [0.8, 0.6], "summary": "Women’s suffrage and urbanization combined accelerated democratic reforms."}
```

```python
>>> result = analyze_social_influences(["Industrial labor strikes"])
{"number_of_factors": 1, "social_factors": ["Industrial labor strikes"], "impact_scores": [0.7], "summary": "Industrial labor strikes pressured governments to enact labor protections."}
```



---

## compile_historical_narrative

### Description
Construct a narrative that encapsulates the historical event or period and its shaping factors.

### Conceptual Info

This node synthesizes the analysis produced by the prior workflow stages into a single, coherent historical narrative. It takes the distilled conclusions, key factors, and impact assessments from the `draw_conclusions` node, and combines them with contextual details (e.g., event name, time frame) to produce a polished story that can be presented to end‑users.

### Docstring

**Summary:** Generate a full historical narrative from analysis outputs.

**Parameters:**

- conclusion_summary (str): Concise summary of the main conclusions about the key drivers and outcomes.
- key_factors (List[str]): List of primary factors identified as key drivers.
- impact_assessment (List[str]): Assessment of each factor's impact level (e.g., 'high', 'medium', 'low').
- confidence_score (float): Overall confidence level (0‑1) in the conclusions.
- recommendations (List[str]): Actionable recommendations or implications derived from the conclusions.
- historical_event (str): Name or title of the historical event or period being studied.
- time_frame (str): Approximate time range (e.g., years) of the event or period.
**Returns:** Dict[str, Any] - Dictionary containing narrative_title, introduction, historical_context, key_factors, impact_summary, conclusion, and overall_narrative.

**Raises:**

- ValueError: Raised when any required input is empty or missing.
**Examples:**

```python
>>> output = compile_historical_narrative(
...     conclusion_summary='The Industrial Revolution transformed labor and technology.',
...     key_factors=['Technological Innovation', 'Urbanization', 'Capital Accumulation'],
...     impact_assessment=['high', 'medium', 'high'],
...     confidence_score=0.92,
...     recommendations=['Study early factory labor laws.', 'Examine urban planning impact.'],
...     historical_event='Industrial Revolution',
...     time_frame='18th–19th centuries'"
                ")
>>> print(output['overall_narrative'])
"The Industrial Revolution: A Transformational Epoch\n\nThe Industrial Revolution, spanning the 18th–19th centuries, marked a profound shift in societal structure, fueled by Technological Innovation, Urbanization, and Capital Accumulation. These key drivers—each assessed as either high or medium impact—redefined labor, production, and urban life.\n\nThe analysis concludes that technological progress and capital flows were the dominant forces, with urbanization acting as a catalyst that accelerated change. The high confidence score of 0.92 underscores the robustness of these findings.\n\nImplications include a deeper study of early factory labor laws and the long-term effects of urban planning during this era.\n"
```

```python
>>> output = compile_historical_narrative(
...     conclusion_summary='The Fall of the Berlin Wall symbolized the end of the Cold War.',
...     key_factors=['Political Reform', 'Economic Strain', 'Public Protest'],
...     impact_assessment=['high', 'medium', 'high'],
...     confidence_score=0.88,
...     recommendations=['Investigate policy shifts post-1989.', 'Assess economic integration effects.'],
...     historical_event='Fall of the Berlin Wall',
...     time_frame='1989'"
                ")
>>> print(output['overall_narrative'])
"Fall of the Berlin Wall: The Collapse of Cold War Ideologies\n\nSet against the backdrop of 1989, the fall of the Berlin Wall marked the culmination of political reform, economic strain, and public protest in the Eastern Bloc. These key drivers—particularly the high-impact political reform and public protest—collectively accelerated the collapse of the Soviet sphere.\n\nThe narrative concludes that the political and social forces outweighed economic pressures, a finding reflected in the 0.88 confidence score.\n\nRecommendations for further study include a detailed examination of the policy shifts after 1989 and the economic integration outcomes that followed.\n"
```



---

## define_historical_context

### Description
Establish the historical period or event to be analyzed.

### Conceptual Info

Provides the foundational historical context needed for subsequent analyses.

### Docstring

**Summary:** Determines the historical event or period to be examined and returns its name and time frame.

**Returns:** Tuple[str, str] - A tuple containing the historical event name and its approximate time frame.

**Raises:**

- ValueError: Raised if the user fails to provide a valid event name or time frame.
**Examples:**

```python
>>> event, timeframe = define_historical_context()
>>> print(event)
>>> print(timeframe)
"Renaissance"
"14th–17th centuries"
```

```python
>>> event, timeframe = define_historical_context()
>>> assert event == "Industrial Revolution"
>>> assert timeframe == "late 18th–19th centuries"
"No output, assertions passed."
```



---

## draw_conclusions

### Description
Derive concise conclusions about how various social, economic, political, and cultural factors jointly shaped the historical event, including assessment of each factor’s impact, confidence level, and actionable recommendations.

### Conceptual Info

The node synthesizes the collective insights from social, economic, political, and cultural analyses into a coherent set of conclusions, providing a high‑level evaluation of drivers, impacts, confidence, and recommendations.

### Docstring

**Summary:** Generate a structured set of conclusions about a historical event based on synthesized influence data.

**Parameters:**

- synthesis (dict): Dictionary containing the outputs of `synthesize_influences`, including key insights and interaction points.
**Returns:** dict - Dictionary matching the `draw_conclusions` output structure.

**Raises:**

- ValueError: If `synthesis` is missing required keys or contains invalid data.
**Examples:**

```python
>>> synth = {
...     'social_insights': 'Social unrest spurred reforms.',
...     'economic_insights': 'Industrial growth fueled capital accumulation.',
...     'political_insights': 'New constitution centralized authority.',
...     'cultural_insights': 'Romanticism challenged traditional norms.',
...     'synthesis_summary': 'Multiple fronts converged to reshape governance.',
...     'interaction_points': ['Economic growth ↔ Political reform', 'Cultural shifts ↔ Social movements'],
...     'importance_scores': [0.8, 0.9, 0.7, 0.6]
>>> }
{
  'conclusion_summary': 'The era was driven by intertwined social, economic, political, and cultural forces that collectively accelerated institutional change.',
  'key_factors': ['Economic Growth', 'Political Reform', 'Social Unrest', 'Cultural Shifts'],
  'impact_assessment': ['high', 'high', 'medium', 'medium'],
  'confidence_score': 0.88,
  'recommendations': ['Focus on sustaining economic diversification', 'Encourage inclusive political dialogues', 'Support cultural initiatives that bridge tradition and innovation']
}
```

```python
>>> synth = {
...     'social_insights': 'Demographic shifts altered labor markets.',
...     'economic_insights': 'Trade embargoes disrupted supply chains.',
...     'political_insights': 'Leadership turnover destabilized governance.',
...     'cultural_insights': 'Artistic movements reflected societal tensions.',
...     'synthesis_summary': 'A fragile equilibrium existed between competing pressures.',
...     'interaction_points': ['Economic disruption ↔ Political instability'],
...     'importance_scores': [0.6, 0.7, 0.5, 0.4]
>>> }
{
  'conclusion_summary': 'Instability arose from the interplay of economic shocks, political turbulence, and cultural expression.',
  'key_factors': ['Trade Embargoes', 'Leadership Turnover', 'Demographic Shifts', 'Artistic Movements'],
  'impact_assessment': ['high', 'medium', 'medium', 'low'],
  'confidence_score': 0.72,
  'recommendations': ['Reform trade policies', 'Promote political stability mechanisms', 'Invest in social cohesion programs']
}
```



---

## identify_key_factors

### Description
Determine the key factors that influenced the historical event or period.

### Conceptual Info

The node aggregates high-level drivers—social, political, economic, and cultural—by synthesizing contextual data from the parent node. It produces a concise list of key factors that set the stage for subsequent influence analyses.

### Docstring

**Summary:** Identify the primary social, political, economic, and cultural factors that shaped a specific historical event or period.

**Parameters:**

- historical_event (str): The name or title of the historical event or period being studied.
- time_frame (str): Approximate time range of the event (e.g., years or dates).
**Returns:** Dict[str, List[str]] - A dictionary containing four lists of factor names, one for each domain: social, political, economic, and cultural.

**Raises:**

- ValueError: Raised when either `historical_event` or `time_frame` is empty or None.
**Examples:**

```python
>>> social_factors, political_factors, economic_factors, cultural_factors = identify_key_factors('French Revolution', '1789-1799')
>>> print('Social:', social_factors)
>>> print('Political:', political_factors)
Social: ['Monarchy', 'Social Inequality', 'Enlightenment Ideas']
Political: ['Absolute Monarchy', 'Reign of Terror', 'Constitutional Reforms']
```

```python
>>> factors = identify_key_factors('Renaissance', '1400-1600')
>>> print(factors['cultural_factors'])
['Humanism', 'Artistic Patronage', 'Scientific Curiosity']
```



---

## synthesize_influences

### Description
Combine the analyses of various social, political, economic, and cultural influences to produce a comprehensive synthesis, identifying how these factors interacted, where they converged, and their relative importance.

### Conceptual Info

This node aggregates the detailed findings from four distinct analytical modules—social, political, economic, and cultural—to produce a unified narrative of influence. It extracts salient themes, highlights cross‑sector interactions, and quantifies the relative weight of each sector in shaping the historical event.

### Docstring

**Summary:** Synthesize social, political, economic, and cultural analyses into a coherent set of insights.

**Parameters:**

- social_analysis (dict): Dictionary containing outputs from `analyze_social_influences`. Expected keys: `number_of_factors`, `social_factors`, `impact_scores`, `summary`.
- political_analysis (dict): Dictionary containing outputs from `analyze_political_influences`. Expected keys: `political_decisions`, `policies_influenced`, `leadership_figures`, `summary`.
- economic_analysis (dict): Dictionary containing outputs from `analyze_economic_influences`. Expected keys: `economic_factor_name`, `impact_summary`, `evidence_sources`, `impact_strength`, `time_period_affected`, `is_consensus`.
- cultural_analysis (dict): Dictionary containing outputs from `analyze_cultural_influences`. Expected keys: `cultural_factors`, `factor_categories`, `factor_descriptions`, `influence_scores`, `is_significant`.
**Returns:** dict - A dictionary with keys `social_insights`, `economic_insights`, `political_insights`, `cultural_insights`, `synthesis_summary`, `interaction_points`, and `importance_scores`.

**Raises:**

- ValueError: Raised if any required key is missing from one of the input analysis dictionaries.
**Examples:**

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

