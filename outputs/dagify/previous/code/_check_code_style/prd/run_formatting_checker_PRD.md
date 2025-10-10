# run_formatting_checker PRD

## Description
Checks code formatting for the given file paths and returns a list of formatting errors


## Conceptual Info

This shim node is responsible for checking the code formatting of given source code files and returning any formatting errors found.

## Docstring

### Summary
Checks code formatting for the given file paths and returns a list of formatting errors

### Parameters

- **file_paths** (str): A string containing the paths to the files to be checked, separated by commas or a single path

### Returns

List[str]: A list of strings where each string represents a formatting error detected in the code files

### Raises

- ValueError: If the input file paths are invalid or if no files are found at the given paths
- TypeError: If the input type is not a string

### Examples

```python
>>> run_formatting_checker(file_paths='path/to/file1.py,path/to/file2.py')
['file1.py:1:1: error: missing whitespace around operator']
```

```python
>>> run_formatting_checker(file_paths='path/to/single_file.py')
['single_file.py:5:5: error: inconsistent indentation']
```
