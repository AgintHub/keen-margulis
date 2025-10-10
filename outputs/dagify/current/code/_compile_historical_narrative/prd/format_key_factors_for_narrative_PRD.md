# format_key_factors_for_narrative PRD

## Description
Formats a list of key factors and corresponding impact assessments into narrative-friendly strings for inclusion in a historical narrative.


## Conceptual Info

This shim takes the raw list of key factors identified by the analysis node along with their impact assessments, and converts them into a human-readable, narrative-friendly format suitable for embedding in historical narratives.

## Docstring

### Summary
Formats key factors and impact assessments into narrative-friendly strings for use in a historical narrative.

### Parameters

- **factors** (List[str]): List of key factor names extracted from the analysis.
- **assessments** (List[str]): List of impact assessments (e.g., 'high', 'medium', 'low') corresponding to each factor.

### Returns

List[str]: A list where each element is a string in the form '<factor>: <assessment> impact', ready for narrative inclusion.

### Raises

- ValueError: Raised when the lengths of `factors` and `assessments` differ or when either list is empty.
- TypeError: Raised when `factors` or `assessments` are not lists of strings.

### Examples

```python
>>> format_key_factors_for_narrative(factors=['Economy', 'Culture'], assessments=['high', 'medium'])
['Economy: high impact', 'Culture: medium impact']
```

```python
>>> format_key_factors_for_narrative(factors=['Infrastructure'], assessments=['low'])
['Infrastructure: low impact']
```
