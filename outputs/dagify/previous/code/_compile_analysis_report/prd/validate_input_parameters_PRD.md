# validate_input_parameters PRD

## Description
Validate the input parameters for sentiment analysis and trend identification, ensuring required fields are present and correctly typed.


## Conceptual Info

This shim function acts as a gatekeeper in the analysis pipeline, ensuring that the sentiment and trend data objects received from upstream nodes adhere to expected schemas before further processing.

## Docstring

### Summary
Validate that sentiment and trend input data contain required fields with correct types and return a success message.

### Parameters

- **sentiment_data** (str): JSON string representation of an AnalyzeSentimentOutput object, containing article indices, sentiment categories, and confidence scores.
- **trends_data** (str): JSON string representation of an IdentifyTrendsOutput object, containing trending topics, sentiment trends, and an overall trend summary.

### Returns

str: A confirmation string, e.g., 'Validation successful', indicating that the input data passed all checks.

### Raises

- ValueError: Raised when required fields are missing or contain invalid data.
- TypeError: Raised when the input parameters are not strings or cannot be parsed into valid JSON objects.

### Examples

```python
>>> output = validate_input_parameters(
...     sentiment_data='{"article_index": [1, 2], "sentiment_category": ["positive", "negative"], "sentiment_confidence": [0.95, 0.85]}',
...     trends_data='{"trending_topics": ["economy"], "sentiment_trends": ["stable neutral"], "overall_trend_summary": "stable"}'
>>> )
'Validation successful'
```

```python
>>> try:
...     validate_input_parameters(
...         sentiment_data='{"article_index": [1], "sentiment_category": ["positive"]}',
...         trends_data='{"trending_topics": ["economy"], "sentiment_trends": ["stable neutral"]}'
...     )
>>> except Exception as e:
...     print(e)
'ValueError: Missing field 'overall_trend_summary' in trends_data'
```
