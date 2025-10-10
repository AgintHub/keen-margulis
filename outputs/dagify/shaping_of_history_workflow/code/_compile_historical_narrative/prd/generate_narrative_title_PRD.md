# generate_narrative_title PRD

## Description
Generates a concise title for a historical narrative based on the given event and time frame.


## Conceptual Info

This shim creates a compelling, concise title for a historical narrative, ensuring the title reflects both the event and its temporal context. The title is later used as the headline of the compiled narrative.

## Docstring

### Summary
Generate a concise title for a historical narrative based on the provided event and time frame.

### Parameters

- **event** (str): The name or description of the historical event to be narrated.
- **time_frame** (str): The temporal scope of the event (e.g., '1939-1945', '18th century').

### Returns

str: A string title that is no longer than 10 words, incorporates the event and time frame, and is suitable for use as a headline in a historical narrative.

### Raises

- ValueError: Raised if either `event` or `time_frame` is an empty string.
- TypeError: Raised if either `event` or `time_frame` is not of type `str`.

### Examples

```python
>>> title = generate_narrative_title(event='The French Revolution', time_frame='1789-1799')
"French Revolution (1789-1799): A Turning Point"
```

```python
>>> title = generate_narrative_title(event='World War II', time_frame='1939-1945')
"World War II (1939-1945): The Global Conflict"
```
