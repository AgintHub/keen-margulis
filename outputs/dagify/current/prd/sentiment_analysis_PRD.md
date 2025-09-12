# sentiment_analysis PRD

## Description
Compute sentiment for each song.


## Conceptual Info

Performs sentiment analysis on song lyrics, producing a sentiment score for each track.

## Docstring

### Summary
Computes overall sentiment scores for a list of song lyrics, returning a list of floats between -1 and 1 aligned with song titles.

### Parameters

- **song_titles** (List[str]): List of song titles corresponding to the lyrics.
- **song_lyrics** (List[str]): List of full lyrics for each song.

### Returns

List[float]: Sentiment score for each song.

### Raises

- ValueError: If input lists are not the same length or are empty.

### Examples

```python
>>> scores = sentiment_analysis(["Love Story", "Bad Blood"], ["I knew you were trouble, so I stayed away", "I used to love you, now I hate you"])
[0.76, -0.62]
```

```python
>>> scores = sentiment_analysis(["Blank Space"], ["So nice I can't decide if I'm a love or a lie"])
[0.48]
```
