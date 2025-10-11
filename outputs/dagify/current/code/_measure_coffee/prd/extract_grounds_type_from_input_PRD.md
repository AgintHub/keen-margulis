# extract_grounds_type_from_input PRD

## Description
Extracts the coffee grounds type from the input string and optional kwargs.


## Conceptual Info

This shim isolates the logic needed to determine the coffee grounds type from user‑provided text or keyword arguments, enabling the coffee measurement workflow to use a consistent and validated grounds type value.

## Docstring

### Summary
Extracts the coffee grounds type from a general input string and optional keyword arguments.

### Parameters

- **general_input** (str): Free‑form text containing information about the desired coffee grounds and cup count.
- **kwargs** (str): Optional JSON or key/value string that may directly specify the grounds_type.

### Returns

str: A lowercase string identifying the coffee grounds type (e.g., "medium grind" or "dark roast").

### Raises

- ValueError: Raised when no recognizable grounds type can be extracted from either `kwargs` or `general_input`.
- TypeError: Raised if either `general_input` or `kwargs` is not of type `str`.

### Examples

```python
>>> extract_grounds_type_from_input("I need 2 cups with medium grind", "")
"medium grind"
```

```python
>>> extract_grounds_type_from_input("Use dark roast for 3 cups", "grounds_type=dark roast")
"dark roast"
```
