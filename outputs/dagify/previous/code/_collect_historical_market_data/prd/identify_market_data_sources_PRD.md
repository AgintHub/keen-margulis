# identify_market_data_sources PRD

## Description
Identifies relevant market data sources based on input parameters and additional keyword arguments.


## Conceptual Info

This shim node is responsible for determining the appropriate market data sources based on the provided input parameters and additional keyword arguments. It plays a crucial role in the data collection pipeline by identifying where to fetch historical market data.

## Docstring

### Summary
Identifies market data sources based on input parameters and additional keyword arguments.

### Parameters

- **input_params** (str): General input string used to determine the relevant market data sources.
- **kwargs** (str): Additional keyword arguments that may influence the identification of market data sources.

### Returns

List[str]: A list of strings representing the identified market data sources.

### Raises

- ValueError: If the input parameters or keyword arguments are invalid or insufficient to identify market data sources.
- TypeError: If the input parameters or keyword arguments are of incorrect type.

### Examples

```python
>>> identify_market_data_sources(input_params='stock_data', kwargs='{"exchange": "NYSE"}')
>>> identify_market_data_sources(input_params='forex_data', kwargs='{"currency_pair": "USD/EUR"}')
['source1', 'source2']
```

```python
>>> identify_market_data_sources(input_params='crypto_data', kwargs='{"exchange": "Binance"}')
['crypto_source1', 'crypto_source2']
```
