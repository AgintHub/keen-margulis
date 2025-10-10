# analyze_sentiment_per_topic PRD

## Description
Analyzes sentiment for each topic across news article summaries and returns a list of sentiment labels per topic per summary.


## Conceptual Info

This shim performs sentiment analysis on a set of news article summaries for a list of trending topics. It outputs, for each topic, a list of sentiment labels corresponding to each summary, enabling downstream trend calculation.

## Docstring

### Summary
Analyzes sentiment for each trending topic across the provided news article summaries, returning sentiment labels per topic per summary.

### Parameters

- **summaries** (List[str]): List of preprocessed news article summaries.
- **topics** (List[str]): List of trending topics to analyze sentiment for.

### Returns

List[List[str]]: A list where each element corresponds to a topic and contains a list of sentiment labels (e.g., 'positive', 'neutral', 'negative') for each summary.

### Raises

- ValueError: If either `summaries` or `topics` is empty, or if the number of summaries does not match the expected input format.
- TypeError: If `summaries` or `topics` is not a list of strings.

### Examples

```python
>>> result = analyze_sentiment_per_topic(["The policy is great.", "The policy is bad."], ["policy"])
[["positive", "negative"]]
```

```python
>>> result = analyze_sentiment_per_topic(["Good results were achieved.", "Results were disappointing.", "Results were neutral."], ["results"])
[["positive", "negative", "neutral"]]
```
