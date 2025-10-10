# summarize_news_articles PRD

## Description
Summarize the key points of the news articles.


## Conceptual Info

The `summarize_news_articles` node takes a list of article titles and their full texts and produces a brief, one‑sentence summary for each article, enabling downstream sentiment analysis and trend identification to focus on the core messages.

## Docstring

### Summary
Generate concise summaries for a collection of news articles.

### Parameters

- **article_titles** (List[str]): List of article titles corresponding to the articles to be summarized.
- **article_texts** (List[str]): Full text content of each article in the same order as `article_titles`.

### Returns

Tuple[int, List[str]]: A tuple where the first element is the number of summaries generated and the second element is a list of summary strings ordered to match the input articles.

### Raises

- ValueError: If either `article_titles` or `article_texts` is empty, or if the two lists have different lengths.
- TypeError: If the inputs are not of the expected list-of-strings types.

### Examples

```python
>>> summaries = summarize_news_articles(
...     article_titles=["Economy grows 3%", "Championship ends in tie‑breaker"],
...     article_texts=[
...         "The economy grew by 3% last quarter, driven largely by consumer spending and investment in technology sectors.",
...         "In an unexpected turn, the championship final concluded with a dramatic tie‑breaker, sending the crowd into a frenzy."
>>> ]
>>> )
(2, ['Economy grew 3% driven by consumer spending and tech investment.', 'Championship final ended with a dramatic tie‑breaker.'])
```

```python
>>> summaries = summarize_news_articles(article_titles=[], article_texts=[])
ValueError: No articles provided.
```
