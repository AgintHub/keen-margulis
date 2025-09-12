# validate_lyrics_input PRD

## Description
Validates and normalizes raw song lyric strings into a clean list of lines.


## Conceptual Info

The shim performs basic text sanitation and validation for lyrics data before further analysis.

## Docstring

### Summary
Validate and clean raw song lyrics.

### Parameters

- **lyrics** (str): Raw lyric string that may contain newlines, extraneous whitespace, or non‑ASCII characters.

### Returns

List[str]: A list of cleaned lyric lines ready for downstream processing.

### Raises

- ValueError: Raised when the input string is empty or contains only whitespace.

### Examples

```python
>>> lyrics = "  Verse one\n\n Chorus   "
>>> cleaned = validate_lyrics_input(lyrics)
['Verse one', 'Chorus']
```
