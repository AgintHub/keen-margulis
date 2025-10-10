# collect_source_code PRD

## Description
Gather the source code files to be analyzed.


## Conceptual Info

This node is responsible for collecting all relevant source code files from a given repository or project directory, making them available for subsequent analysis tasks.

## Docstring

### Summary
Collects source code files from a specified directory or repository.

### Parameters

- **repository_path** (str): Path to the repository or project directory to search for source code files.

### Returns

List[str]: A list of paths to the collected source code files.

### Raises

- FileNotFoundError: If the specified repository_path does not exist.
- PermissionError: If there is no permission to access the repository_path or any of its contents.

### Examples

```python
>>> collect_source_code(repository_path='/home/user/project')
['/home/user/project/file1.py', '/home/user/project/file2.py']
```

```python
>>> collect_source_code(repository_path='/home/user/non_existent_project')
FileNotFoundError: /home/user/non_existent_project does not exist.
```
