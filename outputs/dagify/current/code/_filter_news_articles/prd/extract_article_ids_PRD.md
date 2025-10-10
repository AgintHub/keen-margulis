# extract_article_ids PRD

## Description
Selects article titles from a list based on provided indices and returns them.


## Conceptual Info

This shim extracts the subset of article titles corresponding to given indices, facilitating downstream filtering and reporting steps in a news aggregation workflow.

## Docstring

### Summary
Return the titles of articles at the supplied indices.

### Parameters

- **titles** (List[str]): A list of article titles in the original order.
- **indices** (List[int]): A list of integer indices specifying which titles to extract.

### Returns

List[str]: A list of titles at the requested indices, preserving the order of indices.

### Raises

- ValueError: Raised when an index is out of bounds for the titles list.
- TypeError: Raised when titles is not a list of strings or indices is not a list of integers.

### Examples

```python
>>> titles = ['Alpha', 'Beta', 'Gamma', 'Delta']
>>> indices = [0, 2, 3]
>>> result = extract_article_ids(titles, indices)
>>> print(result)
['Alpha', 'Gamma', 'Delta']
```

```python
>>> titles = ['One', 'Two', 'Three']
>>> indices = []
>>> result = extract_article_ids(titles, indices)
>>> print(result)
[]
```
