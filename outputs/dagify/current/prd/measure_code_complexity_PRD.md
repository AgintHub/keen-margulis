# measure_code_complexity PRD

## Description
Calculate code complexity metrics such as cyclomatic complexity.


## Conceptual Info

This node measures the complexity of the source code by calculating metrics such as cyclomatic complexity for each file collected by the 'collect_source_code' node.

## Docstring

### Summary
Calculates code complexity metrics for a list of source code files.

### Parameters

- **source_code_files** (List[str]): List of paths to source code files as provided by the 'collect_source_code' node.

### Returns

Tuple[List[float], List[int]]: A tuple containing two lists: the first list contains complexity metrics for each file, and the second list contains cyclomatic complexity values for each file.

### Raises

- FileNotFoundError: If any of the source code files listed in 'source_code_files' do not exist.
- ValueError: If the input 'source_code_files' is empty or not a list.

### Examples

```python
>>> source_code_files = ['/path/to/file1.py', '/path/to/file2.py']
>>> complexity_metrics, cyclomatic_complexity = measure_code_complexity(source_code_files)
[0.5, 0.7]
[3, 5]
```

```python
>>> source_code_files = ['/path/to/file3.py']
>>> complexity_metrics, cyclomatic_complexity = measure_code_complexity(source_code_files)
[0.3]
[2]
```
