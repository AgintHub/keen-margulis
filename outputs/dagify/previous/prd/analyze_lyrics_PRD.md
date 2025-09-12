# analyze_lyrics PRD

## Description
Generate word frequency statistics from all lyrics.


## Conceptual Info

This node aggregates raw lyrical text into a concise frequency table, enabling downstream theme extraction and sentiment analysis.

## Docstring

### Summary
Computes the frequency of every unique word across all song lyrics and returns the words sorted by decreasing count.

### Parameters

- **song_titles** (List[str]): Parallel list of song titles; provided for context but not used in frequency computation.
- **song_lyrics** (List[str]): Parallel list of full lyrics corresponding to each song title.

### Returns

Tuple[List[str], List[int]]: A tuple containing the list of unique words sorted by descending frequency and a parallel list of their counts.

### Raises

- ValueError: Raised if `song_lyrics` is empty or all entries are blank.
- TypeError: Raised if inputs are not lists of strings.

### Examples

```python
>>> song_titles = ['A', 'B']
>>> song_lyrics = ['Hello world hello', 'World of code']
>>> unique, counts = analyze_lyrics(song_titles, song_lyrics)
>>> print(unique)
>>> print(counts)
['hello', 'world', 'of', 'code']
[3, 2, 1, 1]
```

```python
>>> song_titles = ['Song']
>>> song_lyrics = ['I love coding', 'I love coding', 'Coding is fun']
>>> unique, counts = analyze_lyrics(song_titles, song_lyrics)
>>> print(dict(zip(unique, counts)))
{'i': 3, 'love': 2, 'coding': 3, 'is': 1, 'fun': 1}
```
