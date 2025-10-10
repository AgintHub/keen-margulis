# get_predefined_news_sources PRD

## Description
Retrieves a predefined list of news source identifiers to be used for article fetching.


## Conceptual Info

The get_predefined_news_sources shim supplies a static set of news source identifiers that downstream nodes use to fetch articles from those sources.

## Docstring

### Summary
Return a list of predefined news source identifiers for article collection.

### Returns

List[str]: A list of string identifiers for news sources such as 'AP News', 'Reuters', 'BBC News'.

### Raises

- ValueError: If the internal source configuration is empty or malformed.

### Examples

```python
>>> sources = get_predefined_news_sources()
['AP News', 'Reuters', 'BBC News']
```

```python
>>> len(get_predefined_news_sources())
3
```
