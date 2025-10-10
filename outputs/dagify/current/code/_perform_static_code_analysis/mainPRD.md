# _perform_static_code_analysis - Complete PRD Documentation

## Overview
PRDs for nodes in the '_perform_static_code_analysis' module.

## Table of Contents

- [validate_source_files_exist](#validate_source_files_exist)

- [run_static_analysis_tools](#run_static_analysis_tools)

- [scan_for_vulnerabilities](#scan_for_vulnerabilities)

- [filter_and_format_issues](#filter_and_format_issues)

- [format_vulnerability_results](#format_vulnerability_results)



---

## validate_source_files_exist

### Description
Validates the existence of source files provided as input file paths.

### Conceptual Info

This shim function validates whether the source code files provided exist in the system.

### Docstring

**Summary:** Validates the existence of source files provided as input file paths.

**Parameters:**

- file_paths (str): A comma-separated string of file paths to validate.
**Returns:** str - A success message if all files exist, otherwise an error message.

**Raises:**

- FileNotFoundError: If any of the provided file paths do not exist.
- TypeError: If the input is not a string or if the string is not properly formatted.
**Examples:**

```python
>>> validate_source_files_exist(file_paths='path/to/file1.py,path/to/file2.py')
'All files exist.'
```

```python
>>> validate_source_files_exist(file_paths='path/to/nonexistent_file.py')
'File not found: path/to/nonexistent_file.py'
```



---

## run_static_analysis_tools

### Description
Runs static analysis tools on the provided source code files and returns the analysis results as a list of strings.

### Conceptual Info

This shim node is responsible for executing static analysis tools on the provided source code files. It plays a crucial role in identifying potential issues and vulnerabilities in the code.

### Docstring

**Summary:** Runs static analysis tools on the given source files and returns the analysis results.

**Parameters:**

- source_files (str): Path(s) to the source code files to be analyzed. This can be a single file path or multiple paths separated by a delimiter.
**Returns:** List[str] - A list of strings representing the issues identified by the static analysis tools. Each string may contain details about the issue, such as its location and description.

**Raises:**

- FileNotFoundError: If any of the specified source files do not exist.
- ValueError: If the input source_files is empty or malformed.
**Examples:**

```python
>>> run_static_analysis_tools(source_files='path/to/source/file1.py')
['issue1: line 10', 'issue2: line 20']
```

```python
>>> run_static_analysis_tools(source_files='path/to/source/file1.py,path/to/source/file2.py')
['file1: issue1: line 10', 'file2: issue2: line 20']
```



---

## scan_for_vulnerabilities

### Description
Scans the given source files for potential security vulnerabilities and returns a list of detected issues.

### Conceptual Info

This shim function is designed to identify potential security vulnerabilities within the provided source code files, playing a critical role in the static code analysis pipeline.

### Docstring

**Summary:** Scans source code files for security vulnerabilities and returns a list of detected issues.

**Parameters:**

- source_files (str): A string representing the paths to source code files to be analyzed for vulnerabilities.
**Returns:** List[str] - A list of strings where each string represents a vulnerability detected in the source code.

**Raises:**

- ValueError: If the input source_files string is empty or malformed.
- TypeError: If the input source_files is not of type str.
**Examples:**

```python
>>> scan_for_vulnerabilities(source_files='/path/to/source/code')
['SQL Injection vulnerability detected', 'Cross-site scripting vulnerability detected']
```

```python
>>> scan_for_vulnerabilities(source_files='/path/to/another/source/code')
['Path traversal vulnerability detected']
```



---

## filter_and_format_issues

### Description
Filters and formats issues identified by static code analysis tools.

### Conceptual Info

This shim node is responsible for taking raw issues from static code analysis, filtering them based on certain criteria, and then formatting them into a standardized output.

### Docstring

**Summary:** Filters and formats raw issues from static code analysis into a list of strings.

**Parameters:**

- raw_issues (str): A string containing raw issues identified by static code analysis, potentially in a serialized or raw text format.
**Returns:** List[str] - A list of strings where each string represents a filtered and formatted issue.

**Raises:**

- ValueError: If the raw_issues string is malformed or cannot be processed.
- TypeError: If the input type is not a string.
**Examples:**

```python
>>> raw_issues = 'issue1:severity1,issue2:severity2'
>>> filtered_issues = filter_and_format_issues(raw_issues=raw_issues)
>>> print(filtered_issues)
['issue1:SEVERITY1', 'issue2:SEVERITY2']
```

```python
>>> raw_issues = 'error:file1.py:line1,message'
>>> filtered_issues = filter_and_format_issues(raw_issues=raw_issues)
>>> print(filtered_issues)
['FILE1.PY:LINE1:ERROR:MESSAGE']
```



---

## format_vulnerability_results

### Description
Formats raw vulnerability data into a structured list of strings for reporting.

### Conceptual Info

This shim function is responsible for taking raw vulnerability data and formatting it into a structured and readable format for reporting purposes.

### Docstring

**Summary:** Formats raw vulnerability data into a list of structured strings.

**Parameters:**

- raw_vulnerabilities (str): The raw vulnerability data that needs to be formatted.
**Returns:** List[str] - A list of strings where each string represents a formatted vulnerability result.

**Raises:**

- ValueError: If the raw_vulnerabilities input is not a valid string or is empty.
- TypeError: If the input type is not a string.
**Examples:**

```python
>>> raw_vulnerabilities = 'CVE-2022-1234:High:Some vulnerability description'
>>> formatted_results = format_vulnerability_results(raw_vulnerabilities)
>>> print(formatted_results)
['CVE-2022-1234: High Severity - Some vulnerability description']
```

```python
>>> raw_vulnerabilities = 'CVE-2022-5678:Medium:Another vulnerability description'
>>> formatted_results = format_vulnerability_results(raw_vulnerabilities)
>>> print(formatted_results)
['CVE-2022-5678: Medium Severity - Another vulnerability description']
```

