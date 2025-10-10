# scan_directory_for_source_files PRD

## Description
Scans a specified directory for source code files and returns their paths


## Conceptual Info

This shim is responsible for scanning a given directory for source code files. It is a crucial step in collecting source code files from a repository.

## Docstring

### Summary
Scans a directory for source code files and returns their paths

### Parameters

- **directory_path** (str): The path to the directory that needs to be scanned for source code files

### Returns

List[str]: A list containing the paths to all source code files found in the specified directory

### Raises

- FileNotFoundError: If the specified directory does not exist
- PermissionError: If there are insufficient permissions to access the directory
- NotADirectoryError: If the provided path is not a directory

### Examples

```python
>>> scan_directory_for_source_files(directory_path='/path/to/project')
>>> # Assuming /path/to/project contains source code files
['/path/to/project/file1.py', '/path/to/project/file2.java']
```

```python
>>> scan_directory_for_source_files(directory_path='/non/existent/directory')
FileNotFoundError: Directory '/non/existent/directory' not found
```
