# generate_summary PRD

## Description
Produce a human‑readable summary of the findings.


## Conceptual Info

Generates a short narrative that encapsulates the dominant lyrical themes and the sentiment trajectory over the artist's career, highlighting any key shifts or anomalies.

## Docstring

### Summary
Create a concise paragraph summarizing key lyrical themes and sentiment trends.

### Parameters

- **themes** (List[str]): Top 5 thematic words in descending frequency order.
- **theme_scores** (List[float]): Normalized frequency score for each corresponding theme (sum of all scores should equal 1).
- **years** (List[int]): Chronological list of release years for which sentiment averages have been computed.
- **avg_sentiment** (List[float]): Average sentiment score for each year, aligned with the `years` list. Scores range from -1 (very negative) to +1 (very positive).

### Returns

str: A single paragraph that lists the top themes, summarizes the sentiment trend over time, and notes any significant pattern shifts.

### Raises

- ValueError: If `themes` and `theme_scores` lists are of unequal length, or if any of the input lists are empty.
- TypeError: If any of the parameters is not of the expected type.

### Examples

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
