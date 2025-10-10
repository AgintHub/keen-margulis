# count_social_factors PRD

## Description
Counts the number of unique social factors provided in the input list.


## Conceptual Info

This shim tallies the distinct social factors supplied by earlier nodes, providing a concise integer count that downstream analyses use to quantify social influence.

## Docstring

### Summary
Return the number of unique social factors from a list.

### Parameters

- **factors** (List[str]): A list of social factor names (strings) to be counted.

### Returns

int: The count of distinct social factor names in the input list.

### Raises

- TypeError: Raised if `factors` is not an iterable of strings.
- ValueError: Raised if any element in `factors` is not a string.

### Examples

```python
>>> count_social_factors(['democracy', 'freedom', 'equality'])
3
```

```python
>>> count_social_factors(['democracy', 'freedom', 'democracy'])
2
```
