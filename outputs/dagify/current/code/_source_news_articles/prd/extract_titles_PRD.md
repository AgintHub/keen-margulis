# extract_titles PRD

## Description
Extracts a list of article titles from a string containing article data.


## Conceptual Info

In the news‑article aggregation pipeline, this shim is responsible for isolating headline titles from raw article data so that downstream components can collect, validate, and store titles efficiently.

## Docstring

### Summary
Extracts headline titles from a raw string of article data.

### Parameters

- **data** (str): A string representation of one or more articles. Each article should contain a line starting with 'Title: ' followed by the headline text.

### Returns

list[str]: A list of the extracted titles in the same order they appear in the input.

### Raises

- ValueError: If the input string is empty or contains no titles.
- TypeError: If the input parameter is not of type `str`.

### Examples

```python
>>> titles = extract_titles("Title: First News\nBody: ...\nTitle: Second News\nBody: ...")
>>> print(titles)
['First News', 'Second News']
```

```python
>>> extract_titles(123)
>>> extract_titles('')
TypeError: data must be a string
ValueError: input string contains no titles
```
