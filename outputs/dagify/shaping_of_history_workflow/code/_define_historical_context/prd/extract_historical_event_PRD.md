# extract_historical_event PRD

## Description
Extracts the name or title of a historical event from a given parsed input string.


## Conceptual Info

This shim is responsible for identifying and returning the most salient historical event name or title from a user-provided text, serving as a building block for higher-level context definition.

## Docstring

### Summary
Extracts the historical event name from a parsed input string.

### Parameters

- **parsed_input** (str): A string containing a user’s query or description that may reference a historical event.

### Returns

str: The extracted event name or title as a plain string.

### Raises

- ValueError: Raised when no discernible historical event can be identified in the input.
- TypeError: Raised when parsed_input is not of type str.

### Examples

```python
>>> extract_historical_event('The Battle of Hastings was a pivotal moment in English history.')
'Battle of Hastings'
```

```python
>>> extract_historical_event('The French Revolution began in 1789 and reshaped Europe.')
'French Revolution'
```
