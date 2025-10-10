# _synthesize_influences - Complete PRD Documentation

## Overview
PRDs for nodes in the '_synthesize_influences' module.

## Table of Contents

- [validate_required_keys](#validate_required_keys)

- [extract_social_insights](#extract_social_insights)

- [extract_political_insights](#extract_political_insights)

- [extract_economic_insights](#extract_economic_insights)

- [extract_cultural_insights](#extract_cultural_insights)

- [identify_cross_sector_interactions](#identify_cross_sector_interactions)

- [calculate_relative_importance](#calculate_relative_importance)

- [generate_unified_narrative](#generate_unified_narrative)



---

## validate_required_keys

### Description
Validates that all required fields are present and non‑null in the social, political, economic, and cultural input data before synthesis.

### Conceptual Info

This shim ensures the integrity of the four influence analysis inputs by verifying that each required attribute exists and holds a value before proceeding to synthesize insights.

### Docstring

**Summary:** Validate the presence and non‑nullness of all required keys in the social, political, economic, and cultural input objects.

**Parameters:**

- social_input (Any): Instance of AnalyzeSocialInfluencesOutput containing social influence data.
- political_input (Any): Instance of AnalyzePoliticalInfluencesOutput containing political influence data.
- economic_input (Any): Instance of AnalyzeEconomicInfluencesOutput containing economic influence data.
- cultural_input (Any): Instance of AnalyzeCulturalInfluencesOutput containing cultural influence data.
**Returns:** str - A confirmation string, e.g., 'Validation passed', if all keys are present; otherwise a ValueError is raised.

**Raises:**

- ValueError: Raised when any required key is missing or its value is None.
- TypeError: Raised when an input argument is not an instance of the expected influence model.
**Examples:**

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



---

## extract_social_insights

### Description
Extracts a concise social insights summary from a social influence analysis model.

### Conceptual Info

The shim aggregates the quantified social factors from the analysis output into a readable narrative that can be consumed by higher‑level synthesis steps.

### Docstring

**Summary:** Generates a textual summary of social influence factors and their impact scores from a `AnalyzeSocialInfluencesOutput` object.

**Parameters:**

- social_analysis (AnalyzeSocialInfluencesOutput): Pydantic model containing the number of social factors, a comma‑separated list of factor names, a comma‑separated list of impact scores, and a summary narrative.
**Returns:** str - A concise paragraph that describes the most significant social factors, their relative impact scores, and how they together shaped the historical event.

**Raises:**

- ValueError: Raised if any required field in `social_analysis` is missing or empty.
- TypeError: Raised if `social_analysis` is not an instance of `AnalyzeSocialInfluencesOutput`.
**Examples:**

```python
>>> from your_module import AnalyzeSocialInfluencesOutput, extract_social_insights
>>> input_data = AnalyzeSocialInfluencesOutput(
...     number_of_factors=3,
...     social_factors='Public sentiment, Religious belief, Economic inequality',
...     impact_scores='0.7, 0.5, 0.6',
...     summary='Three key factors shaped the event.'
>>> )
>>> print(extract_social_insights(social_analysis=input_data))
"The dominant social forces were public sentiment (0.7), economic inequality (0.6) and religious belief (0.5), collectively driving the event’s trajectory."
```

```python
>>> # Handling an invalid input type
>>> try:
...     extract_social_insights(social_analysis='invalid type')
>>> except TypeError as e:
...     print(e)
"TypeError: social_analysis must be an instance of AnalyzeSocialInfluencesOutput"
```



---

## extract_political_insights

### Description
Extracts a concise string of key political insights from a structured political analysis.

### Conceptual Info

The shim processes a raw political analysis string to distill the most relevant political decisions, policies, and leadership figures into a single, concise summary suitable for downstream synthesis.

### Docstring

**Summary:** Extracts a concise summary of key political insights from the provided political analysis string.

**Parameters:**

- political_analysis (str): String containing structured political analysis details (e.g., decisions, policies, leaders).
**Returns:** str - A single string summarizing the most important political insights extracted from the input.

**Raises:**

- ValueError: Raised when the input string is empty or contains only whitespace.
- TypeError: Raised when the input is not of type 'str'.
**Examples:**

```python
>>> result = extract_political_insights(political_analysis='Key decisions: Peace Treaty; Policies: Arms Reduction; Leader: President X')
'Peace Treaty; Arms Reduction; President X'
```

```python
>>> result = extract_political_insights(political_analysis='No major political actions recorded.')
'No major political actions recorded.'
```



---

## extract_economic_insights

### Description
Extracts key economic insights from an AnalyzeEconomicInfluencesOutput input and returns a formatted summary string.

### Conceptual Info

This shim function takes structured economic influence data and produces a concise, human‑readable summary that can be used downstream for synthesis or reporting.

### Docstring

**Summary:** Generates a concise, human‑readable summary of economic factors from an AnalyzeEconomicInfluencesOutput instance.

**Parameters:**

- economic_analysis (AnalyzeEconomicInfluencesOutput): Pydantic model instance containing details of an economic factor analysis.
**Returns:** str - A single string summarizing the economic factor name, impact, evidence, impact strength, time period, and consensus status.

**Raises:**

- ValueError: Raised when required fields in the input model are missing or empty.
- TypeError: Raised when the input is not an instance of AnalyzeEconomicInfluencesOutput.
**Examples:**

```python
>>> economic_data = AnalyzeEconomicInfluencesOutput(economic_factor_name='Industrial Production', impact_summary='Increase in production led to inflation', evidence_sources='Data from 1920 Census', impact_strength=0.8, time_period_affected='1920-1925', is_consensus=True)
>>> print(extract_economic_insights(economic_analysis=economic_data))
"Economic Factor: Industrial Production; Impact: Increase in production led to inflation; Evidence: Data from 1920 Census; Impact Strength: 0.8; Time Period: 1920-1925; Consensus: Yes"
```

```python
>>> economic_data = AnalyzeEconomicInfluencesOutput(economic_factor_name='Trade Imbalance', impact_summary='Exports outpaced imports', evidence_sources='World Bank 2000', impact_strength=0.6, time_period_affected='2000-2005', is_consensus=False)
>>> print(extract_economic_insights(economic_analysis=economic_data))
"Economic Factor: Trade Imbalance; Impact: Exports outpaced imports; Evidence: World Bank 2000; Impact Strength: 0.6; Time Period: 2000-2005; Consensus: No"
```



---

## extract_cultural_insights

### Description
Extracts key cultural insights from the provided analysis and returns them as a concise textual summary.

### Conceptual Info

This shim receives a narrative analysis of cultural influences, distills the most relevant factors and their impacts, and outputs a human‑readable summary to be incorporated into higher‑level synthesis.

### Docstring

**Summary:** Extract key cultural insights from the given analysis and return a concise summary string.

**Parameters:**

- cultural_analysis (str): Textual analysis containing information about cultural factors, categories, descriptions, influence scores, and significance flags.
**Returns:** str - A concise textual summary that highlights the most significant cultural factors and their estimated influence on the historical event.

**Raises:**

- ValueError: Raised if the input string is empty or does not contain any discernible cultural factors.
- TypeError: Raised if the input is not of type str.
**Examples:**

```python
>>> analysis = "Cultural analysis: The Renaissance brought new artistic movements and philosophical ideas, influencing societal values and language trends."
>>> summary = extract_cultural_insights(analysis)
>>> print(summary)
"The Renaissance introduced artistic movements and philosophical ideas that reshaped societal values and language trends, significantly influencing the period."
```

```python
>>> analysis = "Cultural analysis: Minimal cultural influence noted; no distinct factors identified."
>>> summary = extract_cultural_insights(analysis)
>>> print(summary)
"No significant cultural factors identified; cultural influence is minimal."
```



---

## identify_cross_sector_interactions

### Description
Identifies key interaction points where social, political, economic, and cultural influences intersect, returning them as a list of descriptive strings.

### Conceptual Info

This shim aggregates insights from separate influence analyses to pinpoint moments where multiple social, political, economic, and cultural factors converge, providing a concise set of interaction points for further synthesis.

### Docstring

**Summary:** Extracts a list of cross‑sector interaction points from comprehensive influence analyses.

**Parameters:**

- social_data (str): String representation of the output from social influence analysis.
- political_data (str): String representation of the output from political influence analysis.
- economic_data (str): String representation of the output from economic influence analysis.
- cultural_data (str): String representation of the output from cultural influence analysis.
**Returns:** LIST_STR - A list of strings, each describing an interaction point where two or more influence categories intersect.

**Raises:**

- ValueError: If any of the input strings are empty or missing required markers.
- TypeError: If any of the inputs are not of type str.
**Examples:**

```python
>>> output = identify_cross_sector_interactions(
...     social_data='Population growth, migration patterns',
...     political_data='New tax policy',
...     economic_data='Recession',
...     cultural_data='Artistic movements'
>>> )
['Migration patterns influenced by new tax policy', 'Economic recession impacts cultural movements']
```

```python
>>> output = identify_cross_sector_interactions(
...     social_data='Community solidarity',
...     political_data='Civil rights legislation',
...     economic_data='Job creation programs',
...     cultural_data='Music festivals'
>>> )
['Community solidarity bolstered by civil rights legislation', 'Job creation programs enhance cultural music festivals']
```



---

## calculate_relative_importance

### Description
Computes a normalized list of four floats representing the relative importance of social, political, economic, and cultural influences based on their respective analysis outputs.

### Conceptual Info

This shim aggregates the impact assessments from the four influence categories into a single weight vector that can be used by downstream synthesis functions to balance their contributions in narrative generation.

### Docstring

**Summary:** Calculate the relative importance of social, political, economic, and cultural influence categories.

**Parameters:**

- social_input (AnalyzeSocialInfluencesOutput): Pydantic model containing social influence analysis results.
- political_input (AnalyzePoliticalInfluencesOutput): Pydantic model containing political influence analysis results.
- economic_input (AnalyzeEconomicInfluencesOutput): Pydantic model containing economic influence analysis results.
- cultural_input (AnalyzeCulturalInfluencesOutput): Pydantic model containing cultural influence analysis results.
**Returns:** List[float] - A list of four floats (social, political, economic, cultural) that sum to 1.0.

**Raises:**

- ValueError: Raised when any of the input models lack required data or produce an invalid weight distribution.
- TypeError: Raised when the provided arguments are not instances of the expected Pydantic models.
**Examples:**

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



---

## generate_unified_narrative

### Description
Creates a single cohesive narrative by combining social, political, economic, and cultural insights along with their interaction points.

### Conceptual Info

The generate_unified_narrative shim synthesizes insights from multiple domains—social, political, economic, and cultural—into a single, coherent historical narrative, using identified interaction points to show how these influences converged.

### Docstring

**Summary:** Generates a unified historical narrative from social, political, economic, cultural insights and their interaction points.

**Parameters:**

- social_insights (str): Key findings distilled from the social influence analysis.
- political_insights (str): Key findings distilled from the political influence analysis.
- economic_insights (str): Key findings distilled from the economic influence analysis.
- cultural_insights (str): Key findings distilled from the cultural influence analysis.
- interactions (List[str]): List of key interaction points where multiple influences converged.
**Returns:** str - A single string containing a cohesive historical narrative that integrates all provided insights and interactions.

**Raises:**

- ValueError: Raised if any string parameter is empty or None, or if interactions is not a list.
- TypeError: Raised if the types of any parameters do not match the expected types.
**Examples:**

```python
>>> generate_unified_narrative(
...     social_insights='Social factors influence migration patterns.',
...     political_insights='Political decisions shape policy.',
...     economic_insights='Economic pressures drive market changes.',
...     cultural_insights='Cultural norms shape behavior.',
...     interactions=['Interaction 1', 'Interaction 2']
>>> )
'Unified narrative combining the insights and interactions.'
```

```python
>>> output = generate_unified_narrative(
...     social_insights='The rise of industrialization led to urban migration.',
...     political_insights='The new constitution restructured governance.',
...     economic_insights='Trade tariffs spurred local production.',
...     cultural_insights='Art movements reflected societal change.',
...     interactions=['Industrialization spurred migration', 'Constitution influenced trade policies']
>>> )
>>> print(output)
'The industrialization-driven migration reshaped society, while the new constitution and trade tariffs fostered economic growth and cultural expression, illustrating the intertwined forces of history.'
```

