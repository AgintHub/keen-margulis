# get_unique_categories PRD

## Description
Returns a list of unique category labels from the input list, preserving the order of first occurrence.


## Conceptual Info

This shim extracts the distinct category labels from a list while maintaining the order in which they first appear, enabling downstream processing to work with a minimal set of categories.

## Docstring

### Summary
Return a list of unique categories from the provided list, preserving the original order of first appearance.

### Parameters

- **categories** (List[str]): A list of category labels, each a string. The function expects a non-empty list containing only strings.

### Returns

List[str]: A list containing each distinct category from `categories` exactly once, ordered by the first time it appeared in the input list.

### Raises

- TypeError: Raised if `categories` is not a list or if any element is not a string.
- ValueError: Raised if `categories` is an empty list.

### Examples

```python
>>> unique = get_unique_categories(['sports', 'politics', 'sports', 'tech'])
['sports', 'politics', 'tech']
```

```python
>>> unique = get_unique_categories([])
ValueError: Input list cannot be empty.
```
