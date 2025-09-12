# analyze_lyrics_sentiment PRD

## Description
Analyze the sentiment of Taylor Swift's song lyrics.


## Conceptual Info

This node analyzes the sentiment of Taylor Swift's song lyrics to determine the overall emotional tone.

## Docstring

### Summary
Analyzes the sentiment of Taylor Swift's song lyrics.

### Parameters

- **song_lyrics** (List[str]): List of song lyrics from Taylor Swift's discography, obtained from the 'gather_taylor_swift_data' node.

### Returns

{'sentiment_scores': List[float], 'average_sentiment': float}: A dictionary containing a list of sentiment scores for each song and the average sentiment score across all songs.

### Raises

- ValueError: If the input 'song_lyrics' is empty or not a list of strings.

### Examples

```python
>>> song_lyrics = ['I stay out too late, got nothing in my brain', 'I think I got a broken heart']
>>> result = analyze_lyrics_sentiment(song_lyrics)
>>> print(result)
{'sentiment_scores': [0.2, -0.5], 'average_sentiment': -0.15}
```

```python
>>> song_lyrics = ['You took the time to memorize me, my fears, my hopes, and dreams']
>>> result = analyze_lyrics_sentiment(song_lyrics)
>>> print(result)
{'sentiment_scores': [0.8], 'average_sentiment': 0.8}
```
