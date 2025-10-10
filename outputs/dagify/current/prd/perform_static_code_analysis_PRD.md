# perform_static_code_analysis PRD

## Description
Run static code analysis tools to identify potential issues and vulnerabilities.


## Conceptual Info

This node executes static code analysis on the source code files collected by its parent node, 'collect_source_code', to identify potential issues and vulnerabilities.

## Docstring

### Summary
Perform static code analysis on the provided source code files to identify issues and vulnerabilities.

### Parameters

- **source_code_files** (List[str]): List of paths to source code files collected by the 'collect_source_code' node.

### Returns

Tuple[List[str], List[str]]: A tuple containing two lists: 'static_analysis_results' and 'vulnerabilities_found'. The first list contains issues identified by static code analysis, and the second list contains vulnerabilities detected.

### Raises

- FileNotFoundError: If any of the source code files listed in 'source_code_files' are not found.
- AnalysisToolError: If there's an error running the static code analysis tools.

### Examples

```python
>>> source_code_files = ['/path/to/file1.py', '/path/to/file2.py']
>>> static_analysis_results, vulnerabilities_found = perform_static_code_analysis(source_code_files)
(['unused import', 'undefined variable'], ['SQL injection vulnerability'])
```

```python
>>> source_code_files = ['/path/to/secure_code.py']
>>> static_analysis_results, vulnerabilities_found = perform_static_code_analysis(source_code_files)
([], [])
```
