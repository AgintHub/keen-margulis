# run_static_analysis_tools PRD

## Description
Runs static analysis tools on the provided source code files and returns the analysis results as a list of strings.


## Conceptual Info

This shim node is responsible for executing static analysis tools on the provided source code files. It plays a crucial role in identifying potential issues and vulnerabilities in the code.

## Docstring

### Summary
Runs static analysis tools on the given source files and returns the analysis results.

### Parameters

- **source_files** (str): Path(s) to the source code files to be analyzed. This can be a single file path or multiple paths separated by a delimiter.

### Returns

List[str]: A list of strings representing the issues identified by the static analysis tools. Each string may contain details about the issue, such as its location and description.

### Raises

- FileNotFoundError: If any of the specified source files do not exist.
- ValueError: If the input source_files is empty or malformed.

### Examples

```python
>>> run_static_analysis_tools(source_files='path/to/source/file1.py')
['issue1: line 10', 'issue2: line 20']
```

```python
>>> run_static_analysis_tools(source_files='path/to/source/file1.py,path/to/source/file2.py')
['file1: issue1: line 10', 'file2: issue2: line 20']
```
