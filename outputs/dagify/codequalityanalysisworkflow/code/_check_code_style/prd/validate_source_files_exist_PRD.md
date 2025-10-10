# validate_source_files_exist PRD

## Description
Validates the existence of given source files.


## Conceptual Info

This shim function is responsible for validating the existence of source code files provided as input. It plays a crucial role in ensuring that subsequent operations are performed on valid files.

## Docstring

### Summary
Validates a list of source file paths and returns those that exist.

### Parameters

- **file_paths** (str): A string containing a list of file paths to validate, separated by commas or other delimiters as needed.

### Returns

List[str]: A list of file paths that were found to exist.

### Raises

- ValueError: If the input string is malformed or empty.
- TypeError: If the input is not a string.

### Examples

```python
>>> file_paths = 'path/to/file1.py,path/to/file2.py'
>>> validate_source_files_exist(file_paths=file_paths)
['path/to/file1.py', 'path/to/file2.py']
```

```python
>>> file_paths = 'path/to/nonexistent_file.py,path/to/file2.py'
>>> validate_source_files_exist(file_paths=file_paths)
['path/to/file2.py']
```
