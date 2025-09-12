# extract_frequencies_for_themes PRD

## Description
A shim that converts a thematic frequency mapping into a list of integer frequencies aligned to the provided themes.


## Conceptual Info

Extracts an ordered list of frequencies for the provided themes by consulting a serialized theme_counts mapping and returns the frequencies as a List[int].

## Docstring

### Summary
Compute frequencies for themes from a serialized theme-to-count mapping and return them as a list aligned with the input themes.

### Parameters

- **themes** (STR): Serialized representation of the list of themes (e.g., a delimited string or JSON string); in practice, this input provides the order of themes for which frequencies are requested.
- **theme_counts** (STR): Serialized mapping from theme to its frequency count; used to look up counts for each theme in 'themes'.

### Returns

LIST_INT: A list of integer frequencies corresponding to each theme in 'themes' in the same order.

### Raises

- ValueError: Raised if themes cannot be parsed or if a theme is missing from the theme_counts mapping.
- TypeError: Raised if inputs are not strings when expected.

### Examples

```python
>>> themes = 'happy|sad|nostalgic'
>>> theme_counts = '{"happy": 5, "sad": 2, "nostalgic": 3}'
>>> result = extract_frequencies_for_themes(themes, theme_counts)
[5, 2, 3]
```
