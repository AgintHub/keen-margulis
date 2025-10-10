# extract_source_names PRD

## Description
Extracts a list of source names from the provided article data string for a given source identifier.


## Conceptual Info

The shim serves as a lightweight extraction layer that parses raw article data (typically JSON or similar) and retrieves the source names for each article, allowing downstream processing to identify and label news items.

## Docstring

### Summary
Extract source names from article data for a specified source identifier.

### Parameters

- **data** (str): Raw article data in JSON-like string format containing one or more articles with a 'source' field.
- **source** (str): The identifier of the source from which the articles were fetched, used to filter or contextualize extracted names.

### Returns

List[str]: A list of source names corresponding to each article present in the provided data.

### Raises

- ValueError: Raised when the data string is empty or does not contain the expected 'articles' structure.
- TypeError: Raised when either 'data' or 'source' is not of type 'str'.

### Examples

```python
>>> article_data = '{"articles":[{"title":"A","source":"News A"},{"title":"B","source":"News B"}]}'
>>> extract_source_names(article_data, "News A")
["News A", "News B"]
```

```python
>>> article_data = ''
>>> extract_source_names(article_data, "News A")
ValueError: Article data is empty or malformed.
```
