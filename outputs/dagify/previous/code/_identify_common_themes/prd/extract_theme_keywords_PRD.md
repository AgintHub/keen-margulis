# extract_theme_keywords PRD

## Description
Extracts a list of theme keywords from the provided song lyrics.


## Conceptual Info

The node performs keyword extraction on song lyrics to identify recurring themes, enabling downstream analytics such as theme frequency calculation.

## Docstring

### Summary
Extract theme keywords from song lyrics.

### Parameters

- **lyrics** (str): Raw song lyrics to process.

### Returns

List[str]: A list of extracted theme keywords.

### Raises

- ValueError: If the input lyrics string is empty or not a string.

### Examples

```python
>>> lyrics = "Love, heartbreak, and resilience in a quiet town."
>>> keywords = extract_theme_keywords(lyrics)
>>> print(keywords)
['love', 'heartbreak', 'resilience', 'quiet', 'town']
```
