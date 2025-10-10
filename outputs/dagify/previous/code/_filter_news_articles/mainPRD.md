# _filter_news_articles - Complete PRD Documentation

## Overview
PRDs for nodes in the '_filter_news_articles' module.

## Table of Contents

- [validate_input_consistency](#validate_input_consistency)

- [detect_duplicate_articles](#detect_duplicate_articles)

- [identify_irrelevant_articles](#identify_irrelevant_articles)

- [combine_removal_indices](#combine_removal_indices)

- [get_remaining_indices](#get_remaining_indices)

- [extract_article_ids](#extract_article_ids)



---

## validate_input_consistency

### Description
A shim that checks whether the number of article titles and texts matches the reported article count before downstream processing.

### Conceptual Info

This shim ensures that the lists of article titles and texts have the same length as the provided article count, preventing downstream errors during filtering.

### Docstring

**Summary:** Validate that the provided lists of article titles and texts are consistent with the reported article count. If validation passes, returns a confirmation message; otherwise, raises an appropriate exception.

**Parameters:**

- titles (List[str]): A list of article titles.
- texts (List[str]): A list of article full texts corresponding to the titles.
- count (int): The reported total number of articles. Must equal len(titles) and len(texts).
**Returns:** str - A confirmation string, e.g., 'Input validation passed.'

**Raises:**

- TypeError: Raised if any of titles, texts, or count are of incorrect types.
- ValueError: Raised if len(titles) != len(texts) or len(titles) != count.
**Examples:**

```python
>>> titles = ['Title 1', 'Title 2']
>>> texts = ['Text 1', 'Text 2']
>>> count = 2
>>> validate_input_consistency(titles, texts, count)
'Input validation passed.'
```

```python
>>> titles = ['Title 1', 'Title 2']
>>> texts = ['Text 1']
>>> count = 2
>>> try:
...     validate_input_consistency(titles, texts, count)
>>> except ValueError as e:
...     print(e)
'Input validation failed: titles and texts length mismatch with count.'
```



---

## detect_duplicate_articles

### Description
Detects indices of duplicate news articles based on their titles and texts.

### Conceptual Info

This shim identifies duplicate news articles by comparing their titles and full texts. It outputs the list of indices that should be removed to eliminate redundancy in downstream processing.

### Docstring

**Summary:** Return indices of duplicate articles in a list of titles and texts.

**Parameters:**

- titles (List[str]): A list of article titles.
- texts (List[str]): A list of article full texts.
**Returns:** List[int] - A list of integer indices (0‑based) that correspond to articles identified as duplicates.

**Raises:**

- ValueError: If the lengths of `titles` and `texts` do not match.
- TypeError: If `titles` or `texts` is not a list of strings.
**Examples:**

```python
>>> titles = ["Breaking News", "Daily Update", "Breaking News", "Sports Highlights"],
>>> texts  = ["Content A", "Content B", "Content A", "Content C"],
>>> detect_duplicate_articles(titles, texts)
[2]
```

```python
>>> titles = ["News A", "News B", "News C"],
>>> texts  = ["Text A", "Text B", "Text C"],
>>> detect_duplicate_articles(titles, texts)
[]
```



---

## identify_irrelevant_articles

### Description
Identifies indices of news articles considered irrelevant based on content analysis.

### Conceptual Info

The shim abstracts the logic to determine which news articles lack sufficient relevance, enabling downstream filtering steps to remove them.

### Docstring

**Summary:** Returns the zero-based indices of news articles deemed irrelevant.

**Parameters:**

- titles (List[str]): List of article titles.
- texts (List[str]): List of full article texts.
**Returns:** List[int] - Zero-based indices of articles identified as irrelevant.

**Raises:**

- ValueError: If the number of titles and texts differ or if any list is empty.
- TypeError: If titles or texts are not lists of strings.
**Examples:**

```python
>>> titles = ['Short News', 'Detailed Report']
>>> texts = ['Hi', 'This is a comprehensive analysis of the recent event.']
>>> indices = identify_irrelevant_articles(titles, texts)
>>> print(indices)
[0]
```

```python
>>> titles = ['Empty', 'Irrelevant']
>>> texts = ['', '!!!']
>>> indices = identify_irrelevant_articles(titles, texts)
>>> print(indices)
[0, 1]
```



---

## combine_removal_indices

### Description
Combines two lists of article indices—duplicates and irrelevant—into a single sorted list of unique indices for removal.

### Conceptual Info

In the filtering pipeline, articles identified as duplicate or irrelevant must be removed. This shim merges their indices into a single, de‑duplicated, sorted list to be used by downstream components.

### Docstring

**Summary:** Combines duplicate and irrelevant article index lists into a sorted list of unique indices.

**Parameters:**

- duplicates (List[int]): List of integer indices representing articles identified as duplicates.
- irrelevant (List[int]): List of integer indices representing articles identified as irrelevant.
**Returns:** List[int] - A sorted list containing every index from both input lists, with duplicates removed.

**Raises:**

- ValueError: Raised if any element in either input list is not a non‑negative integer.
- TypeError: Raised if either input is not a list.
**Examples:**

```python
>>> duplicates = [1, 3, 5]
>>> irrelevant = [3, 4, 6]
>>> combine_removal_indices(duplicates, irrelevant)
[1, 3, 4, 5, 6]
```

```python
>>> duplicates = []
>>> irrelevant = [2, 7]
>>> combine_removal_indices(duplicates, irrelevant)
[2, 7]
```



---

## get_remaining_indices

### Description
Computes the list of remaining article indices after removing specified indices from a total set.

### Conceptual Info

This shim determines which articles remain after filtering out those identified as duplicates or irrelevant.

### Docstring

**Summary:** Return the list of remaining indices given the total count and a list of removed indices.

**Parameters:**

- total_count (int): The total number of articles originally retrieved.
- removed_indices (List[int]): Indices of articles that have been removed (e.g., duplicates or irrelevant).
**Returns:** List[int] - A sorted list of indices that were not removed.

**Raises:**

- TypeError: If total_count is not an int or removed_indices is not a list of ints.
- ValueError: If any removed index is outside the range [0, total_count-1] or if total_count is negative.
**Examples:**

```python
>>> get_remaining_indices(total_count=5, removed_indices=[0, 2])
[1, 3, 4]
```

```python
>>> get_remaining_indices(total_count=3, removed_indices=[0, 1, 2])
[]
```



---

## extract_article_ids

### Description
Selects article titles from a list based on provided indices and returns them.

### Conceptual Info

This shim extracts the subset of article titles corresponding to given indices, facilitating downstream filtering and reporting steps in a news aggregation workflow.

### Docstring

**Summary:** Return the titles of articles at the supplied indices.

**Parameters:**

- titles (List[str]): A list of article titles in the original order.
- indices (List[int]): A list of integer indices specifying which titles to extract.
**Returns:** List[str] - A list of titles at the requested indices, preserving the order of indices.

**Raises:**

- ValueError: Raised when an index is out of bounds for the titles list.
- TypeError: Raised when titles is not a list of strings or indices is not a list of integers.
**Examples:**

```python
>>> titles = ['Alpha', 'Beta', 'Gamma', 'Delta']
>>> indices = [0, 2, 3]
>>> result = extract_article_ids(titles, indices)
>>> print(result)
['Alpha', 'Gamma', 'Delta']
```

```python
>>> titles = ['One', 'Two', 'Three']
>>> indices = []
>>> result = extract_article_ids(titles, indices)
>>> print(result)
[]
```

