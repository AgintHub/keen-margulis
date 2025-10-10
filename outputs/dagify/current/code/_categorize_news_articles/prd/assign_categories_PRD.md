# assign_categories PRD

## Description
Assigns a category label to each article title based on its content.


## Conceptual Info

This shim determines the appropriate category for each news article title, enabling downstream processes to handle categorized articles.

## Docstring

### Summary
Assign a category label to each article title.

### Parameters

- **article_titles** (List[str]): A list of article titles to be categorized.

### Returns

List[str]: A list of category labels, one for each input title; indices correspond to input order.

### Raises

- ValueError: Raised when the input list is empty.
- TypeError: Raised when the input is not a list or contains non-string elements.

### Examples

```python
>>> categories = assign_categories(['Election 2024: The final debate', 'Sports: Local team wins championship'])
>>> print(categories)
['Politics', 'Sports']
```

```python
>>> assign_categories([])
ValueError: Input list cannot be empty.
```
