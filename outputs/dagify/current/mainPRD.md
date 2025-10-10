# news_analysis_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'news_analysis_workflow' module.

## Table of Contents

- [analyze_sentiment](#analyze_sentiment)

- [categorize_news_articles](#categorize_news_articles)

- [compile_analysis_report](#compile_analysis_report)

- [filter_news_articles](#filter_news_articles)

- [identify_trends](#identify_trends)

- [source_news_articles](#source_news_articles)

- [summarize_news_articles](#summarize_news_articles)



---

## analyze_sentiment

### Description
Analyzes the sentiment of concise news article summaries, returning an ordered list of article indices, sentiment categories, and confidence scores for each article.

### Conceptual Info

The node takes concise article summaries and determines the overall sentiment of each article, returning a list of indices, sentiment categories, and confidence scores.

### Docstring

**Summary:** Analyze the sentiment of news article summaries.

**Parameters:**

- summarize_news_articles_input (SummarizeNewsArticlesOutput): Output of the summarize_news_articles node containing a list of article summaries.
**Returns:** AnalyzeSentimentOutput - An object containing article indices, sentiment categories, and confidence scores.

**Raises:**

- ValueError: Raised if the summary list is empty.
- TypeError: Raised if any summary entry is not a string or if the input is not a SummarizeNewsArticlesOutput instance.
- RuntimeError: Raised when internal sentiment analysis returns mismatched lengths.
**Examples:**

```python
>>> result = analyze_sentiment(SummarizeNewsArticlesOutput(summary_count=2, summaries=["A positive event occurred", "A negative event occurred"]))
>>> print(result)
AnalyzeSentimentOutput(article_index=[0, 1], sentiment_category=['positive', 'negative'], sentiment_confidence=[0.92, 0.85])
```



---

## categorize_news_articles

### Description
Assigns topical categories to a list of filtered news article titles, normalizes the headlines, and provides statistics on the resulting categories for downstream analysis.

### Conceptual Info

The node transforms a cleaned list of news headlines into topic‑labelled records, enabling downstream analytics such as sentiment, trend or clustering analysis. It normalizes headline text, applies a lightweight NLP classifier, and returns cardinality metrics for reporting.

### Docstring

**Summary:** Categorizes news article titles by topic.

**Parameters:**

- filter_news_articles_input (FilterNewsArticlesOutput): Output from the filtering step containing the list of article titles to be categorized.
**Returns:** CategorizeNewsArticlesOutput - Structured output containing categorized titles, category list, and statistics.

**Raises:**

- ValueError: Raised when `filtered_article_ids` is empty or not a list of strings.
- RuntimeError: Raised when the prior filtering step failed or an internal error occurs during categorization.
**Examples:**

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



---

## compile_analysis_report

### Description
Generates a comprehensive and validated textual analysis report by integrating sentiment scores and trend data. Ensures robust validation, clear summaries, and structured output for downstream consumption.

### Conceptual Info

This node aggregates sentiment analysis and trend detection results into a detailed report for downstream applications.

### Docstring

**Summary:** Generates a summarized analysis report from sentiment and trend data.

**Parameters:**

- analyze_sentiment_input (AnalyzeSentimentOutput): Output of the analyze_sentiment node, including sentiment categories and confidence scores.
- identify_trends_input (IdentifyTrendsOutput): Output of the identify_trends node, including trending topics and sentiment trends.
**Returns:** CompileAnalysisReportOutput - Structured output containing the completed analysis report, summaries, and validation status.

**Raises:**

- ValueError: Raised if input validation fails or if inconsistencies are found in the inputs.
- TypeError: Raised if input parameters are of unexpected types.
**Examples:**

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



---

## filter_news_articles

### Description
Enhances the original filtering logic by adding comprehensive input validation, detailed logging, and fallback handling to ensure reliability in downstream analyses.

### Conceptual Info

The filter_news_articles node cleanses a batch of fetched news articles by removing any that are irrelevant to the downstream analytical tasks or that appear more than once. It outputs a list of unique, relevant article identifiers and flags any removal, allowing downstream nodes such as categorization to operate on a refined dataset.

### Docstring

**Summary:** Filter news articles to remove irrelevant or duplicate entries.

**Parameters:**

- source_news_articles_input (SourceNewsArticlesOutput): Validated output from the source_news_articles node.
**Returns:** FilterNewsArticlesOutput - Output containing filtered and removed article ids, and a success flag.

**Raises:**

- ValueError: Raised when input validation fails.
- RuntimeError: Raised when internal filtering logic encounters an unexpected error.
**Examples:**

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



---

## identify_trends

### Description
Analyzes a list of article summaries to surface recurring topics and the evolution of their sentiment, producing a structured output that can be used by downstream analytics or reporting components.

### Conceptual Info

Analyzes a collection of news article summaries to surface recurring themes and their sentiment dynamics.

### Docstring

**Summary:** Identifies trending topics and sentiment trajectories from article summaries.

**Parameters:**

- summarize_news_articles_input (SummarizeNewsArticlesOutput): Pydantic model containing the list of article summaries produced by the summarize_news_articles node.
- kwargs (dict): Optional keyword arguments for extensibility.
**Returns:** IdentifyTrendsOutput - Pydantic model with trending topics, sentiment trends, and an overall summary.

**Raises:**

- ValueError: If the summaries list is empty or contains non-string items.
- RuntimeError: If any helper function fails during processing.
**Examples:**

```python
>>> from your_module import identify_trends
--
```



---

## source_news_articles

### Description
Collects a curated set of news articles from multiple online sources, returning URLs, titles, texts, and source names for each article. The function is designed for robustness, logging, and graceful error handling, producing a Pydantic model for downstream processing.

### Conceptual Info

The source_news_articles node fetches a diversified set of news articles from a curated list of online media outlets. It normalizes the data into a consistent structure, logs key events for observability, and gracefully handles source‑specific failures while ensuring that downstream nodes receive a complete, validated payload.

### Docstring

**Summary:** Retrieve news articles from a set of predefined sources, returning structured metadata and content.

**Parameters:**

- general_input (str | None): Optional textual input that can be used to influence source selection or filtering. Currently unused but kept for compatibility.
- kwargs (dict): Additional keyword arguments forwarded to downstream helpers.
**Returns:** SourceNewsArticlesOutput - Model containing article URLs, titles, texts, source names, count, and a success flag.

**Raises:**

- ValueError: Raised when an unexpected type is passed or collected data cannot be validated.
**Examples:**

```python
>>> result = source_news_articles()
>>> print(result.article_count)
7
```



---

## summarize_news_articles

### Description
Generates a brief, one‑sentence summary for every news article provided by the categorization node, enabling downstream analysis such as sentiment scoring or trend extraction.

### Conceptual Info

Summarization transforms lengthy news content into digestible insights, providing a lightweight representation that downstream modules can process efficiently.

### Docstring

**Summary:** Generate concise one‑sentence summaries of news articles.

**Parameters:**

- categorize_news_articles_input (CategorizeNewsArticlesOutput): Output from the categorization node containing article titles and associated metadata.
**Returns:** SummarizeNewsArticlesOutput - Structured output with the count of summaries and the list of summary strings.

**Raises:**

- ValueError: Raised when no article titles are provided or when title and text counts mismatch.
- TypeError: Raised when input types are not as expected.
**Examples:**

```python
>>> output = summarize_news_articles(categorize_news_articles_input)
>>> print(output.summary_count)
>>> print(output.summaries)
2
['Economy grew 3% driven by consumer spending and tech investment.', 'Championship final ended with a dramatic tie‑breaker.']
```

