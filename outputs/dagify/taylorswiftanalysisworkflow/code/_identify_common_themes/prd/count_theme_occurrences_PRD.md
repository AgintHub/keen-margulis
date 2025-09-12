# count_theme_occurrences PRD

## Description
Counts the occurrences of each theme keyword in the provided lyrics.


## Conceptual Info

The node normalizes text and performs token‑based frequency counting to support downstream theme analysis.

## Docstring

### Summary
Count the occurrences of each theme keyword in the given lyrics.

### Parameters

- **keywords** (str): Comma‑separated string of theme keywords to search for.
- **lyrics** (str): Text containing the song lyrics.

### Returns

str: A JSON string mapping each keyword to its frequency count in the lyrics.

### Raises

- ValueError: Raised if either `keywords` or `lyrics` is empty or None.

### Examples

```python
>>> result = count_theme_occurrences(keywords="love, heartbreak, hope", lyrics="I love you, I love you so much, but heartbreak will come")
>>> print(result)
{"love": 3, "heartbreak": 1, "hope": 0}
```
