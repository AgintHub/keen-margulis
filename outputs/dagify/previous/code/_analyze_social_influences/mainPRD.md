# _analyze_social_influences - Complete PRD Documentation

## Overview
PRDs for nodes in the '_analyze_social_influences' module.

## Table of Contents

- [validate_social_factors_input](#validate_social_factors_input)

- [calculate_impact_scores](#calculate_impact_scores)

- [count_social_factors](#count_social_factors)

- [format_factors_as_string](#format_factors_as_string)

- [calculate_average_impact](#calculate_average_impact)

- [generate_interaction_summary](#generate_interaction_summary)



---

## validate_social_factors_input

### Description
Validates and sanitizes a list of social factor strings, ensuring each entry meets formatting and content criteria.

### Conceptual Info

This shim acts as a gatekeeper for social factor inputs, ensuring data integrity before downstream analysis.

### Docstring

**Summary:** Validate and clean a list of social factor strings.

**Parameters:**

- factors (List[str]): A list of social factor strings to be validated and cleaned.
**Returns:** List[str] - The cleaned list of social factor strings, stripped of leading/trailing whitespace, de-duplicated, and in the original order.

**Raises:**

- ValueError: Raised if any factor is an empty string or contains disallowed characters.
- TypeError: Raised if `factors` is not a list or any element is not a string.
**Examples:**

```python
>>> validate_social_factors_input(['poverty', 'unemployment', 'poverty'])
["poverty", "unemployment"]
```

```python
>>> validate_social_factors_input(['poverty', ' ', 'infrastructure'])
ValueError: Invalid social factor: empty string or disallowed characters
```



---

## calculate_impact_scores

### Description
Calculates a normalized impact score for each provided social factor.

### Conceptual Info

This shim provides a mechanism to quantify the relative importance of social factors within a historical analysis, producing a score per factor that can be aggregated or compared.

### Docstring

**Summary:** Compute impact scores for each social factor.

**Parameters:**

- social_factors (list of str): A list of social factor names to evaluate.
**Returns:** list of float - A list of impact scores between 0.0 and 1.0, one per input factor.

**Raises:**

- ValueError: If the input list is empty.
- TypeError: If any element of the input is not a string.
**Examples:**

```python
>>> scores = calculate_impact_scores(['media coverage', 'public protest', 'policy change'])
>>> print(scores)
[0.78, 0.65, 0.92]
```

```python
>>> try:
...     calculate_impact_scores([])
>>> except ValueError as e:
...     print(e)
Input list of social factors must contain at least one element.
```



---

## count_social_factors

### Description
Counts the number of unique social factors provided in the input list.

### Conceptual Info

This shim tallies the distinct social factors supplied by earlier nodes, providing a concise integer count that downstream analyses use to quantify social influence.

### Docstring

**Summary:** Return the number of unique social factors from a list.

**Parameters:**

- factors (List[str]): A list of social factor names (strings) to be counted.
**Returns:** int - The count of distinct social factor names in the input list.

**Raises:**

- TypeError: Raised if `factors` is not an iterable of strings.
- ValueError: Raised if any element in `factors` is not a string.
**Examples:**

```python
>>> count_social_factors(['democracy', 'freedom', 'equality'])
3
```

```python
>>> count_social_factors(['democracy', 'freedom', 'democracy'])
2
```



---

## format_factors_as_string

### Description
Formats a list of factor names into a comma-separated string for human-readable output.

### Conceptual Info

The shim converts a list of factor identifiers into a single, human-readable string suitable for inclusion in reports or summaries.

### Docstring

**Summary:** Format a list of factor names into a comma-separated string.

**Parameters:**

- factors (List[str]): List of factor names to format into a single string.
**Returns:** str - A single string containing all factor names separated by commas and spaces.

**Raises:**

- ValueError: Raised when the input list is empty or contains non-string items.
- TypeError: Raised when the input is not a list.
**Examples:**

```python
>>> format_factors_as_string(['innovation', 'policy'])
'innovation, policy'
```

```python
>>> format_factors_as_string(['fact1', 'fact2', 'fact3'])
'fact1, fact2, fact3'
```



---

## calculate_average_impact

### Description
Calculates the mean of a list of individual impact scores and returns the result as a float.

### Conceptual Info

This shim provides a simple, reusable routine for computing the average impact of a set of social factors, ensuring consistent validation and error handling across the analytics pipeline.

### Docstring

**Summary:** Computes the mean of a list of individual impact scores, validating the input and raising informative errors for malformed data.

**Parameters:**

- scores (List[float]): A list of float values representing individual impact scores (expected range 0.0–1.0).
**Returns:** float - The average of the provided impact scores.

**Raises:**

- ValueError: Raised when the input list is empty.
- TypeError: Raised when the input is not a list or contains non‑float elements.
**Examples:**

```python
>>> calculate_average_impact([0.2, 0.5, 0.8])
0.5
```

```python
>>> calculate_average_impact([1.0, 0.9])
0.95
```



---

## generate_interaction_summary

### Description
Creates a concise narrative summarizing how the input social factors and their impact scores interact to shape a historical event.

### Conceptual Info

The shim generates a human-readable summary that captures the dynamic interplay among social factors and their quantified influence, enabling downstream components to convey complex analytical insights in accessible prose.

### Docstring

**Summary:** Generate a concise narrative that explains how a set of social factors and their impact scores interact to shape a historical event.

**Parameters:**

- factors (str): Comma‑separated list of social factor names (e.g., "migration,industrialization").
- scores (str): Comma‑separated list of corresponding impact scores as floats between 0.0 and 1.0 (e.g., "0.8,0.6").
**Returns:** str - A short narrative (≤3 sentences) describing how the listed factors interact to influence the historical event.

**Raises:**

- ValueError: If the number of factors does not match the number of scores, or if any score is outside the 0.0–1.0 range.
- TypeError: If either argument is not a string.
**Examples:**

```python
>>> generate_interaction_summary('migration,industrialization', '0.8,0.6')
"Industrialization and migration combined to reshape the urban landscape, driving economic growth and cultural exchange."
```

```python
>>> generate_interaction_summary('women_in_workforce,urbanization', '0.9,0.7')
"The rise of women in the workforce and rapid urbanization together propelled social mobility and reshaped community structures."
```

