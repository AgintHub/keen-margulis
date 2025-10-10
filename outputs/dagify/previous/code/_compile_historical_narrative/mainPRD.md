# _compile_historical_narrative - Complete PRD Documentation

## Overview
PRDs for nodes in the '_compile_historical_narrative' module.

## Table of Contents

- [validate_required_inputs](#validate_required_inputs)

- [generate_narrative_title](#generate_narrative_title)

- [create_introduction](#create_introduction)

- [build_historical_context](#build_historical_context)

- [format_key_factors_for_narrative](#format_key_factors_for_narrative)

- [synthesize_impact_summary](#synthesize_impact_summary)

- [craft_narrative_conclusion](#craft_narrative_conclusion)

- [compile_full_narrative](#compile_full_narrative)



---

## validate_required_inputs

### Description
Validates that all provided required inputs are non-empty and raises an error if any are missing.

### Conceptual Info

Ensures downstream nodes receive all necessary data by validating presence and non-emptiness of required inputs.

### Docstring

**Summary:** Checks that each supplied argument is present and not empty, raising an error if validation fails.

**Parameters:**

- inputs (Any): One or more values to validate. Accepts positional arguments.
**Returns:** str - A confirmation string 'All inputs are valid.' when validation passes.

**Raises:**

- ValueError: Raised when any input is None or an empty string.
- TypeError: Raised when the input type is not supported by the validation logic.
**Examples:**

```python
>>> validate_required_inputs('summary', 'EventName', '2020-2021')
'All inputs are valid.'
```

```python
>>> validate_required_inputs('', 'EventName', '2020-2021')
ValueError('One or more inputs are missing or empty.')
```



---

## generate_narrative_title

### Description
Generates a concise title for a historical narrative based on the given event and time frame.

### Conceptual Info

This shim creates a compelling, concise title for a historical narrative, ensuring the title reflects both the event and its temporal context. The title is later used as the headline of the compiled narrative.

### Docstring

**Summary:** Generate a concise title for a historical narrative based on the provided event and time frame.

**Parameters:**

- event (str): The name or description of the historical event to be narrated.
- time_frame (str): The temporal scope of the event (e.g., '1939-1945', '18th century').
**Returns:** str - A string title that is no longer than 10 words, incorporates the event and time frame, and is suitable for use as a headline in a historical narrative.

**Raises:**

- ValueError: Raised if either `event` or `time_frame` is an empty string.
- TypeError: Raised if either `event` or `time_frame` is not of type `str`.
**Examples:**

```python
>>> title = generate_narrative_title(event='The French Revolution', time_frame='1789-1799')
"French Revolution (1789-1799): A Turning Point"
```

```python
>>> title = generate_narrative_title(event='World War II', time_frame='1939-1945')
"World War II (1939-1945): The Global Conflict"
```



---

## create_introduction

### Description
Generates an introductory paragraph for a historical narrative based on the event, time frame, and a contextual summary.

### Conceptual Info

The `create_introduction` shim is responsible for converting a historical event, its time frame, and a high‑level contextual summary into a coherent, engaging introductory paragraph that sets the stage for the full narrative.

### Docstring

**Summary:** Creates an introduction paragraph for a historical narrative.

**Parameters:**

- event (str): The name or description of the historical event.
- time_frame (str): The period or time frame during which the event occurred.
- context (str): A concise summary of key conclusions or background that should inform the introduction.
**Returns:** str - An introductory paragraph that introduces the event, its time frame, and incorporates the provided context.

**Raises:**

- ValueError: Raised when any of the input parameters are empty strings.
- TypeError: Raised when any of the input parameters are not of type `str`.
**Examples:**

```python
>>> intro = create_introduction(
...     event='Fall of the Berlin Wall',
...     time_frame='1989',
...     context='The fall of the Berlin Wall marked a pivotal moment in the end of the Cold War.'
>>> )
"The Fall of the Berlin Wall in 1989 marked a pivotal moment, symbolizing the unraveling of the Cold War and the reunification of East and West Germany."
```

```python
>>> intro = create_introduction(
...     event='Moon Landing',
...     time_frame='1969',
...     context='Apollo 11 was the first crewed mission to land humans on the Moon, showcasing technological prowess and inspiring global ambition.'
>>> )
"In July 1969, the Apollo 11 mission achieved the historic first human landing on the Moon, epitomizing the height of space exploration and inspiring generations worldwide."
```



---

## build_historical_context

### Description
Produces a concise historical context summary from an event, time frame and list of influencing factors.

### Conceptual Info

This shim encapsulates the complex logic needed to transform event metadata and key factors into a readable historical context paragraph, enabling downstream narrative construction without exposing internal implementation details.

### Docstring

**Summary:** Generates a concise historical context summary based on the specified event, time frame, and key influencing factors.

**Parameters:**

- event (str): Name or description of the historical event.
- time_frame (str): Temporal range or period relevant to the event.
- factors (List[str]): List of key factors (e.g., cultural, economic, political, social) that influenced the event.
**Returns:** str - A single string containing a coherent historical context paragraph.

**Raises:**

- ValueError: Raised when any required argument is missing or empty.
- TypeError: Raised when arguments are of incorrect type (e.g., non-string event/time_frame or non-list factors).
**Examples:**

```python
>>> build_historical_context(event='Industrial Revolution',
...                      time_frame='18th-19th centuries',
...                      factors=['technological innovation', 'economic growth'])
"The Industrial Revolution, spanning the late 18th to early 19th centuries, was propelled by rapid technological innovations such as the steam engine and significant economic expansion, reshaping societies across Europe and North America."
```

```python
>>> build_historical_context(event='Fall of the Berlin Wall',
...                      time_frame='1989',
...                      factors=['political reform', 'economic stagnation', 'public protest'])
"In 1989, the Berlin Wall fell amid sweeping political reforms, severe economic stagnation, and widespread public protests, marking a pivotal moment in the end of the Cold War."
```



---

## format_key_factors_for_narrative

### Description
Formats a list of key factors and corresponding impact assessments into narrative-friendly strings for inclusion in a historical narrative.

### Conceptual Info

This shim takes the raw list of key factors identified by the analysis node along with their impact assessments, and converts them into a human-readable, narrative-friendly format suitable for embedding in historical narratives.

### Docstring

**Summary:** Formats key factors and impact assessments into narrative-friendly strings for use in a historical narrative.

**Parameters:**

- factors (List[str]): List of key factor names extracted from the analysis.
- assessments (List[str]): List of impact assessments (e.g., 'high', 'medium', 'low') corresponding to each factor.
**Returns:** List[str] - A list where each element is a string in the form '<factor>: <assessment> impact', ready for narrative inclusion.

**Raises:**

- ValueError: Raised when the lengths of `factors` and `assessments` differ or when either list is empty.
- TypeError: Raised when `factors` or `assessments` are not lists of strings.
**Examples:**

```python
>>> format_key_factors_for_narrative(factors=['Economy', 'Culture'], assessments=['high', 'medium'])
['Economy: high impact', 'Culture: medium impact']
```

```python
>>> format_key_factors_for_narrative(factors=['Infrastructure'], assessments=['low'])
['Infrastructure: low impact']
```



---

## synthesize_impact_summary

### Description
Creates a concise textual summary of how listed factors, with their impact assessments, collectively influence an event, incorporating an overall conclusion.

### Conceptual Info

The synthesize_impact_summary shim aggregates factor names and their corresponding impact assessments into a cohesive narrative, appending the overarching conclusion to produce a ready‑to‑use impact summary for historical storytelling.

### Docstring

**Summary:** Generates a concise impact summary string from a list of factors, their impact assessments, and an overall conclusion.

**Parameters:**

- factors (List[str]): List of primary factors influencing the event.
- assessments (List[str]): List of impact levels (e.g., 'high', 'medium', 'low') corresponding to each factor.
- conclusion (str): Overall conclusion statement to be appended to the summary.
**Returns:** str - A single string that summarizes the impact of each factor with its assessment and incorporates the overall conclusion.

**Raises:**

- ValueError: Raised when the lengths of `factors` and `assessments` do not match.
- TypeError: Raised when any input is of an incorrect type.
**Examples:**

```python
>>> synthesize_impact_summary(factors=['f1', 'f2'], assessments=['high', 'low'], conclusion='Overall impact is significant.')
'Factors f1 (high) and f2 (low) dominated the event; overall impact: Overall impact is significant.'
```

```python
>>> synthesize_impact_summary(factors=['policy change'], assessments=['medium'], conclusion='The policy shift altered the trajectory.')
'Factor policy change (medium) influenced the event; overall impact: The policy shift altered the trajectory.'
```



---

## craft_narrative_conclusion

### Description
Creates a narrative conclusion paragraph that integrates confidence level, actionable recommendations, and a summary of findings.

### Conceptual Info

The shim generates a cohesive narrative conclusion that reflects the overall confidence in the analysis, outlines actionable recommendations, and summarizes key findings for inclusion in a historical narrative.

### Docstring

**Summary:** Generates a narrative conclusion paragraph from confidence, recommendations, and summary inputs.

**Parameters:**

- confidence (float): Overall confidence level (0-1) in the conclusions.
- recommendations (List[str]): List of actionable recommendations or implications derived from the conclusions.
- summary (str): Concise summary of the main conclusions about the key drivers and outcomes.
**Returns:** str - A single paragraph string that presents the narrative conclusion, integrating confidence, recommendations, and the summary.

**Raises:**

- ValueError: Raised when any required input is missing or invalid.
- TypeError: Raised when input types do not match the expected types.
**Examples:**

```python
>>> conclusion = craft_narrative_conclusion(
...     confidence=0.85,
...     recommendations=['Expand data collection'],
...     summary='The analysis indicates a strong link between policy changes and economic growth.'
>>> )
'Conclusion: With a confidence level of 0.85, the analysis confirms a strong link between policy changes and economic growth, suggesting that expanding data collection will further substantiate these findings.'
```

```python
>>> conclusion = craft_narrative_conclusion(
...     confidence=0.4,
...     recommendations=['Reevaluate methodology', 'Gather additional evidence'],
...     summary='Initial findings are inconclusive regarding the impact of the event.'
>>> )
'Conclusion: Confidence is modest at 0.4, and while the initial findings remain inconclusive, it is recommended to reevaluate the methodology and gather additional evidence to clarify the event's impact.'
```



---

## compile_full_narrative

### Description
Compiles a cohesive narrative string from title, introduction, context, impact, and conclusion components.

### Conceptual Info

This shim function is responsible for assembling the final narrative text that will be returned to the user. It takes discrete narrative components produced by earlier nodes and stitches them together in a logically ordered, readable format.

### Docstring

**Summary:** Compile a full narrative string from separate parts.

**Parameters:**

- title (str): The title of the narrative.
- intro (str): Introductory paragraph setting the scene.
- context (str): Summary of the historical context.
- impact (str): Summary of how key factors impacted the event.
- conclusion (str): Concluding remarks linking the narrative to the conclusions.
**Returns:** str - A single string containing the title, introduction, context, impact, and conclusion, each separated by a newline.

**Raises:**

- ValueError: Raised if any input string is empty or missing.
- TypeError: Raised if any input is not of type str.
**Examples:**

```python
>>> result = compile_full_narrative(
...     title='Historical Event',
...     intro='In the year 1914, tensions rose across Europe.',
...     context='The global tensions were high as alliances formed.',
...     impact='These tensions led to the outbreak of war.',
...     conclusion='Thus, the outcome was the start of a global conflict.'
>>> )
>>> print(result)
Historical Event\nIn the year 1914, tensions rose across Europe.\nThe global tensions were high as alliances formed.\nThese tensions led to the outbreak of war.\nThus, the outcome was the start of a global conflict.
```

```python
>>> try:
...     compile_full_narrative(title='', intro='Intro', context='Context', impact='Impact', conclusion='Conclusion')
>>> except ValueError as e:
...     print(e)
All narrative components must be non-empty strings.
```

