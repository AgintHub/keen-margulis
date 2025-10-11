# analyze_sentiment_scores PRD

## Description
Analyzes the sentiment scores of a given list of customer feedback comments.


## Conceptual Info

This node analyzes customer feedback comments to determine their sentiment scores, which are then used to assess overall customer satisfaction.

## Docstring

### Summary
Analyzes the sentiment of customer feedback comments and returns a list of sentiment scores.

### Parameters

- **feedback_list** (List[str]): A list of customer feedback comments to be analyzed.

### Returns

List[float]: A list of sentiment scores between 0 and 1, where 0 represents very negative sentiment and 1 represents very positive sentiment.

### Raises

- ValueError: If the input feedback_list is empty or contains non-string values.
- TypeError: If the input feedback_list is not a list.

### Examples

```python
>>> feedback_list = ['I loved the service!', 'The product was okay.', 'Terrible experience.']
>>> sentiment_scores = analyze_sentiment_scores(feedback_list=feedback_list)
[0.9, 0.5, 0.1]
```

```python
>>> feedback_list = ['Great product!', 'Average service.', 'Poor quality.']
>>> sentiment_scores = analyze_sentiment_scores(feedback_list=feedback_list)
[0.8, 0.4, 0.2]
```
