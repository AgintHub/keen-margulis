# _source_news_articles - Complete PRD Documentation

## Overview
PRDs for nodes in the '_source_news_articles' module.

## Table of Contents

- [get_predefined_news_sources](#get_predefined_news_sources)

- [fetch_articles_from_source](#fetch_articles_from_source)

- [extract_urls](#extract_urls)

- [extract_titles](#extract_titles)

- [extract_texts](#extract_texts)

- [extract_source_names](#extract_source_names)

- [handle_fetch_error](#handle_fetch_error)

- [validate_collected_data](#validate_collected_data)



---

## get_predefined_news_sources

### Description
Retrieves a predefined list of news source identifiers to be used for article fetching.

### Conceptual Info

The get_predefined_news_sources shim supplies a static set of news source identifiers that downstream nodes use to fetch articles from those sources.

### Docstring

**Summary:** Return a list of predefined news source identifiers for article collection.

**Returns:** List[str] - A list of string identifiers for news sources such as 'AP News', 'Reuters', 'BBC News'.

**Raises:**

- ValueError: If the internal source configuration is empty or malformed.
**Examples:**

```python
>>> sources = get_predefined_news_sources()
['AP News', 'Reuters', 'BBC News']
```

```python
>>> len(get_predefined_news_sources())
3
```



---

## fetch_articles_from_source

### Description
Retrieves news article data for a specified source and returns it as a JSON-formatted string.

### Conceptual Info

This shim abstracts the logic for fetching and aggregating article metadata from a given news source. It isolates external API interactions and data extraction, providing a consistent JSON interface for downstream processing.

### Docstring

**Summary:** Fetches news articles from a specified source and returns article metadata as a JSON string.

**Parameters:**

- source (str): Identifier of the news source to query (e.g., 'NYTimes', 'BBC'). Must be a non-empty string.
**Returns:** str - JSON-formatted string containing a dictionary with keys: 'urls', 'titles', 'texts', and 'sources', each mapping to a list of strings.

**Raises:**

- ValueError: Raised when the `source` argument is an empty string or represents an unsupported news source.
- TypeError: Raised when the `source` argument is not of type `str`.
**Examples:**

```python
>>> result = fetch_articles_from_source('NYTimes')
"{\"urls\": [\"https://nytimes.com/article1\"], \"titles\": [\"Breaking News\"], \"texts\": [\"Full article text...\"], \"sources\": [\"NYTimes\"]}"
```

```python
>>> try:
...     fetch_articles_from_source('')
>>> except ValueError as e:
...     print(e)
"Source identifier must be a non-empty string."
```



---

## extract_urls

### Description
Extracts and returns a list of URLs found in the provided article data.

### Conceptual Info

The shim parses raw article data and isolates URLs for downstream processing.

### Docstring

**Summary:** Parses the input article data string to extract all URLs and returns them as a list of strings.

**Parameters:**

- data (str): A JSON-formatted string representation of article data containing URLs.
**Returns:** List[str] - A list of URL strings extracted from the input data.

**Raises:**

- ValueError: Raised when the input data does not contain any URLs.
- TypeError: Raised when the input data is not a string.
**Examples:**

```python
>>> urls = extract_urls(data='{"content": "Check https://example.com and http://test.com"}')
['https://example.com', 'http://test.com']
```

```python
>>> urls = extract_urls(data='{}')
[]
```



---

## extract_titles

### Description
Extracts a list of article titles from a string containing article data.

### Conceptual Info

In the news‑article aggregation pipeline, this shim is responsible for isolating headline titles from raw article data so that downstream components can collect, validate, and store titles efficiently.

### Docstring

**Summary:** Extracts headline titles from a raw string of article data.

**Parameters:**

- data (str): A string representation of one or more articles. Each article should contain a line starting with 'Title: ' followed by the headline text.
**Returns:** list[str] - A list of the extracted titles in the same order they appear in the input.

**Raises:**

- ValueError: If the input string is empty or contains no titles.
- TypeError: If the input parameter is not of type `str`.
**Examples:**

```python
>>> titles = extract_titles("Title: First News\nBody: ...\nTitle: Second News\nBody: ...")
>>> print(titles)
['First News', 'Second News']
```

```python
>>> extract_titles(123)
>>> extract_titles('')
TypeError: data must be a string
ValueError: input string contains no titles
```



---

## extract_texts

### Description
Parses raw article data and returns the article body as a list of text segments.

### Conceptual Info

extract_texts is a shim that takes raw article data as a string and extracts the main textual content, returning it as a list of paragraphs or text segments for downstream processing.

### Docstring

**Summary:** Extracts article text segments from raw data.

**Parameters:**

- data (str): Raw article data string containing title, headings, paragraphs, etc.
**Returns:** list - A list of strings, each representing a paragraph or text segment extracted from the article.

**Raises:**

- ValueError: Raised when the input string does not contain any extractable text.
- TypeError: Raised when the input is not of type str.
**Examples:**

```python
>>> result = extract_texts('Title\n\nParagraph one.\n\nParagraph two.')
>>> print(result)
['Paragraph one.', 'Paragraph two.']
```

```python
>>> print(extract_texts(''))
[]
```



---

## extract_source_names

### Description
Extracts a list of source names from the provided article data string for a given source identifier.

### Conceptual Info

The shim serves as a lightweight extraction layer that parses raw article data (typically JSON or similar) and retrieves the source names for each article, allowing downstream processing to identify and label news items.

### Docstring

**Summary:** Extract source names from article data for a specified source identifier.

**Parameters:**

- data (str): Raw article data in JSON-like string format containing one or more articles with a 'source' field.
- source (str): The identifier of the source from which the articles were fetched, used to filter or contextualize extracted names.
**Returns:** List[str] - A list of source names corresponding to each article present in the provided data.

**Raises:**

- ValueError: Raised when the data string is empty or does not contain the expected 'articles' structure.
- TypeError: Raised when either 'data' or 'source' is not of type 'str'.
**Examples:**

```python
>>> article_data = '{"articles":[{"title":"A","source":"News A"},{"title":"B","source":"News B"}]}'
>>> extract_source_names(article_data, "News A")
["News A", "News B"]
```

```python
>>> article_data = ''
>>> extract_source_names(article_data, "News A")
ValueError: Article data is empty or malformed.
```



---

## handle_fetch_error

### Description
Handles errors during article fetching and returns a standardized error message.

### Conceptual Info

This shim provides a consistent way to handle and report failures that occur while attempting to fetch news articles from various sources, ensuring that downstream processes receive a clear, structured error description.

### Docstring

**Summary:** Creates a standardized error message for failed article fetch attempts.

**Parameters:**

- error (Exception): The exception raised during the fetch operation.
- source (str): The name of the news source from which the fetch failed.
**Returns:** str - A user‑friendly string summarizing the error and the source.

**Raises:**

- ValueError: If `source` is not a non‑empty string.
- TypeError: If `error` is not an exception instance.
**Examples:**

```python
>>> error = ValueError('Network unreachable')
>>> msg = handle_fetch_error(error=error, source='BBC')
>>> print(msg)
'Failed to fetch from BBC: Network unreachable'
```

```python
>>> error = Exception('Timeout')
>>> msg = handle_fetch_error(error=error, source='Reuters')
>>> print(msg)
'Failed to fetch from Reuters: Timeout'
```



---

## validate_collected_data

### Description
Validates and normalizes collected article data before downstream processing.

### Conceptual Info

Ensures consistency and integrity of article metadata gathered from multiple news sources, preparing it for model ingestion.

### Docstring

**Summary:** Validate the structure and contents of article collections, ensuring all lists are non-empty, of identical length, and contain only string elements.

**Parameters:**

- urls (List[str]): A list of article URLs collected from various news sources.
- titles (List[str]): A list of article titles corresponding to the URLs.
- texts (List[str]): A list of full article texts.
- sources (List[str]): A list of source names from which each article was retrieved.
**Returns:** dict - A dictionary with keys 'urls', 'titles', 'texts', and 'sources' mapping to cleaned lists of strings. The dictionary is returned as a JSON-encoded string.

**Raises:**

- TypeError: Raised when any argument is not a list or contains non-string elements.
- ValueError: Raised when the input lists are empty or do not share the same length.
**Examples:**

```python
>>> validated = validate_collected_data(

...     urls=['https://a.com', 'https://b.com'],

...     titles=['Title A', 'Title B'],

...     texts=['Text A', 'Text B'],

...     sources=['Source A', 'Source B']

>>> )
>>> print(validated)
{'urls': ['https://a.com', 'https://b.com'], 'titles': ['Title A', 'Title B'], 'texts': ['Text A', 'Text B'], 'sources': ['Source A', 'Source B']}
```

```python
>>> try:
...     validate_collected_data(urls=['https://a.com'], titles=['Title A'], texts=['Text A'], sources=['Source A', 'Source B'])
>>> except ValueError as e:
...     print(e)
Input lists must all be of the same non-zero length.
```

