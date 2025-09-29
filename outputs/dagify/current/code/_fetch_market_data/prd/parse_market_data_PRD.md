# parse_market_data PRD

## Description
Parses raw market data into a structured dictionary format.


## Conceptual Info

This shim node is responsible for taking raw market data, which is a list of dictionaries, and parsing it into a structured dictionary format that can be used downstream for extracting prices and volumes.

## Docstring

### Summary
Parses raw market data string into a structured dictionary.

### Parameters

- **raw_data** (str): The raw market data as a string representation of a list of dictionaries.

### Returns

str: A dictionary containing the parsed market data, where keys and values are appropriately structured for further processing.

### Raises

- ValueError: If the input raw_data is not a valid string representation of a list of dictionaries.
- TypeError: If the input raw_data is not a string.

### Examples

```python
>>> raw_data = '[{"price": 10.5, "volume": 100}, {"price": 11.2, "volume": 50}]'
>>> parsed_data = parse_market_data(raw_data=raw_data)
{'prices': [10.5, 11.2], 'volumes': [100, 50]}
```

```python
>>> raw_data = '[{"price": 12.0, "volume": 200}]'
>>> parsed_data = parse_market_data(raw_data=raw_data)
{'prices': [12.0], 'volumes': [200]}
```
