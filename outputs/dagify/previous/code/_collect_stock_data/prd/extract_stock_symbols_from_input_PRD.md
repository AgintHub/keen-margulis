# extract_stock_symbols_from_input PRD

## Description
Extracts stock symbols from a given input text.


## Conceptual Info

This shim function is responsible for extracting stock symbols from a given input text, playing a crucial role in the stock data collection pipeline.

## Docstring

### Summary
Extracts stock symbols from the input text and returns them as a list of strings.

### Parameters

- **input_text** (str): The input text from which stock symbols will be extracted.

### Returns

List[str]: A list of stock symbols extracted from the input text.

### Raises

- ValueError: If the input text is empty or does not contain valid stock symbols.
- TypeError: If the input is not a string.

### Examples

```python
>>> stock_symbols = extract_stock_symbols_from_input(input_text='AAPL, GOOG, MSFT')
>>> print(stock_symbols)
['AAPL', 'GOOG', 'MSFT']
```

```python
>>> stock_symbols = extract_stock_symbols_from_input(input_text='Invalid input')
>>> print(stock_symbols)
[]
```
