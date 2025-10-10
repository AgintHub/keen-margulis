# get_article_texts PRD

## Description
Retrieves the full text of news articles given a list of titles.


## Conceptual Info

This shim acts as an interface to a content retrieval service, fetching full article texts based on provided titles.

## Docstring

### Summary
Fetches full text content for each article title supplied.

### Parameters

- **titles** (List[str]): A list of article titles to retrieve the full text for.

### Returns

List[str]: A list of article texts matching the order of the input titles.

### Raises

- ValueError: If the titles list is empty.
- TypeError: If titles is not a list of strings.
- RuntimeError: If an article corresponding to a title cannot be retrieved.

### Examples

```python
>>> texts = get_article_texts(titles=['Title A', 'Title B'])
['Full text of Title A', 'Full text of Title B']
```

```python
>>> texts = get_article_texts(titles=['Nonexistent Article'])
RuntimeError: Article not found for title 'Nonexistent Article'
```
