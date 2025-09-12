# taylor_swift_analysis_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'taylor_swift_analysis_workflow' module.

## Table of Contents

- [fetch_song_data](#fetch_song_data)

- [analyze_lyrics](#analyze_lyrics)

- [extract_themes](#extract_themes)

- [sentiment_analysis](#sentiment_analysis)

- [trend_over_time](#trend_over_time)

- [generate_summary](#generate_summary)



---

## fetch_song_data

### Description
Collect basic metadata and lyrics for all Taylor Swift songs.

### Conceptual Info

Collect basic metadata and lyrics for all Taylor Swift songs.

### Docstring

**Summary:** Fetches a list of all Taylor Swift songs along with their full lyrics and release years from a public API.

**Parameters:**

- artist (str): Name of the artist to query. Defaults to "Taylor Swift".
**Returns:** dict - Dictionary containing three keys: `song_titles` (List[str]), `song_lyrics` (List[str]), and `release_years` (List[int]). The lists are aligned by index.

**Raises:**

- ValueError: If the API request fails or returns an unexpected status code.
- KeyError: If the API response is missing required fields (e.g., title, lyrics, or year).
**Examples:**

```python
>>> result = fetch_song_data()
>>> print(result['song_titles'][0])
"Love Story"
```

```python
>>> result = fetch_song_data(artist="Taylor Swift")
>>> print(len(result['song_titles']))
"<total number of Taylor Swift songs>"
```



---

## analyze_lyrics

### Description
Generate word frequency statistics from all lyrics.

### Conceptual Info

This node aggregates raw lyrical text into a concise frequency table, enabling downstream theme extraction and sentiment analysis.

### Docstring

**Summary:** Computes the frequency of every unique word across all song lyrics and returns the words sorted by decreasing count.

**Parameters:**

- song_titles (List[str]): Parallel list of song titles; provided for context but not used in frequency computation.
- song_lyrics (List[str]): Parallel list of full lyrics corresponding to each song title.
**Returns:** Tuple[List[str], List[int]] - A tuple containing the list of unique words sorted by descending frequency and a parallel list of their counts.

**Raises:**

- ValueError: Raised if `song_lyrics` is empty or all entries are blank.
- TypeError: Raised if inputs are not lists of strings.
**Examples:**

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



---

## extract_themes

### Description
Identify the dominant lyrical themes.

### Conceptual Info

Extracts the five most frequent words from all song lyrics and calculates each word’s relative frequency as a normalized score.

### Docstring

**Summary:** Selects the top five words by occurrence from lyric word statistics and returns them with their normalized frequency scores.

**Parameters:**

- unique_words (List[str]): List of unique words sorted by descending frequency.
- word_counts (List[int]): Parallel list of counts corresponding to each word in `unique_words`.
**Returns:** Tuple[List[str], List[float]] - A tuple containing the top 5 thematic words and a list of their normalized scores.

**Raises:**

- ValueError: If `unique_words` and `word_counts` are empty or have mismatched lengths.
- ValueError: If the total word count is zero (cannot compute normalized scores).
**Examples:**

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



---

## sentiment_analysis

### Description
Compute sentiment for each song.

### Conceptual Info

Performs sentiment analysis on song lyrics, producing a sentiment score for each track.

### Docstring

**Summary:** Computes overall sentiment scores for a list of song lyrics, returning a list of floats between -1 and 1 aligned with song titles.

**Parameters:**

- song_titles (List[str]): List of song titles corresponding to the lyrics.
- song_lyrics (List[str]): List of full lyrics for each song.
**Returns:** List[float] - Sentiment score for each song.

**Raises:**

- ValueError: If input lists are not the same length or are empty.
**Examples:**

```python
>>> scores = sentiment_analysis(["Love Story", "Bad Blood"], ["I knew you were trouble, so I stayed away", "I used to love you, now I hate you"])
[0.76, -0.62]
```

```python
>>> scores = sentiment_analysis(["Blank Space"], ["So nice I can't decide if I'm a love or a lie"])
[0.48]
```



---

## trend_over_time

### Description
Summarize sentiment trend across release years.

### Conceptual Info

This node aggregates song-level sentiment scores into year-level averages, providing a temporal view of lyrical sentiment across Taylor Swift's discography.

### Docstring

**Summary:** Compute average sentiment per release year from parallel lists of years and sentiment scores.

**Parameters:**

- release_years (List[int]): List of release years for each song, aligned with sentiment_scores.
- sentiment_scores (List[float]): Sentiment score for each song, ranging from -1 (very negative) to 1 (very positive).
**Returns:** Tuple[List[int], List[float]] - A tuple containing two parallel lists:
- years: Chronological list of years with songs.
- avg_sentiment: Average sentiment for each corresponding year.

**Raises:**

- ValueError: If release_years and sentiment_scores are of different lengths.
- ValueError: If either input list is empty.
**Examples:**

```python
>>> years, avg = trend_over_time([2015, 2015, 2016], [0.2, 0.5, -0.1])
([2015, 2016], [0.35, -0.1])
```

```python
>>> trend_over_time([2015, 2016], [0.3])
Traceback (most recent call last):
  ...
ValueError: release_years and sentiment_scores must have the same length.
```



---

## generate_summary

### Description
Produce a human‑readable summary of the findings.

### Conceptual Info

Generates a short narrative that encapsulates the dominant lyrical themes and the sentiment trajectory over the artist's career, highlighting any key shifts or anomalies.

### Docstring

**Summary:** Create a concise paragraph summarizing key lyrical themes and sentiment trends.

**Parameters:**

- themes (List[str]): Top 5 thematic words in descending frequency order.
- theme_scores (List[float]): Normalized frequency score for each corresponding theme (sum of all scores should equal 1).
- years (List[int]): Chronological list of release years for which sentiment averages have been computed.
- avg_sentiment (List[float]): Average sentiment score for each year, aligned with the `years` list. Scores range from -1 (very negative) to +1 (very positive).
**Returns:** str - A single paragraph that lists the top themes, summarizes the sentiment trend over time, and notes any significant pattern shifts.

**Raises:**

- ValueError: If `themes` and `theme_scores` lists are of unequal length, or if any of the input lists are empty.
- TypeError: If any of the parameters is not of the expected type.
**Examples:**

```python
>>> generate_summary(
...     themes=["love", "heartbreak", "growth", "rebellion", "dreams"],
...     theme_scores=[0.28, 0.22, 0.18, 0.12, 0.10],
...     years=[2013, 2014, 2015, 2016, 2017],
...     avg_sentiment=[0.15, 0.08, 0.02, -0.04, -0.10]
>>> )
"The analysis highlights love and heartbreak as the dominant lyrical themes, followed by growth, rebellion, and dreams. Sentiment shifts from mildly positive in 2013 to increasingly negative by 2017, indicating a noticeable downturn in overall lyrical mood during the latter years."
```

```python
>>> generate_summary(
...     themes=["hope", "rain", "silence", "journey", "home"],
...     theme_scores=[0.30, 0.20, 0.15, 0.12, 0.10],
...     years=[2012, 2013, 2014],
...     avg_sentiment=[0.05, 0.10, 0.15]"
                ")
"The prevailing themes are hope, rain, silence, journey, and home. The sentiment trend shows a steady improvement from 2012 to 2014, suggesting an increasingly optimistic tone over time."
```

