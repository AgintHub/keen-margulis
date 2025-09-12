# preprocess_lyrics_text PRD

## Description
This shim takes a list of raw song lyrics and returns a list of cleaned, lowercased, punctuation‑removed, and whitespace‑normalized lyrics ready for sentiment analysis.


## Conceptual Info

Transforms raw lyric text into a standardized format for downstream natural language processing tasks such as sentiment analysis.

## Docstring

### Summary
Preprocess a list of song lyrics for sentiment analysis.

### Parameters

- **lyrics** (LIST_STR): A list of raw lyric strings.

### Returns

LIST_STR: A list of cleaned lyric strings.

### Raises

- ValueError: If `lyrics` is not a list of strings.

### Examples

```python
>>> cleaned = preprocess_lyrics_text(lyrics=["Hey!  ", "Good morning."])
>>> print(cleaned)
['hey', 'good morning']
```
