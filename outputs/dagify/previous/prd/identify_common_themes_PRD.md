# identify_common_themes PRD

## Description
Identify common themes in Taylor Swift's lyrics.


## Conceptual Info

This node analyzes the collected song lyrics to identify recurring themes or topics, providing insights into Taylor Swift's common lyrical motifs.

## Docstring

### Summary
Identify common themes in Taylor Swift's lyrics by analyzing the collected song lyrics.

### Parameters

- **song_lyrics** (List[str]): List of song lyrics from Taylor Swift's discography, provided by the 'gather_taylor_swift_data' node.

### Returns

{'themes': List[str], 'theme_frequencies': List[int]}: A dictionary containing a list of common themes and their corresponding frequencies.

### Raises

- ValueError: If the input 'song_lyrics' is empty or not a list of strings.

### Examples

```python
>>> song_lyrics = ['Love is in the air', 'Heartbreak is hard', 'Love is sweet']
>>> themes, theme_frequencies = identify_common_themes(song_lyrics)
>>> print(themes)
>>> print(theme_frequencies)
['love', 'heartbreak']
[2, 1]
```
