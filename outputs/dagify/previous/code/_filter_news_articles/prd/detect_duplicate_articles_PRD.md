# detect_duplicate_articles PRD

## Description
Detects indices of duplicate news articles based on their titles and texts.


## Conceptual Info

This shim identifies duplicate news articles by comparing their titles and full texts. It outputs the list of indices that should be removed to eliminate redundancy in downstream processing.

## Docstring

### Summary
Return indices of duplicate articles in a list of titles and texts.

### Parameters

- **titles** (List[str]): A list of article titles.
- **texts** (List[str]): A list of article full texts.

### Returns

List[int]: A list of integer indices (0‑based) that correspond to articles identified as duplicates.

### Raises

- ValueError: If the lengths of `titles` and `texts` do not match.
- TypeError: If `titles` or `texts` is not a list of strings.

### Examples

```python
>>> titles = ["Breaking News", "Daily Update", "Breaking News", "Sports Highlights"],
>>> texts  = ["Content A", "Content B", "Content A", "Content C"],
>>> detect_duplicate_articles(titles, texts)
[2]
```

```python
>>> titles = ["News A", "News B", "News C"],
>>> texts  = ["Text A", "Text B", "Text C"],
>>> detect_duplicate_articles(titles, texts)
[]
```
