# extract_political_factors PRD

## Description
Extracts a list of political factors that influenced a specified historical event based on provided historical data.


## Conceptual Info

The shim parses textual historical data to isolate political factors such as policies, leaders, alliances, and conflicts that directly impacted the specified event.

## Docstring

### Summary
Identify political factors influencing a historical event from raw data.

### Parameters

- **historical_data** (str): A plain text string containing contextual information about the historical event.
- **event** (str): The name or title of the historical event to analyze.

### Returns

list[str]: A list of strings, each describing a distinct political factor relevant to the event.

### Raises

- ValueError: Raised when `historical_data` or `event` is empty or missing crucial information.
- TypeError: Raised when `historical_data` or `event` is not a string.

### Examples

```python
>>> extract_political_factors(historical_data='In 1917, the Bolsheviks seized power in Russia, overthrowing the provisional government and establishing a communist regime.', event='Russian Revolution')
['Revolutionary overthrow of the provisional government', 'Rise of Bolshevik leadership', 'Adoption of communist ideology']
```

```python
>>> extract_political_factors(historical_data='The 1960s Civil Rights Movement led to significant policy changes in the United States.', event='Civil Rights Movement')
['Legislative reforms', 'Judicial decisions', 'Federal executive action']
```
