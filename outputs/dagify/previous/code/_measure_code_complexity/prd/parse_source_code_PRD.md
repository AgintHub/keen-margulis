# parse_source_code PRD

## Description
Parses the given source code content into an Abstract Syntax Tree (AST) representation.


## Conceptual Info

This shim function is responsible for parsing source code content into an Abstract Syntax Tree (AST) that can be used for further analysis, such as measuring code complexity.

## Docstring

### Summary
Parses source code content into an AST representation.

### Parameters

- **content** (str): The source code content to be parsed into an AST.

### Returns

str: The AST representation of the source code as a string.

### Raises

- ValueError: If the input content is not valid source code.
- TypeError: If the input content is not a string.

### Examples

```python
>>> parsed_ast = parse_source_code(content='def example_function(): pass')
>>> print(parsed_ast)
'<ast.Module object at 0x...>'
```

```python
>>> try:
...     parse_source_code(content=123)
>>> except TypeError as e:
...     print(e)
'Input content must be a string.'
```
