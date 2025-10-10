# validate_report_completion PRD

## Description
Checks that the generated report contains content and matches the expected article count.


## Conceptual Info

The validation shim ensures that a textual report produced by the pipeline is non-empty, has sufficient length, and reflects the correct number of articles, providing a quick sanity check before downstream usage.

## Docstring

### Summary
Validate that a report string is non-empty and contains at least the specified number of article summaries.

### Parameters

- **report_text** (str): Full textual report to be validated.
- **article_count** (int): Expected number of articles included in the report.

### Returns

bool: True if the report meets all validation criteria; otherwise False.

### Raises

- ValueError: Raised when article_count is negative or zero.
- TypeError: Raised when report_text is not a string or article_count is not an integer.

### Examples

```python
>>> valid = validate_report_completion('Summary 1\nSummary 2', 2)
True
```

```python
>>> validate_report_completion('', 1)
False
```
