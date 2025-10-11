# parse_feedback_data PRD

## Description
Parses customer feedback data into a list of individual feedback comments.


## Conceptual Info

This shim node is responsible for taking raw customer feedback data as input and parsing it into a list of individual feedback comments, which can then be further analyzed.

## Docstring

### Summary
Parses raw customer feedback data into a list of individual feedback comments.

### Parameters

- **feedback_data** (str): The raw customer feedback data that needs to be parsed.

### Returns

List[str]: A list of individual customer feedback comments.

### Raises

- ValueError: If the input feedback data is not in the expected format.
- TypeError: If the input is not a string.

### Examples

```python
>>> parse_feedback_data(feedback_data='Great service!\nExcellent product.')
['Great service!', 'Excellent product.']
```

```python
>>> parse_feedback_data(feedback_data='Poor service.\nBad product.')
['Poor service.', 'Bad product.']
```
