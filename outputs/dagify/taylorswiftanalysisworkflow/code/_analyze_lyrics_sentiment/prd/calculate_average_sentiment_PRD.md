# calculate_average_sentiment PRD

## Description
Computes the average sentiment score from a list of sentiment scores.


## Conceptual Info

Calculates the mean sentiment value from individual song sentiment scores.

## Docstring

### Summary
Calculates the average sentiment score from a list of sentiment values.

### Parameters

- **scores** (List[float]): A list of sentiment scores for each song.

### Returns

float: The average sentiment score across all songs.

### Raises

- ValueError: If the scores list is empty.

### Examples

```python
>>> sentiment_scores = [0.5, 0.7, 0.9]
>>> average = calculate_average_sentiment(sentiment_scores)
>>> print(average)
0.7
```
