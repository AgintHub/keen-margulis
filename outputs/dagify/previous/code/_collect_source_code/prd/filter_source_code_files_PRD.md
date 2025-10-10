# filter_source_code_files PRD

## Description
Filters a list of file paths to identify and return only the source code files.


## Conceptual Info

This shim node filters a given list of file paths to identify and return only the paths that correspond to source code files, playing a crucial role in source code analysis pipelines.

## Docstring

### Summary
Filters a list of file paths to return only source code files.

### Parameters

- **file_paths** (str): A string containing file paths to be filtered, expected to be in a format that can be parsed into a list (e.g., comma-separated or serialized list).

### Returns

List[str]: A list of file paths that are identified as source code files.

### Raises

- ValueError: If the input string cannot be parsed into a list of file paths.
- TypeError: If the input is not a string.

### Examples

```python
>>> file_paths_str = 'path/to/file1.py,path/to/file2.txt,path/to/file3.java'
>>> filtered_files = filter_source_code_files(file_paths=file_paths_str)
['path/to/file1.py', 'path/to/file3.java']
```

```python
>>> file_paths_str = '["path/to/file1.py","path/to/file2.txt","path/to/file3.java"]'
>>> filtered_files = filter_source_code_files(file_paths=file_paths_str)
['path/to/file1.py', 'path/to/file3.java']
```
