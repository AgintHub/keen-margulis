# extract_themes PRD

## Description
Identify the dominant lyrical themes.


## Conceptual Info

Extracts the five most frequent words from all song lyrics and calculates each word’s relative frequency as a normalized score.

## Docstring

### Summary
Selects the top five words by occurrence from lyric word statistics and returns them with their normalized frequency scores.

### Parameters

- **unique_words** (List[str]): List of unique words sorted by descending frequency.
- **word_counts** (List[int]): Parallel list of counts corresponding to each word in `unique_words`.

### Returns

Tuple[List[str], List[float]]: A tuple containing the top 5 thematic words and a list of their normalized scores.

### Raises

- ValueError: If `unique_words` and `word_counts` are empty or have mismatched lengths.
- ValueError: If the total word count is zero (cannot compute normalized scores).

### Examples

```python
>>> unique_words = ['love', 'heart', 'night', 'dream', 'sky']
>>> word_counts = [10, 8, 5, 2, 1]
>>> themes, scores = extract_themes(unique_words, word_counts)
>>> print(themes)
>>> print(scores)
['love', 'heart', 'night', 'dream', 'sky']\n[0.38461538461538464, 0.3076923076923077, 0.19230769230769232, 0.07692307692307693, 0.038461538461538464]
```

```python
>>> unique_words = ['sun', 'rain']
>>> word_counts = [10, 5]
>>> themes, scores = extract_themes(unique_words, word_counts)
>>> print(themes)
>>> print(scores)
['sun', 'rain']\n[0.6666666666666666, 0.3333333333333333]
```
