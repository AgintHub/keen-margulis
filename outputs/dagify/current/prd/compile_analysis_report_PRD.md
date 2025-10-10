# compile_analysis_report PRD

## Description
Compile the sentiment and trend data produced by the preceding analysis nodes into a single, coherent textual report and concise summaries.


## Conceptual Info

This node aggregates sentiment scores and trend findings from previous analysis steps to produce a unified report that can be consumed by end‑users or downstream systems.

## Docstring

### Summary
Generate a comprehensive analysis report from sentiment and trend data.

### Parameters

- **sentiment_category** (List[str]): Sentiment label for each article ('positive', 'negative', 'neutral').
- **sentiment_confidence** (List[float]): Confidence score (0.0–1.0) for each article's sentiment.
- **trending_topics** (List[str]): List of topics that exhibit a trend across the articles.
- **sentiment_trends** (List[str]): Sentiment trend description for each corresponding trending topic.
- **overall_trend_summary** (str): Concise textual summary of the overall trend patterns identified.

### Returns

Dict[str, Any]: Dictionary containing the full report text, sentiment and trend summaries, per‑article sentiment list, trend topics list, article count, and validity flag.

### Raises

- ValueError: If the lengths of `sentiment_category` and `sentiment_confidence` do not match, or if `trending_topics` and `sentiment_trends` differ in length.
- TypeError: If any input parameter is of an unexpected type.

### Examples

```python
>>> sentiment_category = ['positive', 'neutral', 'negative'],
>>> sentiment_confidence = [0.92, 0.85, 0.78],
>>> trending_topics = ['Climate Action', 'Tech Innovation'],
>>> sentiment_trends = ['decreasing positive', 'increasing positive'],
>>> overall_trend_summary = 'The overall sentiment is shifting from positive to more neutral, with rising excitement around tech.'
>>> report = compile_analysis_report(sentiment_category, sentiment_confidence, trending_topics, sentiment_trends, overall_trend_summary)
{
  'report_text': 'Analysis Report:\n\nSentiment:\n- Positive: 1\n- Neutral: 1\n- Negative: 1\n\nTrends:\n- Climate Action: decreasing positive\n- Tech Innovation: increasing positive\n\nOverall Trend: The overall sentiment is shifting from positive to more neutral, with rising excitement around tech.',
  'sentiment_summary': '1 positive, 1 neutral, 1 negative',
  'trend_summary': 'Climate Action shows decreasing positivity while Tech Innovation is gaining traction.',
  'sentiment_per_article': ['positive', 'neutral', 'negative'],
  'trend_topics': ['Climate Action', 'Tech Innovation'],
  'article_count': 3,
  'is_valid': True
}
```
