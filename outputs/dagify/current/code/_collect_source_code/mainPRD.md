# _collect_source_code - Complete PRD Documentation

## Overview
PRDs for nodes in the '_collect_source_code' module.

## Table of Contents

- [extract_repository_path](#extract_repository_path)

- [validate_path_exists](#validate_path_exists)

- [check_path_permissions](#check_path_permissions)

- [scan_directory_for_source_files](#scan_directory_for_source_files)

- [filter_source_code_files](#filter_source_code_files)



---

## extract_repository_path

### Description
Extracts the repository path from the given input parameters.

### Conceptual Info

This shim function is responsible for extracting the repository path from the provided input parameters, playing a crucial role in the source code collection process.

### Docstring

**Summary:** Extracts the repository path based on the provided general input and additional keyword arguments.

**Parameters:**

- general_input (str): The primary input from which the repository path will be extracted.
- kwargs (str): Additional keyword arguments that may contain relevant information for extracting the repository path.
**Returns:** str - The extracted repository path as a string.

**Raises:**

- ValueError: If the general input or kwargs do not contain sufficient information to extract the repository path.
- TypeError: If the input types are not as expected, such as general_input not being a string.
**Examples:**

```python
>>> extract_repository_path(general_input='path/to/repo', kwargs='{}')
'path/to/repo'
```

```python
>>> extract_repository_path(general_input='invalid input', kwargs='{}')
ValueError: Invalid input format
```



---

## validate_path_exists

### Description
Validates whether a given file system path exists.

### Conceptual Info

This shim function is designed to check if a specified file system path exists, playing a crucial role in ensuring that subsequent operations are performed on valid paths.

### Docstring

**Summary:** Checks if a given file system path exists and returns an appropriate output.

**Parameters:**

- path (str): The file system path to be validated.
**Returns:** str - A string indicating the result of the path existence check.

**Raises:**

- TypeError: If the input 'path' is not a string.
- ValueError: If the input 'path' is an empty string or contains invalid characters.
**Examples:**

```python
>>> validate_path_exists(path='/home/user/valid_path')
'Path exists'
```

```python
>>> validate_path_exists(path='/home/user/non_existent_path')
'Path does not exist'
```



---

## check_path_permissions

### Description
Checks if the specified path has appropriate permissions.

### Conceptual Info

This shim function is responsible for verifying that a given path has the necessary permissions for the application to access or manipulate it.

### Docstring

**Summary:** Checks the permissions of a specified path and returns the result.

**Parameters:**

- path (str): The file system path to check for permissions.
**Returns:** str - A string indicating the result of the permission check.

**Raises:**

- PermissionError: If the path does not have the required permissions.
- FileNotFoundError: If the specified path does not exist.
- TypeError: If the input path is not a string.
**Examples:**

```python
>>> check_path_permissions(path='/home/user/repository')
'Path /home/user/repository is accessible.'
```

```python
>>> check_path_permissions(path='/restricted/access')
'Permission denied for path /restricted/access.'
```



---

## scan_directory_for_source_files

### Description
Scans a specified directory for source code files and returns their paths

### Conceptual Info

This shim is responsible for scanning a given directory for source code files. It is a crucial step in collecting source code files from a repository.

### Docstring

**Summary:** Scans a directory for source code files and returns their paths

**Parameters:**

- directory_path (str): The path to the directory that needs to be scanned for source code files
**Returns:** List[str] - A list containing the paths to all source code files found in the specified directory

**Raises:**

- FileNotFoundError: If the specified directory does not exist
- PermissionError: If there are insufficient permissions to access the directory
- NotADirectoryError: If the provided path is not a directory
**Examples:**

```python
>>> scan_directory_for_source_files(directory_path='/path/to/project')
>>> # Assuming /path/to/project contains source code files
['/path/to/project/file1.py', '/path/to/project/file2.java']
```

```python
>>> scan_directory_for_source_files(directory_path='/non/existent/directory')
FileNotFoundError: Directory '/non/existent/directory' not found
```



---

## filter_source_code_files

### Description
Filters a list of file paths to identify and return only the source code files.

### Conceptual Info

This shim node filters a given list of file paths to identify and return only the paths that correspond to source code files, playing a crucial role in source code analysis pipelines.

### Docstring

**Summary:** Filters a list of file paths to return only source code files.

**Parameters:**

- file_paths (str): A string containing file paths to be filtered, expected to be in a format that can be parsed into a list (e.g., comma-separated or serialized list).
**Returns:** List[str] - A list of file paths that are identified as source code files.

**Raises:**

- ValueError: If the input string cannot be parsed into a list of file paths.
- TypeError: If the input is not a string.
**Examples:**

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

