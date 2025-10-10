# generate_full_report PRD

## Description
Creates a comprehensive news analysis report string by combining sentiment summary, trend summary, overall trend summary, sentiment counts, trending topics, and sentiment trends.


## Conceptual Info

The generate_full_report shim is responsible for synthesizing all sentiment and trend information into a single, human‑readable report that can be consumed by downstream reporting modules.

## Docstring

### Summary
Generates a formatted news analysis report from sentiment and trend inputs.

### Parameters

- **sentiment_summary** (str): Brief summary of overall sentiment distribution (positive/negative/neutral).
- **trend_summary** (str): Brief summary of key trends identified across articles.
- **overall_trend_summary** (str): Concise textual summary of the overall trend patterns identified.
- **sentiment_counts** (str): Stringified representation of sentiment counts per category.
- **trending_topics** (str): Comma‑separated list of topics that show a trend across the news articles.
- **sentiment_trends** (str): Sentiment trend descriptors for each corresponding trending topic.

### Returns

str: A single string containing the fully formatted analysis report.

### Raises

- ValueError: Raised if any required input string is empty or None.
- TypeError: Raised if any input is not of type str.

### Examples

```python
>>> report = generate_full_report(
...     sentiment_summary='Positive 60%, Neutral 25%, Negative 15%',
...     trend_summary='Tech adoption increasing, Healthcare interest stable',
...     overall_trend_summary='Overall upward trend in technology sentiment.',
...     sentiment_counts='{"positive": 12, "neutral": 5, "negative": 3}',
...     trending_topics='AI, Telemedicine',
...     sentiment_trends='Increasing positive, Stable neutral'"
              ")
>>> print(report)
"Full Report:\n\nSentiment Summary: Positive 60%, Neutral 25%, Negative 15%\nTrend Summary: Tech adoption increasing, Healthcare interest stable\nOverall Trend Summary: Overall upward trend in technology sentiment.\nSentiment Counts: {\"positive\": 12, \"neutral\": 5, \"negative\": 3}\nTrending Topics: AI, Telemedicine\nSentiment Trends: Increasing positive, Stable neutral"
```

```python
>>> report = generate_full_report(
...     sentiment_summary='Neutral 70%, Positive 20%, Negative 10%',
...     trend_summary='Energy policy discussions rising',
...     overall_trend_summary='Mixed sentiment overall with a slight positive tilt.',
...     sentiment_counts='{"positive": 4, "neutral": 14, "negative": 2}',
...     trending_topics='Renewable Energy, Climate Change',
...     sentiment_trends='Stable neutral, Increasing positive'"
              ")
>>> print(report)
"Full Report:\n\nSentiment Summary: Neutral 70%, Positive 20%, Negative 10%\nTrend Summary: Energy policy discussions rising\nOverall Trend Summary: Mixed sentiment overall with a slight positive tilt.\nSentiment Counts: {\"positive\": 4, \"neutral\": 14, \"negative\": 2}\nTrending Topics: Renewable Energy, Climate Change\nSentiment Trends: Stable neutral, Increasing positive"
```
