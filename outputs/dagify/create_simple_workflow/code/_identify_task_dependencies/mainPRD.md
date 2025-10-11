# _identify_task_dependencies - Complete PRD Documentation

## Overview
PRDs for nodes in the '_identify_task_dependencies' module.

## Table of Contents

- [normalize_task_names](#normalize_task_names)

- [normalize_task_descriptions](#normalize_task_descriptions)

- [detect_semantic_relationships](#detect_semantic_relationships)

- [detect_keyword_dependencies](#detect_keyword_dependencies)

- [merge_dependency_sources](#merge_dependency_sources)

- [filter_duplicate_dependencies](#filter_duplicate_dependencies)

- [format_dependency_pairs](#format_dependency_pairs)



---

## normalize_task_names

### Description
Normalizes a list of task names by lower‑casing, trimming whitespace, and removing non‑alphanumeric characters.

### Conceptual Info

This shim prepares raw task names for downstream dependency analysis by enforcing a consistent format.

### Docstring

**Summary:** Normalize task names to a consistent format.

**Parameters:**

- task_names (List[str]): A list of raw task names to be normalised.
**Returns:** List[str] - The input names transformed to lowercase, stripped of leading/trailing whitespace, and with all non‑alphanumeric characters removed.

**Raises:**

- ValueError: Raised if `task_names` is an empty list.
- TypeError: Raised if any element of `task_names` is not a string.
**Examples:**

```python
>>> normalized = normalize_task_names(["  Deploy   App  ", "Test-API!", "Review/Docs"])
>>> print(normalized)
['deploy app', 'testapi', 'reviewdocs']
```

```python
>>> try:
...     normalize_task_names([])
>>> except ValueError as e:
...     print(str(e))
"task_names list cannot be empty"
```



---

## normalize_task_descriptions

### Description
Normalizes a list of task description strings into clean, lowercase, whitespace-trimmed format.

### Conceptual Info

The normalize_task_descriptions shim prepares raw task description strings for downstream processing by standardizing their formatting and removing extraneous whitespace and punctuation.

### Docstring

**Summary:** Normalizes task description strings into a clean, lowercase, whitespace-trimmed list.

**Parameters:**

- descriptions (List[str]): A list of raw task description strings to be normalized.
**Returns:** List[str] - A list of normalized task description strings, each trimmed, lowercased, and free of redundant whitespace or punctuation.

**Raises:**

- ValueError: Raised if the input list is empty or contains non-string elements.
- TypeError: Raised if the input is not a list.
**Examples:**

```python
>>> descriptions = ['  Task 1: Clean data  ', 'Task 2: Build model\n', 'Analyze results']
>>> normalize_task_descriptions(descriptions)
['task 1: clean data', 'task 2: build model', 'analyze results']
```

```python
>>> normalize_task_descriptions(['   Verify results!   '])
['verify results']
```



---

## detect_semantic_relationships

### Description
Detects semantic relationships between task names and descriptions, returning a list of task pairs that have a semantic dependency.

### Conceptual Info

This shim encapsulates the logic needed to discover semantic dependencies among tasks. It processes the names and descriptions of tasks, applies semantic analysis (e.g., similarity thresholds or NLP models), and outputs the identified relationships for downstream dependency merging.

### Docstring

**Summary:** Detects semantic relationships between given task names and descriptions, returning a list of task pairs that are semantically related.

**Parameters:**

- task_names (List[str]): List of task names to analyze.
- descriptions (List[str]): List of task descriptions corresponding to each task name.
**Returns:** List[tuple] - A list of tuples where each tuple contains two task names that have a detected semantic relationship.

**Raises:**

- ValueError: Raised when either task_names or descriptions is empty.
- ValueError: Raised when task_names and descriptions have different lengths.
- TypeError: Raised when task_names or descriptions are not lists of strings.
**Examples:**

```python
>>> task_names = ['Build Frontend', 'Write Backend', 'Test API']
>>> descriptions = ['Create the user interface', 'Develop server logic', 'Verify API endpoints']
>>> matches = detect_semantic_relationships(task_names=task_names, descriptions=descriptions)
[('Build Frontend', 'Write Backend')]
```

```python
>>> task_names = ['Task A', 'Task B']
>>> descriptions = ['Do something', 'Do another thing']
>>> matches = detect_semantic_relationships(task_names=task_names, descriptions=descriptions)
[]
```



---

## detect_keyword_dependencies

### Description
Detect keyword-based dependencies between tasks by analyzing task names and descriptions.

### Conceptual Info

This shim identifies implicit task dependencies by matching keyword patterns in task descriptions, returning ordered pairs of task names that indicate a prerequisite relationship.

### Docstring

**Summary:** Detect keyword-based dependencies between two lists of task names and descriptions.

**Parameters:**

- task_names (List[str]): List of task names to analyze.
- descriptions (List[str]): Corresponding list of natural‑language descriptions for each task.
**Returns:** List[tuple] - A list of tuples (predecessor_task, dependent_task) representing dependencies inferred from keyword matches.

**Raises:**

- ValueError: Raised when either input list is empty or the two lists have differing lengths.
- TypeError: Raised when input types are not lists of strings or contain non-string elements.
**Examples:**

```python
>>> detect_keyword_dependencies(['Clean data', 'Analyze data'], ['Clean the raw data before analysis', 'Analyze the cleaned data'])
[('Clean data', 'Analyze data')]
```

```python
>>> detect_keyword_dependencies(['Read book', 'Write summary'], ['Read the book', 'Write a summary of the book'])
[]
```



---

## merge_dependency_sources

### Description
Combines semantic and keyword dependency match lists into a single list of dependency tuples.

### Conceptual Info

The function merges two sources of dependency information (semantic and keyword based) to produce a consolidated dependency graph that can be further processed by downstream steps such as duplicate filtering.

### Docstring

**Summary:** Merges semantic and keyword dependency lists into a single dependency list.

**Parameters:**

- semantic_matches (List[tuple]): List of dependency pairs detected by semantic analysis. Each pair is a tuple `(parent_task, child_task)`.
- keyword_matches (List[tuple]): List of dependency pairs detected by keyword-based analysis. Each pair is a tuple `(parent_task, child_task)`.
**Returns:** List[tuple] - A list of unique dependency pairs combining both semantic and keyword sources. The order preserves the original lists' order and removes duplicates.

**Raises:**

- ValueError: If either `semantic_matches` or `keyword_matches` is empty or not a list.
- TypeError: If the elements of `semantic_matches` or `keyword_matches` are not tuples of length 2.
**Examples:**

```python
>>> merge_dependency_sources(
...     semantic_matches=[('TaskA', 'TaskB')],
...     keyword_matches=[('TaskB', 'TaskC')]
>>> )
[('TaskA', 'TaskB'), ('TaskB', 'TaskC')]
```

```python
>>> merge_dependency_sources(
...     semantic_matches=[('TaskA', 'TaskB')],
...     keyword_matches=[('TaskA', 'TaskB'), ('TaskC', 'TaskD')]
>>> )
[('TaskA', 'TaskB'), ('TaskC', 'TaskD')]
```



---

## filter_duplicate_dependencies

### Description
Filter out duplicate dependency pairs from a list of task dependency tuples, preserving order.

### Conceptual Info

This shim removes duplicate dependency pairs from the merged dependencies produced by semantic and keyword detection, ensuring downstream processes work with unique relationships.

### Docstring

**Summary:** Filter duplicate dependencies from a list of task dependency tuples.

**Parameters:**

- dependencies (List[Tuple[str, str]]): List of dependency pairs to be de-duplicated.
**Returns:** LIST_STR - List of unique dependency tuples represented as strings.

**Raises:**

- ValueError: If the dependencies list is empty or contains invalid tuple elements.
- TypeError: If the dependencies argument is not a list or contains non-tuple elements.
**Examples:**

```python
>>> deps = [('task1', 'task2'), ('task2', 'task3'), ('task1', 'task2')]
>>> cleaned = filter_duplicate_dependencies(dependencies=deps)
['(task1, task2)', '(task2, task3)']
```

```python
>>> deps = [('a', 'b'), ('a', 'b'), ('b', 'c')]
>>> cleaned = filter_duplicate_dependencies(dependencies=deps)
['(a, b)', '(b, c)']
```



---

## format_dependency_pairs

### Description
Formats a list of dependency tuples into human‑readable strings of the form "parent -> child".

### Conceptual Info

Transforms raw dependency tuples into concise string representations for reporting and further processing.

### Docstring

**Summary:** Converts a list of dependency tuples into formatted strings.

**Parameters:**

- dependencies (List[tuple]): A list of tuples where each tuple contains two task names (parent, child).
**Returns:** List[str] - A list of strings, each representing a dependency pair in the form 'parent -> child'.

**Raises:**

- ValueError: Raised when the input list is empty or contains non‑tuple elements.
- TypeError: Raised when the input is not a list.
**Examples:**

```python
>>> format_dependency_pairs([('Task1', 'Task2'), ('Task3', 'Task4')])
["Task1 -> Task2", "Task3 -> Task4"]
```

```python
>>> format_dependency_pairs([('A', 'B')])
["A -> B"]
```

