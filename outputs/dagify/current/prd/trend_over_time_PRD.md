# trend_over_time PRD

## Description
Summarize sentiment trend across release years.


## Conceptual Info

This node aggregates song-level sentiment scores into year-level averages, providing a temporal view of lyrical sentiment across Taylor Swift's discography.

## Docstring

### Summary
Compute average sentiment per release year from parallel lists of years and sentiment scores.

### Parameters

- **release_years** (List[int]): List of release years for each song, aligned with sentiment_scores.
- **sentiment_scores** (List[float]): Sentiment score for each song, ranging from -1 (very negative) to 1 (very positive).

### Returns

Tuple[List[int], List[float]]: A tuple containing two parallel lists:
- years: Chronological list of years with songs.
- avg_sentiment: Average sentiment for each corresponding year.

### Raises

- ValueError: If release_years and sentiment_scores are of different lengths.
- ValueError: If either input list is empty.

### Examples

```python
>>> years, avg = trend_over_time([2015, 2015, 2016], [0.2, 0.5, -0.1])
([2015, 2016], [0.35, -0.1])
```

```python
>>> trend_over_time([2015, 2016], [0.3])
Traceback (most recent call last):
  ...
ValueError: release_years and sentiment_scores must have the same length.
```
