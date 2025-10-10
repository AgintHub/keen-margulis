# _analyze_economic_influences - Complete PRD Documentation

## Overview
PRDs for nodes in the '_analyze_economic_influences' module.

## Table of Contents

- [validate_economic_factors_input](#validate_economic_factors_input)

- [analyze_factor_impact](#analyze_factor_impact)

- [gather_evidence_sources](#gather_evidence_sources)

- [format_evidence_sources](#format_evidence_sources)

- [calculate_impact_strength](#calculate_impact_strength)

- [determine_time_period_affected](#determine_time_period_affected)

- [check_scholarly_consensus](#check_scholarly_consensus)



---

## validate_economic_factors_input

### Description
Validates a list of economic factor names, ensuring each is a non-empty alphabetic string and returns the cleaned list.

### Conceptual Info

This shim sanitizes the list of economic factors passed from the identify_key_factors node, ensuring that downstream analysis receives only valid, clean factor names.

### Docstring

**Summary:** Validate and sanitize a list of economic factor names.

**Parameters:**

- factors (List[str]): List of raw economic factor names to validate.
**Returns:** List[str] - A cleaned list of valid economic factor names.

**Raises:**

- TypeError: If `factors` is not a list or contains non-string elements.
- ValueError: If any factor is empty or contains non-alphabetic characters.
**Examples:**

```python
>>> validate_economic_factors_input(['inflation', 'gdp', 'taxation'])
['inflation', 'gdp', 'taxation']
```

```python
>>> validate_economic_factors_input(['inflation', '123', 'gdp'])
ValueError: Factor '123' contains non-alphabetic characters.
```



---

## analyze_factor_impact

### Description
Returns a concise textual summary describing how a specified factor impacted a given historical context.

### Conceptual Info

This shim performs an interpretative analysis of a specified factor within a historical context, producing a brief descriptive summary that can be consumed by downstream nodes.

### Docstring

**Summary:** Analyzes the impact of a given factor on a specified historical context and returns a concise textual summary.

**Parameters:**

- factor_name (str): The name of the factor to analyze, e.g., an economic or social phenomenon.
- historical_context (str): A textual description of the time period or events relevant to the factor.
**Returns:** str - A short paragraph summarizing the factor’s influence on the provided historical context.

**Raises:**

- ValueError: Raised if either factor_name or historical_context is an empty string.
- TypeError: Raised if either factor_name or historical_context is not of type str.
**Examples:**

```python
>>> analyze_factor_impact('Great Depression', '1930s global economic downturn')
'The Great Depression severely reduced industrial production and led to widespread unemployment across the globe, prompting significant policy reforms.'
```

```python
>>> analyze_factor_impact('Industrial Revolution', '18th–19th century Europe')
'The Industrial Revolution transformed European societies by shifting production from manual labor to mechanized factories, which accelerated urbanization and altered social structures.'
```



---

## gather_evidence_sources

### Description
Collects a list of primary source references or data points supporting analysis of the specified economic factor.

### Conceptual Info

This shim emulates the retrieval of primary evidence sources—such as archival documents, journal articles, or statistical reports—that substantiate the impact analysis of an economic factor in historical research.

### Docstring

**Summary:** Retrieve a list of evidence sources for a given economic factor.

**Parameters:**

- factor_name (str): Name of the economic factor to retrieve evidence for.
**Returns:** list[str] - A list of strings, each representing a primary source reference or data point relevant to the factor.

**Raises:**

- ValueError: Raised when `factor_name` is an empty string.
- TypeError: Raised when `factor_name` is not a string.
**Examples:**

```python
>>> gather_evidence_sources('Industrial Revolution')
['Textbook: History of the Industrial Revolution', 'Archive: Factory Records 1815-1830', 'Journal Article: Economic Impact of Steam Power']
```

```python
>>> gather_evidence_sources('Great Depression')
['Government Report: 1933 Unemployment Statistics', 'Newspaper Archives: 1929 Stock Market Crash']
```



---

## format_evidence_sources

### Description
Formats a string of evidence source identifiers into a semicolon-separated, human‑readable format suitable for inclusion in analysis reports.

### Conceptual Info

Provides a reliable way to convert raw evidence source listings into a clean, report‑friendly format.

### Docstring

**Summary:** Formats raw evidence source strings into a standardized, human‑readable format.

**Parameters:**

- evidence_list (str): A string containing evidence source identifiers separated by commas, semicolons, or newlines.
**Returns:** str - A semicolon-separated string of evidence source identifiers.

**Raises:**

- ValueError: If evidence_list is empty or contains only whitespace.
- TypeError: If evidence_list is not a string.
**Examples:**

```python
>>> result = format_evidence_sources('Smith2020, Doe2019; Brown2021')
'Smith2020; Doe2019; Brown2021'
```

```python
>>> result = format_evidence_sources('Smith2020\nDoe2019\nBrown2021')
'Smith2020; Doe2019; Brown2021'
```



---

## calculate_impact_strength

### Description
Computes a numeric impact strength (0–1) for an economic factor based on its textual impact analysis.

### Conceptual Info

This shim evaluates the intensity of an economic factor's influence by converting qualitative analysis into a quantitative score.

### Docstring

**Summary:** Calculate a numeric strength rating (0–1) for an economic factor based on its impact analysis.

**Parameters:**

- factor_name (str): Name of the economic factor to evaluate.
- impact_analysis (str): Textual description of how the factor impacted the historical context.
**Returns:** float - A float between 0 and 1 representing the strength of the factor's impact.

**Raises:**

- ValueError: If either input is an empty string or missing.
- TypeError: If inputs are not of type str.
**Examples:**

```python
>>> strength = calculate_impact_strength(
...     factor_name='Inflation',
...     impact_analysis='High inflation led to widespread unemployment.'
>>> )
0.85
```

```python
>>> strength = calculate_impact_strength(
...     factor_name='Reform',
...     impact_analysis='Policy reform stabilized the economy.'
>>> )
0.6
```



---

## determine_time_period_affected

### Description
A function that returns the time period during which the specified economic factor was most influential.

### Conceptual Info

This shim estimates the most influential time period for an economic factor by analyzing the factor name and the surrounding historical context. It is used to populate the `time_period_affected` field in the economic influence analysis workflow.

### Docstring

**Summary:** Determine the most influential time period for a given economic factor based on historical context.

**Parameters:**

- factor_name (str): Name of the economic factor to analyze (e.g., "Great Depression").
- historical_context (str): Descriptive text or data that provides contextual background for the factor.
**Returns:** str - An ISO-formatted date range string (e.g., "1929-01-01 to 1939-12-31") representing the period during which the factor was most influential.

**Raises:**

- ValueError: Raised when either `factor_name` or `historical_context` is empty or missing.
- TypeError: Raised when either `factor_name` or `historical_context` is not of type `str`.
**Examples:**

```python
>>> result = determine_time_period_affected("Great Depression", "Economic downturn during the 1930s.")
>>> print(result)
"1929-01-01 to 1939-12-31"
```

```python
>>> result = determine_time_period_affected("Financial Crisis", "The 2007-2008 global credit crunch.")
>>> print(result)
"2007-01-01 to 2009-12-31"
```



---

## check_scholarly_consensus

### Description
Check if there is scholarly consensus for the specified economic factor name.

### Conceptual Info

The shim verifies whether academic literature agrees on the significance of a named economic factor, serving as a decision point in historical analysis pipelines.

### Docstring

**Summary:** Return a boolean indicating the presence of scholarly consensus on the significance of a specified economic factor.

**Parameters:**

- factor_name (str): The name of the economic factor to evaluate for scholarly consensus.
**Returns:** bool - True if a consensus exists, False otherwise.

**Raises:**

- ValueError: Raised when factor_name is an empty string.
- TypeError: Raised when factor_name is not of type str.
**Examples:**

```python
>>> check_scholarly_consensus('Inflation')
True
```

```python
>>> check_scholarly_consensus('UnusualEvent')
False
```

