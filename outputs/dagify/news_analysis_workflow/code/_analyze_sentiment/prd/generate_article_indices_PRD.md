# generate_article_indices PRD

## Description
Generates a sequential list of article indices based on the number of summaries provided.


## Conceptual Info

This shim creates a simple mapping from article count to a list of integer indices, which is used by downstream sentiment analysis to align results with the original article order.

## Docstring

### Summary
Return a list of integers from 0 to summaries_count-1 representing article indices.

### Parameters

- **summaries_count** (int): The total number of article summaries that require indexing.

### Returns

List[int]: A list of sequential integer indices corresponding to each article.

### Raises

- ValueError: Raised when summaries_count is negative.
- TypeError: Raised when summaries_count is not of type int.

### Examples

```python
>>> generate_article_indices(summaries_count=3)
[0, 1, 2]
```

```python
>>> generate_article_indices(summaries_count=0)
[]
```
