# parse_user_input PRD

## Description
Parses a raw user input string into a structured dictionary representation of the user's intent for workflow generation.


## Conceptual Info

This shim function serves as the initial natural language processing step, converting free-text user input into a structured dictionary that downstream workflow components can consume.

## Docstring

### Summary
Parse a user-provided text string into a JSON-formatted dictionary of intent and parameters.

### Parameters

- **input_text** (str): The raw input text from the user to be parsed.

### Returns

str: A JSON string that maps keys such as 'intent', 'parameters', etc., representing the parsed user intent.

### Raises

- ValueError: Raised when the input text cannot be parsed into a valid intent dictionary.
- TypeError: Raised when input_text is not of type str.

### Examples

```python
>>> parse_user_input('Book me a flight to Paris next Monday')
'{"intent": "book_flight", "destination": "Paris", "date": "next Monday"}'
```

```python
>>> parse_user_input('Show me the weather in New York')
'{"intent": "get_weather", "location": "New York"}'
```
