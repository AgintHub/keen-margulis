# extract_cultural_factors PRD

## Description
Extracts a list of primary cultural factors influencing a historical event or period based on provided historical data and event name.


## Conceptual Info

The shim analyzes provided historical data for a given event, identifying key cultural elements that shaped the period.

## Docstring

### Summary
Return a list of primary cultural factors influencing a specified historical event.

### Parameters

- **historical_data** (str): Raw textual or structured historical data related to the event.
- **event** (str): Name or title of the historical event or period to analyze.

### Returns

list[str]: A list of cultural factors (strings) that had a significant impact on the event.

### Raises

- ValueError: Raised if either 'historical_data' or 'event' is empty or does not contain relevant information.
- TypeError: Raised if any argument is not of type 'str'.

### Examples

```python
>>> extract_cultural_factors(
...     historical_data="The Renaissance was a period of renewed interest in classical art and philosophy.",
...     event="Renaissance"
>>> )
['Art', 'Classical philosophy', 'Humanism']
```

```python
>>> extract_cultural_factors(
...     historical_data="The Cold War saw a surge in propaganda art and ideological literature.",
...     event="Cold War"
>>> )
['Propaganda art', 'Ideological literature', 'Cultural exchange']
```
