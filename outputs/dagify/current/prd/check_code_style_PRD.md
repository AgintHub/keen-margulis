# check_code_style PRD

## Description
Analyze code style and formatting consistency.


## Conceptual Info

This node analyzes the style and formatting consistency of the source code files collected by the 'collect_source_code' node.

## Docstring

### Summary
Analyze code style and formatting consistency using linters or style checkers.

### Parameters

- **source_code_files** (List[str]): List of paths to source code files collected by the 'collect_source_code' node.

### Returns

Tuple[List[str], List[str]]: A tuple containing a list of style issues identified and a list of formatting errors detected.

### Raises

- FileNotFoundError: If any of the source code files are not found.
- Exception: If there is an error during the analysis process.

### Examples

```python
>>> source_code_files = ['/path/to/file1.py', '/path/to/file2.py']
>>> style_issues, formatting_errors = check_code_style(source_code_files)
(['unused import', 'invalid indentation'], [' trailing whitespace', ' inconsistent spacing'])
```

```python
>>> source_code_files = ['/path/to/file3.py']
>>> style_issues, formatting_errors = check_code_style(source_code_files)
(['missing docstring'], [])
```
