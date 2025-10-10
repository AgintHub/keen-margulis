# extract_topics_from_summaries PRD

## Description
Extracts a list of key topics from each preprocessed news article summary.


## Conceptual Info

This shim bridges raw article summaries to downstream trend analysis by extracting salient topics from each summary.

## Docstring

### Summary
Extract topics from each preprocessed news article summary.

### Parameters

- **summaries** (List[str]): A list of preprocessed summaries, one per news article.

### Returns

List[List[str]]: A list where each element is a list of topics extracted from the corresponding summary.

### Raises

- TypeError: Raised if `summaries` is not a list or contains non-string elements.
- ValueError: Raised if any summary in the list is an empty string or if topic extraction fails for a summary.

### Examples

```python
>>> summaries = ["The economy is growing fast", "New technology advances are exciting"]
>>> topics = extract_topics_from_summaries(summaries)
>>> print(topics)
[['economy', 'growth'], ['technology', 'advancement']]
```

```python
>>> summaries = ["Climate change impacts rising sea levels", "Sports events attract millions of viewers"]
>>> topics = extract_topics_from_summaries(summaries)
>>> print(topics)
[['climate change', 'sea level', 'impact'], ['sports', 'viewers']]
```
