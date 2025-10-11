# get_current_timestamp PRD

## Description
Returns the current UTC timestamp as an ISO 8601 string.


## Conceptual Info

Provides a consistent, timezone‑aware timestamp for use in workflow steps that require a point in time.

## Docstring

### Summary
Return the current UTC time formatted as an ISO 8601 string.

### Returns

str: ISO 8601 formatted string representing the current UTC timestamp.

### Raises

- TypeError: If arguments are passed to the function.

### Examples

```python
>>> timestamp = get_current_timestamp()
>>> print(timestamp)
"2025-10-11T12:34:56+00:00"
```

```python
>>> print(get_current_timestamp())
"2025-10-11T12:34:56+00:00"
```
