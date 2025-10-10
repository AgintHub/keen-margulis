# format_evidence_sources PRD

## Description
Formats a string of evidence source identifiers into a semicolon-separated, human‑readable format suitable for inclusion in analysis reports.


## Conceptual Info

Provides a reliable way to convert raw evidence source listings into a clean, report‑friendly format.

## Docstring

### Summary
Formats raw evidence source strings into a standardized, human‑readable format.

### Parameters

- **evidence_list** (str): A string containing evidence source identifiers separated by commas, semicolons, or newlines.

### Returns

str: A semicolon-separated string of evidence source identifiers.

### Raises

- ValueError: If evidence_list is empty or contains only whitespace.
- TypeError: If evidence_list is not a string.

### Examples

```python
>>> result = format_evidence_sources('Smith2020, Doe2019; Brown2021')
'Smith2020; Doe2019; Brown2021'
```

```python
>>> result = format_evidence_sources('Smith2020\nDoe2019\nBrown2021')
'Smith2020; Doe2019; Brown2021'
```
