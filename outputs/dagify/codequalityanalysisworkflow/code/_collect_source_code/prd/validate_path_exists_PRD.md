# validate_path_exists PRD

## Description
Validates whether a given file system path exists.


## Conceptual Info

This shim function is designed to check if a specified file system path exists, playing a crucial role in ensuring that subsequent operations are performed on valid paths.

## Docstring

### Summary
Checks if a given file system path exists and returns an appropriate output.

### Parameters

- **path** (str): The file system path to be validated.

### Returns

str: A string indicating the result of the path existence check.

### Raises

- TypeError: If the input 'path' is not a string.
- ValueError: If the input 'path' is an empty string or contains invalid characters.

### Examples

```python
>>> validate_path_exists(path='/home/user/valid_path')
'Path exists'
```

```python
>>> validate_path_exists(path='/home/user/non_existent_path')
'Path does not exist'
```
