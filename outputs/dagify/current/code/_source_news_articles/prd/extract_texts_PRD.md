# extract_texts PRD

## Description
Parses raw article data and returns the article body as a list of text segments.


## Conceptual Info

extract_texts is a shim that takes raw article data as a string and extracts the main textual content, returning it as a list of paragraphs or text segments for downstream processing.

## Docstring

### Summary
Extracts article text segments from raw data.

### Parameters

- **data** (str): Raw article data string containing title, headings, paragraphs, etc.

### Returns

list: A list of strings, each representing a paragraph or text segment extracted from the article.

### Raises

- ValueError: Raised when the input string does not contain any extractable text.
- TypeError: Raised when the input is not of type str.

### Examples

```python
>>> result = extract_texts('Title\n\nParagraph one.\n\nParagraph two.')
>>> print(result)
['Paragraph one.', 'Paragraph two.']
```

```python
>>> print(extract_texts(''))
[]
```
