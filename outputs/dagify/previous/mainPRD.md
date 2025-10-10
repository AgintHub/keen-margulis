# codequalityanalysisworkflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'codequalityanalysisworkflow' module.

## Table of Contents

- [collect_source_code](#collect_source_code)

- [perform_static_code_analysis](#perform_static_code_analysis)

- [measure_code_complexity](#measure_code_complexity)

- [check_code_style](#check_code_style)

- [compile_analysis_report](#compile_analysis_report)



---

## collect_source_code

### Description
Gather the source code files to be analyzed.

### Conceptual Info

This node is responsible for collecting all relevant source code files from a given repository or project directory, making them available for subsequent analysis tasks.

### Docstring

**Summary:** Collects source code files from a specified directory or repository.

**Parameters:**

- repository_path (str): Path to the repository or project directory to search for source code files.
**Returns:** List[str] - A list of paths to the collected source code files.

**Raises:**

- FileNotFoundError: If the specified repository_path does not exist.
- PermissionError: If there is no permission to access the repository_path or any of its contents.
**Examples:**

```python
>>> collect_source_code(repository_path='/home/user/project')
['/home/user/project/file1.py', '/home/user/project/file2.py']
```

```python
>>> collect_source_code(repository_path='/home/user/non_existent_project')
FileNotFoundError: /home/user/non_existent_project does not exist.
```



---

## perform_static_code_analysis

### Description
Run static code analysis tools to identify potential issues and vulnerabilities.

### Conceptual Info

This node executes static code analysis on the source code files collected by its parent node, 'collect_source_code', to identify potential issues and vulnerabilities.

### Docstring

**Summary:** Perform static code analysis on the provided source code files to identify issues and vulnerabilities.

**Parameters:**

- source_code_files (List[str]): List of paths to source code files collected by the 'collect_source_code' node.
**Returns:** Tuple[List[str], List[str]] - A tuple containing two lists: 'static_analysis_results' and 'vulnerabilities_found'. The first list contains issues identified by static code analysis, and the second list contains vulnerabilities detected.

**Raises:**

- FileNotFoundError: If any of the source code files listed in 'source_code_files' are not found.
- AnalysisToolError: If there's an error running the static code analysis tools.
**Examples:**

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



---

## measure_code_complexity

### Description
Calculate code complexity metrics such as cyclomatic complexity.

### Conceptual Info

This node measures the complexity of the source code by calculating metrics such as cyclomatic complexity for each file collected by the 'collect_source_code' node.

### Docstring

**Summary:** Calculates code complexity metrics for a list of source code files.

**Parameters:**

- source_code_files (List[str]): List of paths to source code files as provided by the 'collect_source_code' node.
**Returns:** Tuple[List[float], List[int]] - A tuple containing two lists: the first list contains complexity metrics for each file, and the second list contains cyclomatic complexity values for each file.

**Raises:**

- FileNotFoundError: If any of the source code files listed in 'source_code_files' do not exist.
- ValueError: If the input 'source_code_files' is empty or not a list.
**Examples:**

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



---

## check_code_style

### Description
Analyze code style and formatting consistency.

### Conceptual Info

This node analyzes the style and formatting consistency of the source code files collected by the 'collect_source_code' node.

### Docstring

**Summary:** Analyze code style and formatting consistency using linters or style checkers.

**Parameters:**

- source_code_files (List[str]): List of paths to source code files collected by the 'collect_source_code' node.
**Returns:** Tuple[List[str], List[str]] - A tuple containing a list of style issues identified and a list of formatting errors detected.

**Raises:**

- FileNotFoundError: If any of the source code files are not found.
- Exception: If there is an error during the analysis process.
**Examples:**

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



---

## compile_analysis_report

### Description
Compile a comprehensive report summarizing the analysis results.

### Conceptual Info

This node aggregates analysis results from static code analysis, complexity measurement, and style checking to generate a comprehensive report.

### Docstring

**Summary:** Compile a comprehensive report summarizing the analysis results from static code analysis, complexity measurement, and style checking.

**Parameters:**

- static_analysis_results (List[str]): List of issues identified by static code analysis from perform_static_code_analysis node.
- vulnerabilities_found (List[str]): List of vulnerabilities detected by static code analysis from perform_static_code_analysis node.
- complexity_metrics (List[float]): List of complexity metrics for each file from measure_code_complexity node.
- cyclomatic_complexity (List[int]): Cyclomatic complexity values for each file from measure_code_complexity node.
- style_issues (List[str]): List of style issues identified by check_code_style node.
- formatting_errors (List[str]): List of formatting errors detected by check_code_style node.
**Returns:** Tuple[str, List[str], float] - A tuple containing the analysis summary, list of recommendations, and overall code quality score.

**Raises:**

- ValueError: If any of the input lists are empty or invalid.
**Examples:**

```python
>>> static_analysis_results = ['issue1', 'issue2']
>>> vulnerabilities_found = ['vuln1']
>>> complexity_metrics = [0.5, 0.7]
>>> cyclomatic_complexity = [3, 5]
>>> style_issues = ['style_issue1']
>>> formatting_errors = ['formatting_error1']
>>> analysis_summary, recommendations, quality_score = compile_analysis_report(static_analysis_results, vulnerabilities_found, complexity_metrics, cyclomatic_complexity, style_issues, formatting_errors)
('Analysis Summary: Found 2 issues, 1 vulnerability, and 2 complexity metrics.', ['Fix issue1', 'Reduce cyclomatic complexity'], 0.8)
```

