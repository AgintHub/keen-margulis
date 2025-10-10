# identify_recurring_topics PRD

## Description
Returns a list of topics that appear in multiple input topic lists.


## Conceptual Info

The identify_recurring_topics shim aggregates topics extracted from news summaries and determines which topics are common across multiple articles, enabling trend analysis.

## Docstring

### Summary
Finds topics that appear in more than one of the provided topic lists.

### Parameters

- **topic_lists** (List[List[str]]): A list where each element is a list of topic strings extracted from a single news summary.

### Returns

List[str]: A list of unique topics that occur in at least two of the input lists.

### Raises

- TypeError: If topic_lists is not a list of lists of strings.
- ValueError: If topic_lists is empty or contains empty sublists.

### Examples

```python
>>> topic_lists = [['economy', 'policy'], ['economy', 'inflation'], ['policy', 'economy']]
>>> print(identify_recurring_topics(topic_lists=topic_lists))
['economy', 'policy']
```

```python
>>> topic_lists = [['technology'], ['health'], ['finance']]
>>> print(identify_recurring_topics(topic_lists=topic_lists))
[]
```
