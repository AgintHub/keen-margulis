# compile_historical_narrative PRD

## Description
Construct a narrative that encapsulates the historical event or period and its shaping factors.


## Conceptual Info

This node synthesizes the analysis produced by the prior workflow stages into a single, coherent historical narrative. It takes the distilled conclusions, key factors, and impact assessments from the `draw_conclusions` node, and combines them with contextual details (e.g., event name, time frame) to produce a polished story that can be presented to end‑users.

## Docstring

### Summary
Generate a full historical narrative from analysis outputs.

### Parameters

- **conclusion_summary** (str): Concise summary of the main conclusions about the key drivers and outcomes.
- **key_factors** (List[str]): List of primary factors identified as key drivers.
- **impact_assessment** (List[str]): Assessment of each factor's impact level (e.g., 'high', 'medium', 'low').
- **confidence_score** (float): Overall confidence level (0‑1) in the conclusions.
- **recommendations** (List[str]): Actionable recommendations or implications derived from the conclusions.
- **historical_event** (str): Name or title of the historical event or period being studied.
- **time_frame** (str): Approximate time range (e.g., years) of the event or period.

### Returns

Dict[str, Any]: Dictionary containing narrative_title, introduction, historical_context, key_factors, impact_summary, conclusion, and overall_narrative.

### Raises

- ValueError: Raised when any required input is empty or missing.

### Examples

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
