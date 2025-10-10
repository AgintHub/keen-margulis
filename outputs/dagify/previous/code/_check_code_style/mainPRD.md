# _check_code_style - Complete PRD Documentation

## Overview
PRDs for nodes in the '_check_code_style' module.

## Table of Contents

- [validate_source_files_exist](#validate_source_files_exist)

- [run_style_linter](#run_style_linter)

- [run_formatting_checker](#run_formatting_checker)



---

## validate_source_files_exist

### Description
Validates the existence of given source files.

### Conceptual Info

This shim function is responsible for validating the existence of source code files provided as input. It plays a crucial role in ensuring that subsequent operations are performed on valid files.

### Docstring

**Summary:** Validates a list of source file paths and returns those that exist.

**Parameters:**

- file_paths (str): A string containing a list of file paths to validate, separated by commas or other delimiters as needed.
**Returns:** List[str] - A list of file paths that were found to exist.

**Raises:**

- ValueError: If the input string is malformed or empty.
- TypeError: If the input is not a string.
**Examples:**

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



---

## run_style_linter

### Description
Runs a style linter on the given file paths and returns a list of style issues identified.

### Conceptual Info

This shim function represents a style linter that checks the given source code files for style issues and returns a list of problems found.

### Docstring

**Summary:** Runs a style linter on the provided file paths and returns a list of style issues.

**Parameters:**

- file_paths (str): A string containing file paths to be checked by the linter, separated by commas or a specific delimiter.
**Returns:** List[str] - A list of strings where each string represents a style issue identified by the linter.

**Raises:**

- ValueError: If the input file paths are invalid or if the linter encounters an internal error.
- TypeError: If the input type is not a string.
**Examples:**

```python
>>> run_style_linter(file_paths='path/to/file1.py,path/to/file2.py')
['style_issue1', 'style_issue2']
```

```python
>>> run_style_linter(file_paths='path/to/file3.py')
['style_issue3']
```



---

## run_formatting_checker

### Description
Checks code formatting for the given file paths and returns a list of formatting errors

### Conceptual Info

This shim node is responsible for checking the code formatting of given source code files and returning any formatting errors found.

### Docstring

**Summary:** Checks code formatting for the given file paths and returns a list of formatting errors

**Parameters:**

- file_paths (str): A string containing the paths to the files to be checked, separated by commas or a single path
**Returns:** List[str] - A list of strings where each string represents a formatting error detected in the code files

**Raises:**

- ValueError: If the input file paths are invalid or if no files are found at the given paths
- TypeError: If the input type is not a string
**Examples:**

```python
>>> run_formatting_checker(file_paths='path/to/file1.py,path/to/file2.py')
['file1.py:1:1: error: missing whitespace around operator']
```

```python
>>> run_formatting_checker(file_paths='path/to/single_file.py')
['single_file.py:5:5: error: inconsistent indentation']
```

