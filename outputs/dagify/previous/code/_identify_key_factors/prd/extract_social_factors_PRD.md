# extract_social_factors PRD

## Description
Extracts a list of primary social factors influencing a specified historical event from provided historical data.


## Conceptual Info

This shim encapsulates the logic required to distill social influences from raw historical narratives, enabling downstream modules to focus on higher‑level analysis without re‑implementing complex NLP or domain‑specific heuristics.

## Docstring

### Summary
Extracts primary social factors from a block of historical data for a given event.

### Parameters

- **historical_data** (str): A textual representation of historical information that may include descriptions, accounts, or analyses relevant to the event.
- **event** (str): The name or title of the historical event for which social factors should be extracted.

### Returns

list[str]: A list of strings, each representing a distinct social factor that had a significant influence on the specified event.

### Raises

- ValueError: Raised when `historical_data` is empty or the event cannot be found within the data.
- TypeError: Raised when either `historical_data` or `event` is not of type `str`.

### Examples

```python
>>> extract_social_factors('Industrial Revolution was marked by rapid mechanization and urban migration.', 'Industrial Revolution')
['Mechanization', 'Urban migration', 'Labor movement']
```

```python
>>> extract_social_factors('The French Revolution was driven by Enlightenment ideas, economic hardship, and class conflict.', 'French Revolution')
['Enlightenment ideas', 'Economic hardship', 'Class conflict']
```
