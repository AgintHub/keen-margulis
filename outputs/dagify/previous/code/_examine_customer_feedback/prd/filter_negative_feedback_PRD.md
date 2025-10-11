# filter_negative_feedback PRD

## Description
Filters negative customer feedback from a list based on sentiment scores.


## Conceptual Info

This shim function filters negative customer feedback from a list based on sentiment scores, playing a crucial role in analyzing customer satisfaction.

## Docstring

### Summary
Filters negative customer feedback based on sentiment scores.

### Parameters

- **feedback_list** (str): A string representation of a list of customer feedback comments.
- **sentiment_scores** (str): A string representation of a list of sentiment scores corresponding to the feedback comments.

### Returns

List[str]: A list of negative customer feedback comments.

### Raises

- ValueError: When the input lists are not of the same length or when the sentiment scores are not valid.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> feedback_list = '["Great product!", "Terrible service.", "Average experience."]'
>>> sentiment_scores = '[0.8, -0.7, 0.1]'
>>> filter_negative_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
["Terrible service."]
```

```python
>>> feedback_list = '["Love the product!", "Hate the service.", "Okay experience."]'
>>> sentiment_scores = '[0.9, -0.8, 0.2]'
>>> filter_negative_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
["Hate the service."]
```
