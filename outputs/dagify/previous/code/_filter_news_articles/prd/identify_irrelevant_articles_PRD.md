# identify_irrelevant_articles PRD

## Description
Identifies indices of news articles considered irrelevant based on content analysis.


## Conceptual Info

The shim abstracts the logic to determine which news articles lack sufficient relevance, enabling downstream filtering steps to remove them.

## Docstring

### Summary
Returns the zero-based indices of news articles deemed irrelevant.

### Parameters

- **titles** (List[str]): List of article titles.
- **texts** (List[str]): List of full article texts.

### Returns

List[int]: Zero-based indices of articles identified as irrelevant.

### Raises

- ValueError: If the number of titles and texts differ or if any list is empty.
- TypeError: If titles or texts are not lists of strings.

### Examples

```python
>>> titles = ['Short News', 'Detailed Report']
>>> texts = ['Hi', 'This is a comprehensive analysis of the recent event.']
>>> indices = identify_irrelevant_articles(titles, texts)
>>> print(indices)
[0]
```

```python
>>> titles = ['Empty', 'Irrelevant']
>>> texts = ['', '!!!']
>>> indices = identify_irrelevant_articles(titles, texts)
>>> print(indices)
[0, 1]
```
