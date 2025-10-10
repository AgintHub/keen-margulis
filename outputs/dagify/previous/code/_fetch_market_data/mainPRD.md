# _fetch_market_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_fetch_market_data' module.

## Table of Contents

- [get_market_data_sources](#get_market_data_sources)

- [fetch_data_from_sources](#fetch_data_from_sources)

- [parse_market_data](#parse_market_data)

- [extract_prices](#extract_prices)

- [extract_volumes](#extract_volumes)

- [validate_market_data](#validate_market_data)



---

## get_market_data_sources

### Description
Retrieves a list of URLs for market data sources.

### Conceptual Info

This shim function is responsible for providing a list of URLs that serve as sources for market data. It acts as a bridge to fetch the necessary data for further processing.

### Docstring

**Summary:** Fetches and returns a list of URLs for market data sources.

**Returns:** List[str] - A list of URLs where market data can be fetched.

**Raises:**

- RuntimeError: If there's an issue retrieving the market data sources.
**Examples:**

```python
>>> sources = get_market_data_sources()
['https://source1.com/data', 'https://source2.com/data']
```

```python
>>> print(get_market_data_sources())
['https://source1.com/data', 'https://source2.com/data']
```



---

## fetch_data_from_sources

### Description
Fetches data from multiple sources and returns it in a structured format.

### Conceptual Info

This shim node is responsible for fetching data from multiple sources and returning it in a structured format that can be further processed downstream.

### Docstring

**Summary:** Fetches data from the provided sources and returns it as a list of dictionaries.

**Parameters:**

- sources (str): A string representing the sources from which data should be fetched.
**Returns:** List[dict] - A list of dictionaries containing the fetched data from various sources.

**Raises:**

- ValueError: If the input 'sources' is not a valid string or is empty.
- TypeError: If the input 'sources' is not of type string.
**Examples:**

```python
>>> sources = 'https://example.com/data1,https://example.com/data2'
>>> result = fetch_data_from_sources(sources=sources)
[{'source': 'https://example.com/data1', 'data': '...'}, {'source': 'https://example.com/data2', 'data': '...'}]
```

```python
>>> sources = 'https://example.com/data3'
>>> result = fetch_data_from_sources(sources=sources)
[{'source': 'https://example.com/data3', 'data': '...'}]
```



---

## parse_market_data

### Description
Parses raw market data into a structured dictionary format.

### Conceptual Info

This shim node is responsible for taking raw market data, which is a list of dictionaries, and parsing it into a structured dictionary format that can be used downstream for extracting prices and volumes.

### Docstring

**Summary:** Parses raw market data string into a structured dictionary.

**Parameters:**

- raw_data (str): The raw market data as a string representation of a list of dictionaries.
**Returns:** str - A dictionary containing the parsed market data, where keys and values are appropriately structured for further processing.

**Raises:**

- ValueError: If the input raw_data is not a valid string representation of a list of dictionaries.
- TypeError: If the input raw_data is not a string.
**Examples:**

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



---

## extract_prices

### Description
Extracts a list of prices from the given parsed market data.

### Conceptual Info

This shim node is responsible for extracting a list of prices from the parsed market data, which is crucial for further analysis and processing in the market data pipeline.

### Docstring

**Summary:** Extracts prices from the given parsed market data and returns them as a list of floats.

**Parameters:**

- parsed_data (str): A string representation of the parsed market data, expected to contain price information.
**Returns:** List[float] - A list of float values representing the extracted prices.

**Raises:**

- ValueError: If the parsed data is malformed or does not contain valid price information.
- TypeError: If the input parsed_data is not of type str.
**Examples:**

```python
>>> parsed_data = '{ "prices": [10.5, 20.8, 30.1] }'
>>> prices = extract_prices(parsed_data=parsed_data)
>>> print(prices)
[10.5, 20.8, 30.1]
```

```python
>>> parsed_data = 'Invalid data'
>>> try: extract_prices(parsed_data=parsed_data)
>>> except ValueError as e: print(e)
Malformed input data
```



---

## extract_volumes

### Description
Extracts market volumes from parsed market data.

### Conceptual Info

This shim function is responsible for extracting market volumes from the parsed market data, playing a crucial role in processing financial data for further analysis.

### Docstring

**Summary:** Extracts and returns market volumes as a list of integers from the given parsed market data.

**Parameters:**

- parsed_data (str): A string representation of parsed market data containing volume information.
**Returns:** List[int] - A list of integers representing the extracted market volumes.

**Raises:**

- ValueError: If the parsed_data is not in the expected format or if volume extraction fails.
- TypeError: If the input parsed_data is not of type str.
**Examples:**

```python
>>> parsed_data = '{ "market_volumes": [100, 200, 300] }'
>>> volumes = extract_volumes(parsed_data=parsed_data)
>>> print(volumes)
[100, 200, 300]
```

```python
>>> parsed_data = 'Invalid data format'
>>> try:
...     volumes = extract_volumes(parsed_data=parsed_data)
>>> except ValueError as e:
...     print(e)
Invalid data format
```



---

## validate_market_data

### Description
Validates market data by checking prices and volumes for consistency and correctness.

### Conceptual Info

This shim node is responsible for validating market data, specifically checking if the provided prices and volumes are consistent and correct.

### Docstring

**Summary:** Validates market data by checking the consistency and correctness of prices and volumes.

**Parameters:**

- prices (List[float]): List of current market prices to be validated.
- volumes (List[int]): List of current market volumes to be validated.
**Returns:** str - Output indicating whether the market data is valid or not.

**Raises:**

- ValueError: When the lengths of prices and volumes lists do not match.
- TypeError: When prices or volumes contain invalid data types.
**Examples:**

```python
>>> validate_market_data(prices=[10.5, 20.8, 30.1], volumes=[100, 200, 300])
'Market data is valid'
```

```python
>>> validate_market_data(prices=[10.5, 'invalid', 30.1], volumes=[100, 200, 300])
TypeError: Prices must be a list of floats.
```

