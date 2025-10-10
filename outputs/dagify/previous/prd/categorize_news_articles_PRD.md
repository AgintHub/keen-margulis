# categorize_news_articles PRD

## Description
Assigns topical categories to a list of filtered news article titles, normalizes the headlines, and provides statistics on the resulting categories for downstream analysis.


## Conceptual Info

The node transforms a cleaned list of news headlines into topic‑labelled records, enabling downstream analytics such as sentiment, trend or clustering analysis. It normalizes headline text, applies a lightweight NLP classifier, and returns cardinality metrics for reporting.

## Docstring

### Summary
Categorizes news article titles by topic.

### Parameters

- **filter_news_articles_input** (FilterNewsArticlesOutput): Output from the filtering step containing the list of article titles to be categorized.

### Returns

CategorizeNewsArticlesOutput: Structured output containing categorized titles, category list, and statistics.

### Raises

- ValueError: Raised when `filtered_article_ids` is empty or not a list of strings.
- RuntimeError: Raised when the prior filtering step failed or an internal error occurs during categorization.

### Examples

```python
>>> filtered = FilterNewsArticlesOutput(**{
...     'filtered_article_ids': ['Economic growth forecast', 'Parliament passes new law', 'Local community event'],
...     'removed_article_ids': [],
...     'filter_success': True
>>> })
>>> result = categorize_news_articles(filtered)
>>> print(result)
CategorizeNewsArticlesOutput(article_titles=['Economic growth forecast', 'Parliament passes new law', 'Local community event'], categories=['Economics', 'Politics', 'Social Issues'], unique_category_count=3, article_count=3, is_successful=True)
```
