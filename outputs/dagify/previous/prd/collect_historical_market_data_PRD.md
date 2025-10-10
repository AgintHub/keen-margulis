# collect_historical_market_data PRD

## Description
Gather historical market data from various sources


## Conceptual Info

This node is responsible for gathering historical market data, including prices, volumes, and other relevant metrics, from various sources.

## Docstring

### Summary
Collects historical market data from multiple sources, returning prices, volumes, and other metrics.

### Returns

Tuple[List[float], List[float], List[str]]: A tuple containing historical prices, volumes, and other metrics.

### Raises

- ConnectionError: If there's an issue connecting to the data sources.
- DataError: If the retrieved data is malformed or incomplete.

### Examples

```python
>>> historical_data = collect_historical_market_data()
([100.0, 101.0, 102.0], [1000.0, 1100.0, 1200.0], ['metric1', 'metric2', 'metric3'])
```
