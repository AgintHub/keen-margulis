# generate_sentiment_summary PRD

## Description
Generates a concise textual summary of overall sentiment distribution based on sentiment counts.


## Conceptual Info

The generate_sentiment_summary shim produces a human-readable summary of sentiment distribution across a set of news articles, converting numerical counts into a short narrative.

## Docstring

### Summary
Create a brief summary of overall sentiment distribution based on provided counts of positive, negative, and neutral sentiments.

### Parameters

- **sentiment_counts** (Dict[str, int]): Dictionary mapping sentiment categories ('positive', 'negative', 'neutral') to their respective article counts.

### Returns

str: A short English sentence summarizing the sentiment distribution.

### Raises

- ValueError: If sentiment_counts is missing one or more of the required keys.
- TypeError: If sentiment_counts is not a dictionary or contains non-integer counts.

### Examples

```python
>>> sentiment_counts = {'positive': 12, 'negative': 5, 'neutral': 3}
>>> summary = generate_sentiment_summary(sentiment_counts=sentiment_counts)
>>> print(summary)
'In total, 12 articles were positive, 5 negative, and 3 neutral.'
```

```python
>>> sentiment_counts = {'positive': 7, 'negative': 7, 'neutral': 6}
>>> print(generate_sentiment_summary(sentiment_counts=sentiment_counts))
'The sentiment distribution is even: 7 positive, 7 negative, and 6 neutral articles.'
```
