# filter_and_format_issues PRD

## Description
Filters and formats issues identified by static code analysis tools.


## Conceptual Info

This shim node is responsible for taking raw issues from static code analysis, filtering them based on certain criteria, and then formatting them into a standardized output.

## Docstring

### Summary
Filters and formats raw issues from static code analysis into a list of strings.

### Parameters

- **raw_issues** (str): A string containing raw issues identified by static code analysis, potentially in a serialized or raw text format.

### Returns

List[str]: A list of strings where each string represents a filtered and formatted issue.

### Raises

- ValueError: If the raw_issues string is malformed or cannot be processed.
- TypeError: If the input type is not a string.

### Examples

```python
>>> raw_issues = 'issue1:severity1,issue2:severity2'
>>> filtered_issues = filter_and_format_issues(raw_issues=raw_issues)
>>> print(filtered_issues)
['issue1:SEVERITY1', 'issue2:SEVERITY2']
```

```python
>>> raw_issues = 'error:file1.py:line1,message'
>>> filtered_issues = filter_and_format_issues(raw_issues=raw_issues)
>>> print(filtered_issues)
['FILE1.PY:LINE1:ERROR:MESSAGE']
```
