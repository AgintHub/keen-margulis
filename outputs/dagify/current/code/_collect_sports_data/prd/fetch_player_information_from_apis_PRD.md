# fetch_player_information_from_apis PRD

## Description
Fetches player information from multiple APIs based on the provided data sources.


## Conceptual Info

This shim node is responsible for fetching player information from multiple APIs, playing a crucial role in data collection for sports analytics.

## Docstring

### Summary
Fetches player information from multiple APIs based on the provided data sources and returns a list of dictionaries.

### Parameters

- **sources** (str): A string representing the data sources to fetch player information from.

### Returns

List[dict]: A list of dictionaries where each dictionary contains player information fetched from the APIs.

### Raises

- ValueError: If the input 'sources' is invalid or empty.
- TypeError: If the input 'sources' is not of type string.

### Examples

```python
>>> fetch_player_information_from_apis(sources='api1,api2,api3')
[{'player_id': 1, 'name': 'John Doe'}, {'player_id': 2, 'name': 'Jane Doe'}]
```

```python
>>> fetch_player_information_from_apis(sources='api4')
[{'player_id': 3, 'name': 'Bob Smith'}]
```
