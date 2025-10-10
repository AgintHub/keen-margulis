# _compile_analysis_report - Complete PRD Documentation

## Overview
PRDs for nodes in the '_compile_analysis_report' module.

## Table of Contents

- [validate_input_parameters](#validate_input_parameters)

- [count_sentiment_categories](#count_sentiment_categories)

- [generate_sentiment_summary](#generate_sentiment_summary)

- [generate_trend_summary](#generate_trend_summary)

- [generate_full_report](#generate_full_report)

- [validate_report_completion](#validate_report_completion)



---

## validate_input_parameters

### Description
Validate the input parameters for sentiment analysis and trend identification, ensuring required fields are present and correctly typed.

### Conceptual Info

This shim function acts as a gatekeeper in the analysis pipeline, ensuring that the sentiment and trend data objects received from upstream nodes adhere to expected schemas before further processing.

### Docstring

**Summary:** Validate that sentiment and trend input data contain required fields with correct types and return a success message.

**Parameters:**

- sentiment_data (str): JSON string representation of an AnalyzeSentimentOutput object, containing article indices, sentiment categories, and confidence scores.
- trends_data (str): JSON string representation of an IdentifyTrendsOutput object, containing trending topics, sentiment trends, and an overall trend summary.
**Returns:** str - A confirmation string, e.g., 'Validation successful', indicating that the input data passed all checks.

**Raises:**

- ValueError: Raised when required fields are missing or contain invalid data.
- TypeError: Raised when the input parameters are not strings or cannot be parsed into valid JSON objects.
**Examples:**

```python
>>> output = validate_input_parameters(
...     sentiment_data='{"article_index": [1, 2], "sentiment_category": ["positive", "negative"], "sentiment_confidence": [0.95, 0.85]}',
...     trends_data='{"trending_topics": ["economy"], "sentiment_trends": ["stable neutral"], "overall_trend_summary": "stable"}'
>>> )
'Validation successful'
```

```python
>>> try:
...     validate_input_parameters(
...         sentiment_data='{"article_index": [1], "sentiment_category": ["positive"]}',
...         trends_data='{"trending_topics": ["economy"], "sentiment_trends": ["stable neutral"]}'
...     )
>>> except Exception as e:
...     print(e)
'ValueError: Missing field 'overall_trend_summary' in trends_data'
```



---

## count_sentiment_categories

### Description
Returns a JSON string mapping each sentiment category ('positive', 'negative', 'neutral') to its count from a comma‑separated input string.

### Conceptual Info

This shim aggregates sentiment counts from a list of categories supplied as a string, enabling downstream report generation modules to summarize overall sentiment distribution.

### Docstring

**Summary:** Counts occurrences of the sentiment categories 'positive', 'negative', and 'neutral' from a comma‑separated string and returns a JSON string of the resulting counts.

**Parameters:**

- sentiment_categories (str): Comma‑separated string of sentiment categories to count. Example: "positive,negative,positive".
**Returns:** str - JSON string mapping each of the categories 'positive', 'negative', and 'neutral' to an integer count.

**Raises:**

- ValueError: Raised when the input string contains an invalid sentiment category or is empty.
- TypeError: Raised when the input is not a string.
**Examples:**

```python
>>> output = count_sentiment_categories('positive,negative,positive')
'{'positive': 2, 'negative': 1, 'neutral': 0}'
```

```python
>>> output = count_sentiment_categories('neutral,neutral,positive')
'{'positive': 1, 'negative': 0, 'neutral': 2}'
```



---

## generate_sentiment_summary

### Description
Generates a concise textual summary of overall sentiment distribution based on sentiment counts.

### Conceptual Info

The generate_sentiment_summary shim produces a human-readable summary of sentiment distribution across a set of news articles, converting numerical counts into a short narrative.

### Docstring

**Summary:** Create a brief summary of overall sentiment distribution based on provided counts of positive, negative, and neutral sentiments.

**Parameters:**

- sentiment_counts (Dict[str, int]): Dictionary mapping sentiment categories ('positive', 'negative', 'neutral') to their respective article counts.
**Returns:** str - A short English sentence summarizing the sentiment distribution.

**Raises:**

- ValueError: If sentiment_counts is missing one or more of the required keys.
- TypeError: If sentiment_counts is not a dictionary or contains non-integer counts.
**Examples:**

```python
>>> sentiment_counts = {'positive': 12, 'negative': 5, 'neutral': 3}
>>> summary = generate_sentiment_summary(sentiment_counts=sentiment_counts)
>>> print(summary)
'In total, 12 articles were positive, 5 negative, and 3 neutral.'
```

```python
>>> sentiment_counts = {'positive': 7, 'negative': 7, 'neutral': 6}
>>> print(generate_sentiment_summary(sentiment_counts=sentiment_counts))
'The sentiment distribution is even: 7 positive, 7 negative, and 6 neutral articles.'
```



---

## generate_trend_summary

### Description
Generates a concise textual summary of trend patterns based on input topics and their sentiment trends.

### Conceptual Info

This shim is responsible for turning raw trend data—topics and their associated sentiment evolution—into an easily readable sentence that captures the overall trend narrative, facilitating downstream reporting.

### Docstring

**Summary:** Generate a concise trend summary from lists of trending topics and their sentiment trends.

**Parameters:**

- trending_topics (List[str]): A list of topics that show a trend across the news articles.
- sentiment_trends (List[str]): A list describing the sentiment trend for each corresponding trending topic, e.g., 'increasing positive', 'decreasing negative', or 'stable neutral'.
**Returns:** str - A single sentence that succinctly summarizes how each topic's sentiment is evolving.

**Raises:**

- ValueError: Raised when the two input lists have different lengths or are empty.
- TypeError: Raised when inputs are not lists of strings.
**Examples:**

```python
>>> summary = generate_trend_summary(['Economy', 'Tech'], ['increasing positive', 'stable neutral'])
'The Economy trend shows increasing positive sentiment, while Tech trend remains stable and neutral.'
```

```python
>>> summary = generate_trend_summary(['Healthcare'], ['decreasing negative'])
'The Healthcare trend shows decreasing negative sentiment.'
```



---

## generate_full_report

### Description
Creates a comprehensive news analysis report string by combining sentiment summary, trend summary, overall trend summary, sentiment counts, trending topics, and sentiment trends.

### Conceptual Info

The generate_full_report shim is responsible for synthesizing all sentiment and trend information into a single, human‑readable report that can be consumed by downstream reporting modules.

### Docstring

**Summary:** Generates a formatted news analysis report from sentiment and trend inputs.

**Parameters:**

- sentiment_summary (str): Brief summary of overall sentiment distribution (positive/negative/neutral).
- trend_summary (str): Brief summary of key trends identified across articles.
- overall_trend_summary (str): Concise textual summary of the overall trend patterns identified.
- sentiment_counts (str): Stringified representation of sentiment counts per category.
- trending_topics (str): Comma‑separated list of topics that show a trend across the news articles.
- sentiment_trends (str): Sentiment trend descriptors for each corresponding trending topic.
**Returns:** str - A single string containing the fully formatted analysis report.

**Raises:**

- ValueError: Raised if any required input string is empty or None.
- TypeError: Raised if any input is not of type str.
**Examples:**

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



---

## validate_report_completion

### Description
Checks that the generated report contains content and matches the expected article count.

### Conceptual Info

The validation shim ensures that a textual report produced by the pipeline is non-empty, has sufficient length, and reflects the correct number of articles, providing a quick sanity check before downstream usage.

### Docstring

**Summary:** Validate that a report string is non-empty and contains at least the specified number of article summaries.

**Parameters:**

- report_text (str): Full textual report to be validated.
- article_count (int): Expected number of articles included in the report.
**Returns:** bool - True if the report meets all validation criteria; otherwise False.

**Raises:**

- ValueError: Raised when article_count is negative or zero.
- TypeError: Raised when report_text is not a string or article_count is not an integer.
**Examples:**

```python
>>> valid = validate_report_completion('Summary 1\nSummary 2', 2)
True
```

```python
>>> validate_report_completion('', 1)
False
```

