# extract_common_complaints PRD

## Description
Extracts common complaints from a list of negative customer feedback.


## Conceptual Info

This node is responsible for analyzing negative customer feedback to identify recurring complaints, which are then used to inform customer satisfaction metrics.

## Docstring

### Summary
Extracts common complaints from negative customer feedback.

### Parameters

- **negative_feedback** (List[str]): List of negative customer feedback comments.

### Returns

List[str]: List of common complaints extracted from the negative feedback.

### Raises

- ValueError: If the input negative feedback is not a list of strings.
- TypeError: If the input type is not a list.

### Examples

```python
>>> negative_feedback = ['The product is too expensive.', 'The service was slow.', 'The product is too expensive.']
>>> complaints = extract_common_complaints(negative_feedback)
['The product is too expensive.']
```

```python
>>> negative_feedback = ['Poor customer support.', 'Product did not meet expectations.', 'Poor customer support.']
>>> complaints = extract_common_complaints(negative_feedback)
['Poor customer support.']
```
