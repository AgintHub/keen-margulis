# compile_analysis_report PRD

## Description
Generates a comprehensive and validated textual analysis report by integrating sentiment scores and trend data. Ensures robust validation, clear summaries, and structured output for downstream consumption.


## Conceptual Info

This node aggregates sentiment analysis and trend detection results into a detailed report for downstream applications.

## Docstring

### Summary
Generates a summarized analysis report from sentiment and trend data.

### Parameters

- **analyze_sentiment_input** (AnalyzeSentimentOutput): Output of the analyze_sentiment node, including sentiment categories and confidence scores.
- **identify_trends_input** (IdentifyTrendsOutput): Output of the identify_trends node, including trending topics and sentiment trends.

### Returns

CompileAnalysisReportOutput: Structured output containing the completed analysis report, summaries, and validation status.

### Raises

- ValueError: Raised if input validation fails or if inconsistencies are found in the inputs.
- TypeError: Raised if input parameters are of unexpected types.

### Examples

```python
>>> analyze_output = AnalyzeSentimentOutput(
...     article_index=[0, 1],
...     sentiment_category=['positive', 'neutral'],
...     sentiment_confidence=[0.95, 0.78]
>>> )
>>> trends_output = IdentifyTrendsOutput(
...     trending_topics=['AI', 'Climate Change'],
...     sentiment_trends=['increasing positive', 'stable neutral'],
...     overall_trend_summary='AI topics are gaining positivity while climate sentiment remains neutral.'
>>> )
>>> result = compile_analysis_report(
...     analyze_sentiment_input=analyze_output,
...     identify_trends_input=trends_output
>>> )
>>> print(result.report_text)
Full analysis report combining sentiment and trend insights.
```
