# compile_full_narrative PRD

## Description
Compiles a cohesive narrative string from title, introduction, context, impact, and conclusion components.


## Conceptual Info

This shim function is responsible for assembling the final narrative text that will be returned to the user. It takes discrete narrative components produced by earlier nodes and stitches them together in a logically ordered, readable format.

## Docstring

### Summary
Compile a full narrative string from separate parts.

### Parameters

- **title** (str): The title of the narrative.
- **intro** (str): Introductory paragraph setting the scene.
- **context** (str): Summary of the historical context.
- **impact** (str): Summary of how key factors impacted the event.
- **conclusion** (str): Concluding remarks linking the narrative to the conclusions.

### Returns

str: A single string containing the title, introduction, context, impact, and conclusion, each separated by a newline.

### Raises

- ValueError: Raised if any input string is empty or missing.
- TypeError: Raised if any input is not of type str.

### Examples

```python
>>> result = compile_full_narrative(
...     title='Historical Event',
...     intro='In the year 1914, tensions rose across Europe.',
...     context='The global tensions were high as alliances formed.',
...     impact='These tensions led to the outbreak of war.',
...     conclusion='Thus, the outcome was the start of a global conflict.'
>>> )
>>> print(result)
Historical Event\nIn the year 1914, tensions rose across Europe.\nThe global tensions were high as alliances formed.\nThese tensions led to the outbreak of war.\nThus, the outcome was the start of a global conflict.
```

```python
>>> try:
...     compile_full_narrative(title='', intro='Intro', context='Context', impact='Impact', conclusion='Conclusion')
>>> except ValueError as e:
...     print(e)
All narrative components must be non-empty strings.
```
