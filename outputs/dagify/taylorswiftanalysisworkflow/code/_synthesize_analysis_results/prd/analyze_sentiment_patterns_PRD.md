# analyze_sentiment_patterns PRD

## Description
Analyzes sentiment scores and an average sentiment value to generate a textual insight about sentiment patterns across songs.


## Conceptual Info

Provides sentiment‑based textual analysis for music lyric datasets.

## Docstring

### Summary
Generate insights from a list of sentiment scores and an average sentiment.

### Parameters

- **sentiment_scores** (List[float]): List of sentiment scores for each song.
- **average_sentiment** (float): Average sentiment score across all songs.

### Returns

str: Textual insight summarizing sentiment patterns.

### Raises

- ValueError: Raised when input lists are empty or contain non‑numeric values.

### Examples

```python
>>> sentiment_scores = [0.8, 0.6, 0.9, 0.4]
>>> average_sentiment = 0.675
>>> insight = analyze_sentiment_patterns(sentiment_scores, average_sentiment)
>>> print(insight)
"The overall sentiment trend is positive, with a moderate spread of scores, indicating consistent enthusiasm across the songs."
```
