# extract_positive_themes PRD

## Description
Extracts themes from positive customer feedback.


## Conceptual Info

This shim function is designed to extract and return themes from positive customer feedback, aiding in understanding customer satisfaction.

## Docstring

### Summary
Extracts themes from the given positive customer feedback.

### Parameters

- **positive_feedback** (str): Positive customer feedback from which themes are to be extracted.

### Returns

List[str]: A list of themes identified from the positive customer feedback.

### Raises

- ValueError: If the input positive feedback is empty or not a string.
- TypeError: If the input is not of type string.

### Examples

```python
>>> positive_feedback = 'The customer service was excellent.'
>>> themes = extract_positive_themes(positive_feedback)
>>> print(themes)
['customer service']
```

```python
>>> positive_feedback = 'The product quality was great.'
>>> themes = extract_positive_themes(positive_feedback)
>>> print(themes)
['product quality']
```
