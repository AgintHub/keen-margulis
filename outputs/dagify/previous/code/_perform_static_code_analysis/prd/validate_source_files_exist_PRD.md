# validate_source_files_exist PRD

## Description
Validates the existence of source files provided as input file paths.


## Conceptual Info

This shim function validates whether the source code files provided exist in the system.

## Docstring

### Summary
Validates the existence of source files provided as input file paths.

### Parameters

- **file_paths** (str): A comma-separated string of file paths to validate.

### Returns

str: A success message if all files exist, otherwise an error message.

### Raises

- FileNotFoundError: If any of the provided file paths do not exist.
- TypeError: If the input is not a string or if the string is not properly formatted.

### Examples

```python
>>> validate_source_files_exist(file_paths='path/to/file1.py,path/to/file2.py')
'All files exist.'
```

```python
>>> validate_source_files_exist(file_paths='path/to/nonexistent_file.py')
'File not found: path/to/nonexistent_file.py'
```
