# run_style_linter PRD

## Description
Runs a style linter on the given file paths and returns a list of style issues identified.


## Conceptual Info

This shim function represents a style linter that checks the given source code files for style issues and returns a list of problems found.

## Docstring

### Summary
Runs a style linter on the provided file paths and returns a list of style issues.

### Parameters

- **file_paths** (str): A string containing file paths to be checked by the linter, separated by commas or a specific delimiter.

### Returns

List[str]: A list of strings where each string represents a style issue identified by the linter.

### Raises

- ValueError: If the input file paths are invalid or if the linter encounters an internal error.
- TypeError: If the input type is not a string.

### Examples

```python
>>> run_style_linter(file_paths='path/to/file1.py,path/to/file2.py')
['style_issue1', 'style_issue2']
```

```python
>>> run_style_linter(file_paths='path/to/file3.py')
['style_issue3']
```
