# validate_political_factors PRD

## Description
This shim validates a list of political factor strings, ensuring they are non-empty, of correct type, and contain no duplicates, returning a string summarizing the outcome.


## Conceptual Info

The validate_political_factors shim ensures that the list of political factors passed to the analysis pipeline is clean, typed correctly, and free of duplicates before further processing.

## Docstring

### Summary
Validate a list of political factor strings, checking for type correctness, non-empty values, and duplicates, and return a formatted validation report.

### Parameters

- **factors** (List[str]): List of political factor strings to validate.

### Returns

str: A message indicating whether validation succeeded or detailing any validation issues.

### Raises

- ValueError: Raised when a factor is empty or duplicates are found.
- TypeError: Raised when the input is not a list of strings.

### Examples

```python
>>> result = validate_political_factors(["Economic recession", "Election", "Policy change"])
"All political factors validated successfully."
```

```python
>>> try:
...     validate_political_factors(["Economic recession", "", "Election"])
>>> except ValueError as e:
...     print(str(e))
"Political factor at index 1 is empty."
```
