# calculate_sentiment_trends PRD

## Description
Produces a sentiment trend label for each topic by analysing a list of sentiment strings per topic.


## Conceptual Info

The shim determines how sentiment towards each recurring topic evolves across time, producing concise trend labels such as "increasing positive" or "stable negative".

## Docstring

### Summary
Calculate sentiment trend labels for a set of topics based on per‑topic sentiment lists.

### Parameters

- **topic_sentiments** (List[List[str]]): A list where each element is a list of sentiment strings ('positive', 'negative', 'neutral') collected for a specific topic.

### Returns

List[str]: A list of sentiment trend descriptors, one per topic, e.g. 'increasing positive', 'decreasing negative', or 'stable neutral'.

### Raises

- ValueError: Raised when the input is empty or a sub‑list is empty.
- TypeError: Raised when the input is not a list of lists of strings.

### Examples

```python
>>> sentiment_lists = [
...     ['positive', 'positive', 'neutral'],
...     ['negative', 'negative', 'negative'],
...     ['neutral', 'neutral', 'neutral']
>>> ]
>>> result = calculate_sentiment_trends(topic_sentiments=sentiment_lists)
>>> print(result)
['increasing positive', 'decreasing negative', 'stable neutral']
```

```python
>>> sentiment_lists = [
...     ['positive'],
...     ['negative', 'positive', 'negative', 'positive']
>>> ]
>>> result = calculate_sentiment_trends(topic_sentiments=sentiment_lists)
>>> print(result)
['stable positive', 'fluctuating negative']
```
