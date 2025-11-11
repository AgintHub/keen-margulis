# _identify_dependencies_between_subtasks - Complete PRD Documentation

## Overview
PRDs for nodes in the '_identify_dependencies_between_subtasks' module.

## Table of Contents

- [validate_input_parameters](#validate_input_parameters)

- [parse_sequencing_requirements](#parse_sequencing_requirements)

- [validate_dependencies_against_subtasks](#validate_dependencies_against_subtasks)

- [check_dependencies_exist](#check_dependencies_exist)

- [format_dependency_list](#format_dependency_list)



---

## validate_input_parameters

### Description
Validates the input parameters subtask_list and sequencing_requirements to ensure they are in the correct format and contain the necessary information.

### Conceptual Info

The validate_input_parameters shim is responsible for validating the input parameters to ensure they are in the correct format and contain the necessary information for the subsequent nodes to function correctly.

### Docstring

**Summary:** Validate the input parameters subtask_list and sequencing_requirements.

**Parameters:**

- subtask_list (list[str]): List of subtasks or steps to achieve the task objective.
- sequencing_requirements (str): Description of any sequencing or ordering requirements between subtasks.
**Returns:** str - Output indicating whether the input parameters are valid or not.

**Raises:**

- ValueError: When input validation fails due to incorrect format or missing information.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> validate_input_parameters(subtask_list=['task1', 'task2'], sequencing_requirements='task1 -> task2')
'Input parameters are valid'
```

```python
>>> validate_input_parameters(subtask_list=[], sequencing_requirements='')
'Input parameters are invalid'
```



---

## parse_sequencing_requirements

### Description
Parses sequencing requirements from a string into a list of dependencies.

### Conceptual Info

The parse_sequencing_requirements shim function takes a string describing sequencing requirements and returns a list of dependencies.

### Docstring

**Summary:** Parses sequencing requirements from a string into a list of dependencies.

**Parameters:**

- sequencing_requirements (str): Input string containing sequencing requirements.
**Returns:** List[str] - List of parsed dependencies.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> parse_sequencing_requirements('Task A must be completed before Task B')
['Task A -> Task B']
```

```python
>>> parse_sequencing_requirements('Task C and Task D are independent')
[]
```



---

## validate_dependencies_against_subtasks

### Description
Validates a list of dependencies against a list of subtasks to ensure they are valid and properly formatted.

### Conceptual Info

This shim function validates a list of dependencies against a list of subtasks to ensure they are valid and properly formatted.

### Docstring

**Summary:** Validates a list of dependencies against a list of subtasks.

**Parameters:**

- dependencies (str): A string representation of a list of dependencies, where each dependency is represented as 'subtask_id_1 -> subtask_id_2'
- subtask_list (str): A string representation of a list of subtasks
**Returns:** List[str] - A list of validated dependencies

**Raises:**

- ValueError: When a dependency is invalid or does not exist in the subtask list
- TypeError: When the input types are incorrect
**Examples:**

```python
>>> validate_dependencies_against_subtasks(dependencies='A -> B', subtask_list='A,B,C')
['A -> B']
```

```python
>>> validate_dependencies_against_subtasks(dependencies='A -> D', subtask_list='A,B,C')
[]
```



---

## check_dependencies_exist

### Description
Checks if dependencies exist between subtasks.

### Conceptual Info

The check_dependencies_exist shim function checks if there are any dependencies between subtasks.

### Docstring

**Summary:** Checks if dependencies exist between subtasks.

**Parameters:**

- dependencies (str): A string representing dependencies between subtasks.
**Returns:** bool - True if dependencies exist, False otherwise.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> check_dependencies_exist('subtask1 -> subtask2')
True
```

```python
>>> check_dependencies_exist('')
False
```



---

## format_dependency_list

### Description
Formats a list of dependencies into a string representation.

### Conceptual Info

The format_dependency_list shim function formats a list of dependencies into a string representation, which can be used to describe the dependencies between subtasks.

### Docstring

**Summary:** Formats a list of dependencies into a string representation.

**Parameters:**

- dependencies (str): A list of dependencies where each dependency is represented as 'subtask_id_1 -> subtask_id_2'.
**Returns:** str - The formatted dependency list as a string.

**Raises:**

- ValueError: When the input dependencies are invalid or empty.
- TypeError: When the input type is incorrect.
**Examples:**

```python
>>> format_dependency_list(dependencies=['A -> B', 'B -> C'])
'A -> B, B -> C'
```

```python
>>> format_dependency_list(dependencies=[])
''
```

