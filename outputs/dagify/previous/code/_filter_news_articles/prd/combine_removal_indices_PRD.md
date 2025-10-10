# combine_removal_indices PRD

## Description
Combines two lists of article indices—duplicates and irrelevant—into a single sorted list of unique indices for removal.


## Conceptual Info

In the filtering pipeline, articles identified as duplicate or irrelevant must be removed. This shim merges their indices into a single, de‑duplicated, sorted list to be used by downstream components.

## Docstring

### Summary
Combines duplicate and irrelevant article index lists into a sorted list of unique indices.

### Parameters

- **duplicates** (List[int]): List of integer indices representing articles identified as duplicates.
- **irrelevant** (List[int]): List of integer indices representing articles identified as irrelevant.

### Returns

List[int]: A sorted list containing every index from both input lists, with duplicates removed.

### Raises

- ValueError: Raised if any element in either input list is not a non‑negative integer.
- TypeError: Raised if either input is not a list.

### Examples

```python
>>> duplicates = [1, 3, 5]
>>> irrelevant = [3, 4, 6]
>>> combine_removal_indices(duplicates, irrelevant)
[1, 3, 4, 5, 6]
```

```python
>>> duplicates = []
>>> irrelevant = [2, 7]
>>> combine_removal_indices(duplicates, irrelevant)
[2, 7]
```
