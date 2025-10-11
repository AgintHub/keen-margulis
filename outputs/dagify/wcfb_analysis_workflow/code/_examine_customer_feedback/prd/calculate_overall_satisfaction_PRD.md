# calculate_overall_satisfaction PRD

## Description
Calculates the overall customer satisfaction score based on sentiment scores.


## Conceptual Info

This shim node is responsible for computing an overall satisfaction score from a list of sentiment scores derived from customer feedback.

## Docstring

### Summary
Calculates the overall customer satisfaction score based on the provided sentiment scores.

### Parameters

- **sentiment_scores** (List[float]): A list of sentiment scores derived from customer feedback.

### Returns

float: The overall customer satisfaction score calculated from the sentiment scores.

### Raises

- ValueError: If the input sentiment scores are empty or invalid.
- TypeError: If the input sentiment scores are not a list of floats.

### Examples

```python
>>> sentiment_scores = [0.8, 0.9, 0.7]
>>> overall_satisfaction = calculate_overall_satisfaction(sentiment_scores=sentiment_scores)
0.8
```

```python
>>> sentiment_scores = [0.5, 0.6, 0.4]
>>> overall_satisfaction = calculate_overall_satisfaction(sentiment_scores=sentiment_scores)
0.5
```
