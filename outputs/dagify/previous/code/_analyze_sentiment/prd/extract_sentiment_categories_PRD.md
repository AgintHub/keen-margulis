# extract_sentiment_categories PRD

## Description
Extracts a list of sentiment categories from sentiment analysis results.


## Conceptual Info

This shim retrieves the sentiment category labels (e.g., 'positive', 'negative', 'neutral') from a batch of sentiment analysis result dictionaries, enabling downstream components to aggregate and report sentiment distributions across articles.

## Docstring

### Summary
Return a list of sentiment categories from the given analysis results.

### Parameters

- **results** (List[dict]): A list of dictionaries returned by a sentiment analysis batch process. Each dictionary must contain a 'sentiment_category' key with a string value.

### Returns

List[str]: A list of sentiment category strings in the same order as the input results.

### Raises

- TypeError: If the input is not a list or contains non-dictionary elements.
- ValueError: If any dictionary in the list lacks the 'sentiment_category' key.

### Examples

```python
>>> results = [
...     {'sentiment_category': 'positive', 'sentiment_confidence': 0.95},
...     {'sentiment_category': 'neutral', 'sentiment_confidence': 0.60},
...     {'sentiment_category': 'negative', 'sentiment_confidence': 0.20}
>>> ]
>>> extract_sentiment_categories(results=results)
['positive', 'neutral', 'negative']
```

```python
>>> results = [
...     {'sentiment_confidence': 0.95},
...     {'sentiment_category': 'neutral'}
>>> ]
>>> extract_sentiment_categories(results=results)
ValueError: Each result dictionary must contain a 'sentiment_category' key.
```
