# validate_collected_data PRD

## Description
Validates and normalizes collected article data before downstream processing.


## Conceptual Info

Ensures consistency and integrity of article metadata gathered from multiple news sources, preparing it for model ingestion.

## Docstring

### Summary
Validate the structure and contents of article collections, ensuring all lists are non-empty, of identical length, and contain only string elements.

### Parameters

- **urls** (List[str]): A list of article URLs collected from various news sources.
- **titles** (List[str]): A list of article titles corresponding to the URLs.
- **texts** (List[str]): A list of full article texts.
- **sources** (List[str]): A list of source names from which each article was retrieved.

### Returns

dict: A dictionary with keys 'urls', 'titles', 'texts', and 'sources' mapping to cleaned lists of strings. The dictionary is returned as a JSON-encoded string.

### Raises

- TypeError: Raised when any argument is not a list or contains non-string elements.
- ValueError: Raised when the input lists are empty or do not share the same length.

### Examples

```python
>>> validated = validate_collected_data(

...     urls=['https://a.com', 'https://b.com'],

...     titles=['Title A', 'Title B'],

...     texts=['Text A', 'Text B'],

...     sources=['Source A', 'Source B']

>>> )
>>> print(validated)
{'urls': ['https://a.com', 'https://b.com'], 'titles': ['Title A', 'Title B'], 'texts': ['Text A', 'Text B'], 'sources': ['Source A', 'Source B']}
```

```python
>>> try:
...     validate_collected_data(urls=['https://a.com'], titles=['Title A'], texts=['Text A'], sources=['Source A', 'Source B'])
>>> except ValueError as e:
...     print(e)
Input lists must all be of the same non-zero length.
```
