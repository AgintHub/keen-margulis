# count_words PRD

## Description
Counts the number of words in a given text string.


## Conceptual Info

The count_words shim encapsulates a simple word counting operation that can be reused by other nodes in the data pipeline, ensuring consistent and testable behavior for text metrics.

## Docstring

### Summary
Return the total number of words contained in the input string.

### Parameters

- **text** (str): The text to be analyzed. Must be a non-empty string.

### Returns

int: An integer representing the number of words in `text`. Words are sequences of characters separated by whitespace.

### Raises

- TypeError: Raised if `text` is not of type `str`.
- ValueError: Raised if `text` is an empty string or contains only whitespace.

### Examples

```python
>>> count_words('Hello world')
2
```

```python
>>> count_words('This is a test.')
4
```
