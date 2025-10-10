# get_remaining_indices PRD

## Description
Computes the list of remaining article indices after removing specified indices from a total set.


## Conceptual Info

This shim determines which articles remain after filtering out those identified as duplicates or irrelevant.

## Docstring

### Summary
Return the list of remaining indices given the total count and a list of removed indices.

### Parameters

- **total_count** (int): The total number of articles originally retrieved.
- **removed_indices** (List[int]): Indices of articles that have been removed (e.g., duplicates or irrelevant).

### Returns

List[int]: A sorted list of indices that were not removed.

### Raises

- TypeError: If total_count is not an int or removed_indices is not a list of ints.
- ValueError: If any removed index is outside the range [0, total_count-1] or if total_count is negative.

### Examples

```python
>>> get_remaining_indices(total_count=5, removed_indices=[0, 2])
[1, 3, 4]
```

```python
>>> get_remaining_indices(total_count=3, removed_indices=[0, 1, 2])
[]
```
