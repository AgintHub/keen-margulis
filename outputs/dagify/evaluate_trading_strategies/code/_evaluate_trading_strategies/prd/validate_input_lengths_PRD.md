# validate_input_lengths PRD

## Description
Validates that the length of the predictions list matches the length of the confidence list in the trading strategy evaluation process.


## Conceptual Info

Ensures that the prediction and confidence inputs supplied to downstream evaluation functions have identical lengths, preventing misalignment errors during strategy assessment.

## Docstring

### Summary
Check that `predictions` and `confidence` lists are of equal length. Returns a confirmation string on success; otherwise raises an exception.

### Parameters

- **predictions** (List[str]): A list of string predictions for market trends.
- **confidence** (List[float]): A list of confidence scores corresponding to each prediction.

### Returns

str: A success message such as "Lengths are valid" when the two lists have the same length.

### Raises

- ValueError: Raised when the lengths of `predictions` and `confidence` differ.
- TypeError: Raised if either argument is not a list or contains incompatible element types.

### Examples

```python
>>> validate_input_lengths(['bull', 'bear'], [0.8, 0.6])
'Lengths are valid'
```

```python
>>> validate_input_lengths(['bull', 'bear', 'neutral'], [0.8, 0.6])
Traceback (most recent call last):\n  ...\nValueError: Length mismatch: predictions has 3 elements while confidence has 2.
```
