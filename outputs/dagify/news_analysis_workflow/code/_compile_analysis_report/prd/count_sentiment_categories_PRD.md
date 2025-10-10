# count_sentiment_categories PRD

## Description
Returns a JSON string mapping each sentiment category ('positive', 'negative', 'neutral') to its count from a comma‑separated input string.


## Conceptual Info

This shim aggregates sentiment counts from a list of categories supplied as a string, enabling downstream report generation modules to summarize overall sentiment distribution.

## Docstring

### Summary
Counts occurrences of the sentiment categories 'positive', 'negative', and 'neutral' from a comma‑separated string and returns a JSON string of the resulting counts.

### Parameters

- **sentiment_categories** (str): Comma‑separated string of sentiment categories to count. Example: "positive,negative,positive".

### Returns

str: JSON string mapping each of the categories 'positive', 'negative', and 'neutral' to an integer count.

### Raises

- ValueError: Raised when the input string contains an invalid sentiment category or is empty.
- TypeError: Raised when the input is not a string.

### Examples

```python
>>> output = count_sentiment_categories('positive,negative,positive')
'{'positive': 2, 'negative': 1, 'neutral': 0}'
```

```python
>>> output = count_sentiment_categories('neutral,neutral,positive')
'{'positive': 1, 'negative': 0, 'neutral': 2}'
```
