# validate_social_factors_input PRD

## Description
Validates and sanitizes a list of social factor strings, ensuring each entry meets formatting and content criteria.


## Conceptual Info

This shim acts as a gatekeeper for social factor inputs, ensuring data integrity before downstream analysis.

## Docstring

### Summary
Validate and clean a list of social factor strings.

### Parameters

- **factors** (List[str]): A list of social factor strings to be validated and cleaned.

### Returns

List[str]: The cleaned list of social factor strings, stripped of leading/trailing whitespace, de-duplicated, and in the original order.

### Raises

- ValueError: Raised if any factor is an empty string or contains disallowed characters.
- TypeError: Raised if `factors` is not a list or any element is not a string.

### Examples

```python
>>> validate_social_factors_input(['poverty', 'unemployment', 'poverty'])
["poverty", "unemployment"]
```

```python
>>> validate_social_factors_input(['poverty', ' ', 'infrastructure'])
ValueError: Invalid social factor: empty string or disallowed characters
```
