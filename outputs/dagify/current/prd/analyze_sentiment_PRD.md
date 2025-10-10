# analyze_sentiment PRD

## Description
Analyzes the sentiment of concise news article summaries, returning an ordered list of article indices, sentiment categories, and confidence scores for each article.


## Conceptual Info

The node takes concise article summaries and determines the overall sentiment of each article, returning a list of indices, sentiment categories, and confidence scores.

## Docstring

### Summary
Analyze the sentiment of news article summaries.

### Parameters

- **summarize_news_articles_input** (SummarizeNewsArticlesOutput): Output of the summarize_news_articles node containing a list of article summaries.

### Returns

AnalyzeSentimentOutput: An object containing article indices, sentiment categories, and confidence scores.

### Raises

- ValueError: Raised if the summary list is empty.
- TypeError: Raised if any summary entry is not a string or if the input is not a SummarizeNewsArticlesOutput instance.
- RuntimeError: Raised when internal sentiment analysis returns mismatched lengths.

### Examples

```python
>>> result = analyze_sentiment(SummarizeNewsArticlesOutput(summary_count=2, summaries=["A positive event occurred", "A negative event occurred"]))
>>> print(result)
AnalyzeSentimentOutput(article_index=[0, 1], sentiment_category=['positive', 'negative'], sentiment_confidence=[0.92, 0.85])
```
