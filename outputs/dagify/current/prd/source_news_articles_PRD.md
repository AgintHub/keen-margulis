# source_news_articles PRD

## Description
Gather news articles from various sources.


## Conceptual Info

The `source_news_articles` node fetches a curated set of news articles from multiple online sources, ensuring coverage of a broad spectrum of topics and viewpoints. It outputs the raw data needed for downstream filtering, categorization, summarization, sentiment analysis, and trend identification.

## Docstring

### Summary
Collects news articles from a predefined list of sources, returning metadata and content for each article.

### Returns

dict: A dictionary containing the following keys:
- `article_urls`: List[str]
- `article_titles`: List[str]
- `article_texts`: List[str]
- `article_sources`: List[str]
- `article_count`: int
- `fetch_successful`: bool

### Raises

- ConnectionError: Raised when the network connection to a news source fails.
- ValueError: Raised if the fetched data is empty or cannot be parsed.

### Examples

```python
>>> result = source_news_articles()
>>> print(result['article_count'])
5
```

```python
>>> result = source_news_articles()
>>> print(result['article_urls'])
['https://example.com/article1', 'https://example.org/news/2', 'https://news.com/story3']
```
