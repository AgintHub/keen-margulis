# analyze_individual_song_sentiments PRD

## Description
Computes a sentiment score for each song lyric in a list and returns a list of float scores.


## Conceptual Info

Provides a per-song sentiment analysis, enabling downstream aggregation and visualization of emotional tone across a collection of lyrics.

## Docstring

### Summary
Analyzes the sentiment of each song lyric in the input list and returns a corresponding list of sentiment scores.

### Parameters

- **lyrics** (List[str]): List of preprocessed song lyrics to analyze.

### Returns

List[float]: Sentiment scores for each input lyric.

### Raises

- ValueError: Raised when the input list is empty or contains invalid items.

### Examples

```python
>>> >>> from shim import analyze_individual_song_sentiments
>>> >>> lyrics = ["Love story, you got me like...", "I can't get no sleep..."],
>>> >>> scores = analyze_individual_song_sentiments(lyrics=lyrics)
>>> >>> print(scores)
[0.45, -0.12]
```
