# filter_positive_feedback PRD

## Description
Filters customer feedback to identify positive comments based on sentiment scores.


## Conceptual Info

This shim function filters customer feedback to extract positive comments by analyzing the provided sentiment scores, playing a crucial role in understanding customer satisfaction.

## Docstring

### Summary
Filters customer feedback to identify positive comments based on their sentiment scores.

### Parameters

- **feedback_list** (str): A JSON string representing a list of customer feedback comments.
- **sentiment_scores** (str): A JSON string representing a list of sentiment scores corresponding to the feedback comments.

### Returns

List[str]: A list of customer feedback comments that are identified as positive based on their sentiment scores.

### Raises

- ValueError: If the input JSON strings are malformed or if the lengths of feedback_list and sentiment_scores do not match.
- TypeError: If the input types are not as expected (e.g., not JSON strings).

### Examples

```python
>>> import json
>>> feedback_list = json.dumps(['Great product!', 'Terrible service.', 'Excellent quality!'])
>>> sentiment_scores = json.dumps([0.8, 0.2, 0.9])
>>> filter_positive_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
['Great product!', 'Excellent quality!']
```

```python
>>> import json
>>> feedback_list = json.dumps(['Bad experience.', 'Good product.', 'Average service.'])
>>> sentiment_scores = json.dumps([0.1, 0.7, 0.5])
>>> filter_positive_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
['Good product.']
```
