# _generate_trading_signals - Complete PRD Documentation

## Overview
PRDs for nodes in the '_generate_trading_signals' module.

## Table of Contents

- [validate_input_lengths](#validate_input_lengths)

- [validate_input_types](#validate_input_types)

- [process_recommended_strategies](#process_recommended_strategies)

- [calculate_signal_confidence](#calculate_signal_confidence)



---

## validate_input_lengths

### Description
Validates that the input lists have the same length.

### Conceptual Info

This shim node validates that the input lists for evaluations and strategies have the same length, ensuring data consistency before further processing.

### Docstring

**Summary:** Validates the lengths of input lists for evaluations and strategies.

**Parameters:**

- evaluations (str): String representation of a list of evaluations.
- strategies (str): String representation of a list of strategies.
**Returns:** str - Output indicating whether the input lists have the same length.

**Raises:**

- ValueError: If the lengths of the input lists do not match.
**Examples:**

```python
>>> validate_input_lengths(evaluations='[1, 2, 3]', strategies='["a", "b", "c"]')
'Input lengths are valid'
```

```python
>>> validate_input_lengths(evaluations='[1, 2]', strategies='["a", "b", "c"]')
ValueError: 'Input lists have different lengths'
```



---

## validate_input_types

### Description
Validates that the input evaluations and strategies are of the correct type.

### Conceptual Info

This shim node is responsible for validating the data types of input evaluations and strategies, ensuring they are List[str] as expected by downstream processing.

### Docstring

**Summary:** Validates the input types of evaluations and strategies, raising exceptions for invalid types.

**Parameters:**

- evaluations (List[str]): A list of strategy evaluations to be validated.
- strategies (List[str]): A list of recommended strategies to be validated.
**Returns:** str - A success message if both inputs are valid List[str].

**Raises:**

- TypeError: If either evaluations or strategies is not a List[str].
**Examples:**

```python
>>> validate_input_types(evaluations=['eval1', 'eval2'], strategies=['strat1', 'strat2'])
'Input types are valid.'
```

```python
>>> validate_input_types(evaluations='not a list', strategies=['strat1', 'strat2'])
TypeError: Evaluations must be a List[str]
```



---

## process_recommended_strategies

### Description
Processes a list of recommended trading strategies to produce a list of trading signals.

### Conceptual Info

This shim node takes a list of recommended trading strategies as input and generates a list of trading signals as output, serving as an intermediary step in the trading signal generation pipeline.

### Docstring

**Summary:** Processes recommended trading strategies to generate trading signals.

**Parameters:**

- strategies (str): A string representing a list of recommended trading strategies.
**Returns:** List[str] - A list of trading signals generated based on the input strategies.

**Raises:**

- ValueError: If the input strategies are not in the expected format.
- TypeError: If the input is not a string or does not represent a list.
**Examples:**

```python
>>> process_recommended_strategies(strategies='["Strategy1", "Strategy2"]')
['Signal1', 'Signal2']
```

```python
>>> process_recommended_strategies(strategies='["Strategy3"]')
['Signal3']
```



---

## calculate_signal_confidence

### Description
Calculates confidence levels for generated trading signals based on strategy evaluations and recommendations.

### Conceptual Info

This shim node is responsible for determining the confidence levels of trading signals generated based on the evaluations of different trading strategies and the recommended strategies.

### Docstring

**Summary:** Calculates confidence levels for trading signals based on strategy evaluations and recommendations.

**Parameters:**

- evaluations (str): A string containing evaluations of different trading strategies, expected to be in a format that can be parsed by the implementation.
- strategies (str): A string containing recommended trading strategies, expected to be in a format that can be parsed by the implementation.
**Returns:** List[float] - A list of floating-point numbers representing the confidence levels for the generated trading signals.

**Raises:**

- ValueError: If the input strings are not in the expected format or contain invalid data.
- TypeError: If the input parameters are not of the expected type.
**Examples:**

```python
>>> evaluations = 'strategy1:0.8;strategy2:0.9'
>>> strategies = 'strategy1;strategy2'
>>> confidence_levels = calculate_signal_confidence(evaluations, strategies)
[0.8, 0.9]
```

```python
>>> evaluations = 'strategyA:0.7;strategyB:0.6'
>>> strategies = 'strategyA;strategyB'
>>> confidence_levels = calculate_signal_confidence(evaluations, strategies)
[0.7, 0.6]
```

