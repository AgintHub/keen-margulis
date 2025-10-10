# filter_news_articles PRD

## Description
Filter out irrelevant or redundant news articles.


## Conceptual Info

The filter_news_articles node cleanses a batch of fetched news articles by removing any that are irrelevant to the downstream analytical tasks or that appear more than once. It outputs a list of unique, relevant article identifiers and flags any removal, allowing downstream nodes such as categorization to operate on a refined dataset.

## Docstring

### Summary
Filter out irrelevant or duplicate news articles from a collected set.

### Parameters

- **article_titles** (List[str]): Headlines of the news articles collected by the source_news_articles node.
- **article_texts** (List[str]): Full text content of each news article.
- **article_count** (int): Total number of articles provided. Used to validate that titles and texts lists are consistent.

### Returns

Tuple[List[str], List[str], bool]: A tuple containing (filtered_article_ids, removed_article_ids, filter_success).

### Raises

- ValueError: Raised if the lengths of article_titles and article_texts do not match article_count, indicating malformed input.
- RuntimeError: Raised if an internal filtering error occurs, such as failure to compute similarity scores.

### Examples

```python
>>> filtered, removed, success = filter_news_articles(

...     article_titles=['A', 'B', 'C'],

...     article_texts=['text A', 'text B', 'text C'],

...     article_count=3

>>> )
>>> print(filtered, removed, success)
(['A', 'B', 'C'], [], True)
```

```python
>>> filtered, removed, success = filter_news_articles(

...     article_titles=['A', 'B', 'C', 'B'],

...     article_texts=['text A', 'text B', 'text C', 'text B'],

...     article_count=4

>>> )
>>> print(filtered, removed, success)
(['A', 'B', 'C'], ['B'], True)
```
