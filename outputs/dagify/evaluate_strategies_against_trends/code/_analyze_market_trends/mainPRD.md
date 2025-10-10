# _analyze_market_trends - Complete PRD Documentation

## Overview
PRDs for nodes in the '_analyze_market_trends' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [normalize_market_data](#normalize_market_data)

- [analyze_price_trends](#analyze_price_trends)

- [analyze_volume_indicators](#analyze_volume_indicators)

- [combine_trend_indicators](#combine_trend_indicators)

- [identify_chart_patterns](#identify_chart_patterns)



---

## validate_input_data

### Description
Validates input data for market analysis to ensure it conforms to expected formats and ranges.

### Conceptual Info

This shim node is responsible for validating the input market data to ensure it meets the necessary criteria for further analysis.

### Docstring

**Summary:** Validates input market data including current prices, historical prices, and trading volumes.

**Parameters:**

- current_prices (str): Current prices of the assets in string format, expected to be convertible to a list of floats.
- historical_prices (str): Historical price data for the assets over a specified period in string format, expected to be convertible to a list of floats.
- trading_volumes (str): Trading volumes for the assets in string format, expected to be convertible to a list of floats.
**Returns:** str - A string indicating whether the input data is valid ('valid') or not ('invalid').

**Raises:**

- ValueError: Raised when the input strings cannot be converted to the expected numerical formats or are out of expected ranges.
- TypeError: Raised when the input parameters are not strings.
**Examples:**

```python
>>> validate_input_data(current_prices='[1.0, 2.0, 3.0]', historical_prices='[4.0, 5.0, 6.0]', trading_volumes='[7.0, 8.0, 9.0]')
'valid'
```

```python
>>> validate_input_data(current_prices='invalid', historical_prices='[4.0, 5.0, 6.0]', trading_volumes='[7.0, 8.0, 9.0]')
'invalid'
```



---

## normalize_market_data

### Description
Normalizes market data by processing current prices, historical prices, and trading volumes into a standardized format.

### Conceptual Info

This shim node is responsible for normalizing market data, which includes current prices, historical prices, and trading volumes, into a standardized format that can be used for further analysis.

### Docstring

**Summary:** Normalizes market data inputs into a standardized dictionary format.

**Parameters:**

- current_prices (str): A string representation of a list of current prices of assets.
- historical_prices (str): A string representation of a list of historical prices of assets.
- trading_volumes (str): A string representation of a list of trading volumes of assets.
**Returns:** str - A string representation of a dictionary containing the normalized market data.

**Raises:**

- ValueError: If the input strings cannot be parsed into lists of floats.
- TypeError: If the input parameters are not strings.
**Examples:**

```python
>>> normalize_market_data('[100.0, 200.0]', '[50.0, 150.0, 250.0]', '[1000.0, 2000.0]')
'{"current_prices": [100.0, 200.0], "historical_prices": [50.0, 150.0, 250.0], "trading_volumes": [1000.0, 2000.0]}'
```

```python
>>> normalize_market_data('[150.0, 250.0]', '[75.0, 175.0, 275.0]', '[1500.0, 2500.0]')
'{"current_prices": [150.0, 250.0], "historical_prices": [75.0, 175.0, 275.0], "trading_volumes": [1500.0, 2500.0]}'
```



---

## analyze_price_trends

### Description
Analyzes current and historical price data to identify trends and patterns.

### Conceptual Info

This shim analyzes price trends by comparing current and historical prices, identifying patterns and trends that could inform market analysis.

### Docstring

**Summary:** Analyzes current and historical price data to identify market trends and patterns.

**Parameters:**

- current_prices (str): Current prices of the assets in a string format, expected to be a comma-separated list of float values.
- historical_prices (str): Historical price data for the assets over a specified period in a string format, expected to be a comma-separated list of float values.
**Returns:** List[str] - List of identified price trends and patterns, such as 'bullish', 'bearish', or other trend indicators.

**Raises:**

- ValueError: If the input strings for current_prices or historical_prices are not properly formatted or contain invalid data.
- TypeError: If the input parameters are not strings.
**Examples:**

```python
>>> analyze_price_trends(current_prices='100.0,120.0,110.0', historical_prices='90.0,100.0,110.0,120.0,130.0')
>>> output = ['bullish']
['bullish']
```

```python
>>> analyze_price_trends(current_prices='80.0,70.0,60.0', historical_prices='100.0,90.0,80.0,70.0,60.0')
>>> output = ['bearish']
['bearish']
```



---

## analyze_volume_indicators

### Description
Analyzes trading volume indicators in relation to price data to identify market trends.

### Conceptual Info

This shim analyzes trading volume indicators in the context of price data to identify significant market trends or patterns, playing a crucial role in the overall market trend analysis pipeline.

### Docstring

**Summary:** Analyzes trading volume indicators in relation to price data to identify market trends or patterns.

**Parameters:**

- trading_volumes (str): A string representation of trading volumes, expected to be a comma-separated list of volume values.
- price_data (str): A string representation of price data, expected to be a comma-separated list of price values corresponding to the trading volumes.
**Returns:** List[str] - A list of strings representing the analyzed volume indicators in relation to the price data, indicating market trends or patterns.

**Raises:**

- ValueError: Raised when the input strings are not in the expected format or contain invalid data.
- TypeError: Raised when the input types are not as expected (i.e., not strings).
**Examples:**

```python
>>> analyze_volume_indicators(trading_volumes='100,200,300', price_data='10.0,20.0,30.0')
['Bullish', 'Bearish', 'Neutral']
```

```python
>>> analyze_volume_indicators(trading_volumes='500,400,600', price_data='5.0,4.0,6.0')
['Increasing', 'Decreasing', 'Stable']
```



---

## combine_trend_indicators

### Description
Combines price and volume trend indicators into a unified list of trend indicators.

### Conceptual Info

This shim node is responsible for merging price and volume trend indicators into a single list, providing a unified view of market trends.

### Docstring

**Summary:** Combines price and volume trend indicators into a single list.

**Parameters:**

- price_trends (str): A string representing price trends, expected to be in a format that can be parsed into a list of trend indicators.
- volume_trends (str): A string representing volume trends, expected to be in a format that can be parsed into a list of trend indicators.
**Returns:** List[str] - A list of combined trend indicators.

**Raises:**

- ValueError: If the input strings cannot be parsed into valid trend indicators.
- TypeError: If the input types are not strings.
**Examples:**

```python
>>> price_trends = 'up,down,stable'
>>> volume_trends = 'high,low,medium'
>>> output = combine_trend_indicators(price_trends=price_trends, volume_trends=volume_trends)
['up_high', 'down_low', 'stable_medium']
```

```python
>>> price_trends = 'bullish,bearish'
>>> volume_trends = 'increasing,decreasing'
>>> output = combine_trend_indicators(price_trends=price_trends, volume_trends=volume_trends)
['bullish_increasing', 'bearish_decreasing']
```



---

## identify_chart_patterns

### Description
Identifies chart patterns in financial data based on current prices, historical prices, and trading volumes.

### Conceptual Info

This shim node is responsible for analyzing financial market data to identify chart patterns. It takes current prices, historical prices, and trading volumes as input and returns a list of recognized patterns.

### Docstring

**Summary:** Identifies chart patterns in financial data based on the provided current prices, historical prices, and trading volumes.

**Parameters:**

- current_prices (str): Current prices of the assets, expected to be a string representation of a list of floats.
- historical_prices (str): Historical price data for the assets over a specified period, expected to be a string representation of a list of floats.
- volumes (str): Trading volumes for the assets, expected to be a string representation of a list of floats.
**Returns:** List[str] - A list of identified chart patterns as strings.

**Raises:**

- ValueError: If the input strings cannot be parsed into lists of floats.
- TypeError: If the input types are not strings.
**Examples:**

```python
>>> current_prices = '[100.0, 120.0, 110.0]'
>>> historical_prices = '[90.0, 100.0, 110.0, 120.0, 130.0]'
>>> volumes = '[1000, 1200, 1100]'
>>> output = identify_chart_patterns(current_prices, historical_prices, volumes)
['Bullish Trend', 'Resistance Breakout']
```

```python
>>> current_prices = '[50.0, 60.0, 55.0]'
>>> historical_prices = '[40.0, 50.0, 60.0, 55.0, 65.0]'
>>> volumes = '[500, 600, 550]'
>>> output = identify_chart_patterns(current_prices, historical_prices, volumes)
['Bearish Divergence', 'Support Level']
```

