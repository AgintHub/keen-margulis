# validate_feedback_input PRD

## Description
Validates the input feedback data to ensure it is properly formatted and contains valid information.


## Conceptual Info

This node serves as a validation checkpoint for customer feedback data, ensuring that it meets certain criteria before being processed further in the system.

## Docstring

### Summary
Validates the input feedback data to ensure it is not empty and contains valid information.

### Parameters

- **feedback_data** (str): The input feedback data to be validated.

### Returns

str: A message indicating whether the feedback data is valid or not.

### Raises

- ValueError: When the input feedback data is empty or contains invalid information.
- TypeError: When the input type is not a string or a list of strings.

### Examples

```python
>>> validate_feedback_input(feedback_data='Good service')
'Feedback data is valid'
```

```python
>>> validate_feedback_input(feedback_data='')
ValueError: Feedback data is empty
```
