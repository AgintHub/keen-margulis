# raise_value_error PRD

## Description
Raises a ValueError with a specified message.


## Conceptual Info

The raise_value_error shim function is used to raise a ValueError with a specified message, typically used for input validation and error handling.

## Docstring

### Summary
Raises a ValueError with a specified message.

### Parameters

- **message** (str): The message to be included in the ValueError.

### Raises

- ValueError: Raised with the specified message.

### Examples

```python
>>> raise_value_error(message='Input validation failed')
ValueError: Input validation failed
```

```python
>>> try: raise_value_error(message='Invalid input')
>>> except ValueError as e: print(e)
Invalid input
```
