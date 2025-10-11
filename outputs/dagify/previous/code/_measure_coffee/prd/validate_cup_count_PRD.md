# validate_cup_count PRD

## Description
Validates that the desired cup count is a positive integer and returns a confirmation message.


## Conceptual Info

This shim ensures the cup count provided for brewing coffee is valid, preventing downstream errors in the measurement process.

## Docstring

### Summary
Checks that the desired cup count is a positive integer and returns a confirmation string.

### Parameters

- **desired_cup_count** (int): Number of coffee cups intended to brew. Must be a positive integer.

### Returns

str: A confirmation message indicating the cup count is valid.

### Raises

- ValueError: If desired_cup_count is less than or equal to zero.
- TypeError: If desired_cup_count is not an integer.

### Examples

```python
>>> validate_cup_count(5)
'Cup count 5 validated successfully.'
```

```python
>>> validate_cup_count(-3)
ValueError: Cup count must be a positive integer.
```
