# validate_lyrics_input PRD

## Description
Validates and sanitizes the input lyrics to ensure they are in the correct format and free of unsuitable content.


## Conceptual Info

This function performs input validation and sanitization to ensure lyrics are properly formatted for further analysis.

## Docstring

### Summary
Validates and sanitizes input song lyrics.

### Parameters

- **lyrics** (str): Raw song lyrics, potentially containing invalid or unsafe content.

### Returns

List[str]: A validated, sanitized list of song lyrics ready for further processing.

### Raises

- ValueError: Raised when the input lyrics are in an invalid or unsupported format.

### Examples

```python
>>> lyrics = '....'
>>> validated_lyrics = validate_lyrics_input(lyrics)
['Valid lyric line 1', 'Valid lyric line 2']
```
