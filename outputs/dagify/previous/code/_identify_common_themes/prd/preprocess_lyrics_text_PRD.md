# preprocess_lyrics_text PRD

## Description
Preprocesses a list of raw song lyric strings into clean, tokenized, and lowercased text suitable for keyword extraction.


## Conceptual Info

Node responsible for preparing lyric texts for downstream analysis by standardizing format and removing noise.

## Docstring

### Summary
Preprocesses raw song lyrics.

### Parameters

- **lyrics** (List[str]): A list of raw lyric strings to be cleaned.

### Returns

List[str]: List of cleaned, tokenized lyric strings.

### Raises

- ValueError: Raised when the input list is empty or contains non-string elements.

### Examples

```python
>>> lyrics = ['Hello! This is a test.', 'Another line: with punctuation.']
>>> preprocessed = preprocess_lyrics_text(lyrics=lyrics)
>>> print(preprocessed)
['hello this is a test', 'another line with punctuation']
```
