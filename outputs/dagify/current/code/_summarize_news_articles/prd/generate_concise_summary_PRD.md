# generate_concise_summary PRD

## Description
Generates a concise summary of a news article given its title and processed text


## Conceptual Info

This shim serves as the core summarization component in the news aggregation pipeline, converting raw article text into digestible summaries for downstream consumers such as dashboards and search indexes.

## Docstring

### Summary
Generate a concise summary of a news article given its title and processed text.

### Parameters

- **title** (str): Title of the news article. Must be a non-empty string.
- **text** (str): Fully processed article text (e.g., after cleaning, tokenization, and normalization). Must be a non-empty string.

### Returns

str: A short paragraph summarizing the main facts of the article. The summary should be no longer than 3–4 sentences and retain the key entities and events.

### Raises

- ValueError: Raised when either `title` or `text` is an empty string.
- TypeError: Raised when either `title` or `text` is not of type `str`.

### Examples

```python
>>> summary = generate_concise_summary(

...     title='WHO Approves Three COVID-19 Vaccines',

...     text=('The World Health Organization has approved three COVID-19 vaccines after a thorough review of their safety and efficacy data. The vaccines, developed by Pfizer, Moderna, and AstraZeneca, are expected to be distributed globally starting next month. The approval aims to accelerate vaccination efforts amid the ongoing pandemic.')

>>> )
"WHO approves three COVID‑19 vaccines, aiming for global distribution next month after thorough safety reviews."
```

```python
>>> summary = generate_concise_summary(

...     title='Tech Giants Announce New AI Initiative',

...     text=('In a joint statement, leading technology companies unveiled a collaborative AI research initiative. The goal is to develop ethical AI frameworks and share open-source tools. They plan to release initial findings by Q3.')

>>> )
"Tech giants launch collaborative AI initiative to develop ethical frameworks and release open-source tools by Q3."
```
