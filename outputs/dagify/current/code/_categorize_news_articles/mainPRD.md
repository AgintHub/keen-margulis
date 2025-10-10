# _categorize_news_articles - Complete PRD Documentation

## Overview
PRDs for nodes in the '_categorize_news_articles' module.

## Table of Contents

- [validate_input](#validate_input)

- [normalize_article_titles](#normalize_article_titles)

- [assign_categories](#assign_categories)

- [get_unique_categories](#get_unique_categories)



---

## validate_input

### Description
Validate the list of article identifiers, ensuring each is a non-empty string and return a status message.

### Conceptual Info

This shim centralizes validation logic for article identifiers used throughout the news processing pipeline, ensuring that downstream nodes receive clean, well‑formed input.

### Docstring

**Summary:** Validate the list of article identifiers, ensuring that each element is a non-empty string and return a status message.

**Parameters:**

- filtered_article_ids (List[str]): A list of article identifiers (IDs or titles) that must be validated.
**Returns:** str - A confirmation string indicating that validation succeeded.

**Raises:**

- TypeError: Raised when `filtered_article_ids` is not a list.
- ValueError: Raised when the list is empty, contains non-string elements, or any string element is empty.
**Examples:**

```python
>>> validate_input(['id1', 'id2', 'id3'])
'Validation succeeded.'
```

```python
>>> try:
...     validate_input(['id1', '', 'id3'])
>>> except ValueError as e:
...     print(e)
'Article ID at index 1 is empty or not a string.'
```



---

## normalize_article_titles

### Description
Normalizes a list of article identifiers or titles to a canonical string format suitable for downstream processing.

### Conceptual Info

The `normalize_article_titles` shim is responsible for converting raw article identifiers or titles into a uniform format. This ensures consistency for later filtering, categorization, and duplicate detection steps.

### Docstring

**Summary:** Normalizes article titles to a canonical string format suitable for downstream processing.

**Parameters:**

- article_ids (List[str]): A list of article identifiers or raw titles that need to be normalized.
**Returns:** List[str] - A list of cleaned titles with consistent casing, whitespace trimmed, and non‑essential characters removed.

**Raises:**

- ValueError: Raised when `article_ids` is empty or contains no valid strings.
- TypeError: Raised when `article_ids` is not a list or contains non‑string elements.
**Examples:**

```python
>>> normalized = normalize_article_titles([" Breaking News: New COVID Case ", "UPDATE 2024-01-01", "12345"])
["Breaking News: New COVID Case", "UPDATE 2024-01-01", "12345"]
```

```python
>>> normalize_article_titles(["  sports:  Olympics 2024  "])
["Sports: Olympics 2024"]
```



---

## assign_categories

### Description
Assigns a category label to each article title based on its content.

### Conceptual Info

This shim determines the appropriate category for each news article title, enabling downstream processes to handle categorized articles.

### Docstring

**Summary:** Assign a category label to each article title.

**Parameters:**

- article_titles (List[str]): A list of article titles to be categorized.
**Returns:** List[str] - A list of category labels, one for each input title; indices correspond to input order.

**Raises:**

- ValueError: Raised when the input list is empty.
- TypeError: Raised when the input is not a list or contains non-string elements.
**Examples:**

```python
>>> categories = assign_categories(['Election 2024: The final debate', 'Sports: Local team wins championship'])
>>> print(categories)
['Politics', 'Sports']
```

```python
>>> assign_categories([])
ValueError: Input list cannot be empty.
```



---

## get_unique_categories

### Description
Returns a list of unique category labels from the input list, preserving the order of first occurrence.

### Conceptual Info

This shim extracts the distinct category labels from a list while maintaining the order in which they first appear, enabling downstream processing to work with a minimal set of categories.

### Docstring

**Summary:** Return a list of unique categories from the provided list, preserving the original order of first appearance.

**Parameters:**

- categories (List[str]): A list of category labels, each a string. The function expects a non-empty list containing only strings.
**Returns:** List[str] - A list containing each distinct category from `categories` exactly once, ordered by the first time it appeared in the input list.

**Raises:**

- TypeError: Raised if `categories` is not a list or if any element is not a string.
- ValueError: Raised if `categories` is an empty list.
**Examples:**

```python
>>> unique = get_unique_categories(['sports', 'politics', 'sports', 'tech'])
['sports', 'politics', 'tech']
```

```python
>>> unique = get_unique_categories([])
ValueError: Input list cannot be empty.
```

