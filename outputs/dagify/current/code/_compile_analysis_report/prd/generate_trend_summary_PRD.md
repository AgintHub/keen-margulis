# generate_trend_summary PRD

## Description
Generates a concise textual summary of trend patterns based on input topics and their sentiment trends.


## Conceptual Info

This shim is responsible for turning raw trend data—topics and their associated sentiment evolution—into an easily readable sentence that captures the overall trend narrative, facilitating downstream reporting.

## Docstring

### Summary
Generate a concise trend summary from lists of trending topics and their sentiment trends.

### Parameters

- **trending_topics** (List[str]): A list of topics that show a trend across the news articles.
- **sentiment_trends** (List[str]): A list describing the sentiment trend for each corresponding trending topic, e.g., 'increasing positive', 'decreasing negative', or 'stable neutral'.

### Returns

str: A single sentence that succinctly summarizes how each topic's sentiment is evolving.

### Raises

- ValueError: Raised when the two input lists have different lengths or are empty.
- TypeError: Raised when inputs are not lists of strings.

### Examples

```python
>>> summary = generate_trend_summary(['Economy', 'Tech'], ['increasing positive', 'stable neutral'])
'The Economy trend shows increasing positive sentiment, while Tech trend remains stable and neutral.'
```

```python
>>> summary = generate_trend_summary(['Healthcare'], ['decreasing negative'])
'The Healthcare trend shows decreasing negative sentiment.'
```
