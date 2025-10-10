# filter_news_articles PRD

## Description
Enhances the original filtering logic by adding comprehensive input validation, detailed logging, and fallback handling to ensure reliability in downstream analyses.


## Conceptual Info

The filter_news_articles node cleanses a batch of fetched news articles by removing any that are irrelevant to the downstream analytical tasks or that appear more than once. It outputs a list of unique, relevant article identifiers and flags any removal, allowing downstream nodes such as categorization to operate on a refined dataset.

## Docstring

### Summary
Filter news articles to remove irrelevant or duplicate entries.

### Parameters

- **source_news_articles_input** (SourceNewsArticlesOutput): Validated output from the source_news_articles node.

### Returns

FilterNewsArticlesOutput: Output containing filtered and removed article ids, and a success flag.

### Raises

- ValueError: Raised when input validation fails.
- RuntimeError: Raised when internal filtering logic encounters an unexpected error.

### Examples

```python
>>> from filter_news_articles import filter_news_articles, SourceNewsArticlesOutput, FilterNewsArticlesOutput
>>> # Sample input with three articles
>>> input_data = SourceNewsArticlesOutput(
...     article_urls=['url1', 'url2', 'url3'],
...     article_titles=['Title A', 'Title B', 'Title C'],
...     article_texts=['text A', 'text B', 'text C'],
...     article_sources=['Source X', 'Source Y', 'Source Z'],
...     article_count=3,
...     fetch_successful=True
>>> )
>>> output = filter_news_articles(input_data)
>>> print(output)
FilterNewsArticlesOutput(filtered_article_ids=['Title A', 'Title B', 'Title C'], removed_article_ids=[], filter_success=True)
```

```python
>>> # Sample input with a duplicate title
>>> input_data = SourceNewsArticlesOutput(
...     article_urls=['url1', 'url2', 'url3'],
...     article_titles=['Title A', 'Title B', 'Title B'],
...     article_texts=['text A', 'text B', 'text B'],
...     article_sources=['Source X', 'Source Y', 'Source Y'],
...     article_count=3,
...     fetch_successful=True
>>> )
>>> output = filter_news_articles(input_data)
>>> print(output)
FilterNewsArticlesOutput(filtered_article_ids=['Title A', 'Title B'], removed_article_ids=['Title B'], filter_success=True)
```
