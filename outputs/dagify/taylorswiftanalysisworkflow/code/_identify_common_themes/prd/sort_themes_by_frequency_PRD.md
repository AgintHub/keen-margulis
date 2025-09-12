# sort_themes_by_frequency PRD

## Description
Sorts a dictionary of theme counts into a list of theme names ordered from most to least frequent.


## Conceptual Info

Transforms raw theme-frequency mappings into a sorted list for downstream analysis.

## Docstring

### Summary
Sort a theme frequency dictionary into a descending order list.

### Parameters

- **theme_counts** (str): A JSON-encoded string representing a dictionary where keys are theme strings and values are integer counts.

### Returns

list[str]: A list of theme names sorted by decreasing frequency.

### Raises

- ValueError: If the input JSON is invalid or not a dictionary of string–int pairs.

### Examples

```python
>>> input_json = '{"love": 15, "heartbreak": 8, "growth": 12}'
>>> sorted_themes = sort_themes_by_frequency(theme_counts=input_json)
>>> print(sorted_themes)
["love", "growth", "heartbreak"]
```
