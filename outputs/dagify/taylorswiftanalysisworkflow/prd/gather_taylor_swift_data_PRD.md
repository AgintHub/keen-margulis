# gather_taylor_swift_data PRD

## Description
Collect data on Taylor Swift's discography, lyrics, and chart performance.


## Conceptual Info

This node collects comprehensive data on Taylor Swift's music, including album names, release dates, song lyrics, and chart performance metrics.

## Docstring

### Summary
Gathers data on Taylor Swift's discography, lyrics, and chart performance.

### Returns

dict: A dictionary containing lists of album names, release dates, song lyrics, and chart performance metrics.

### Raises

- DataCollectionError: If there's an issue collecting data from the sources.
- DataFormatError: If the collected data is not in the expected format.

### Examples

```python
>>> data = gather_taylor_swift_data()
>>> print(data['album_names'])
>>> print(data['release_dates'])
>>> print(data['song_lyrics'])
>>> print(data['chart_performance'])
['Taylor Swift', 'Fearless', ...]
['2006-10-24', '2008-11-11', ...]
[' lyrics1 ', ' lyrics2 ', ...]
[10, 20, ...]
```
