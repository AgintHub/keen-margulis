# validate_input_files PRD

## Description
Validates the input files provided to ensure they are suitable for further processing.


## Conceptual Info

This shim node is responsible for validating the input files, ensuring they meet the necessary criteria for further processing in the code complexity measurement pipeline.

## Docstring

### Summary
Validates a list of source files to ensure they are valid and suitable for processing.

### Parameters

- **source_files** (List[str]): A list of paths to the source code files to be validated.

### Returns

str: A string indicating the result of the validation. The exact format and content are to be determined based on the specific validation criteria.

### Raises

- ValueError: Raised when the input list is empty or when any of the file paths are invalid or inaccessible.
- TypeError: Raised when the input is not a list of strings.

### Examples

```python
>>> source_files = ['/path/to/file1.py', '/path/to/file2.py']
>>> validate_input_files(source_files=source_files)
'Validation successful'
```

```python
>>> source_files = []
>>> validate_input_files(source_files=source_files)
ValueError: Input list cannot be empty
```
