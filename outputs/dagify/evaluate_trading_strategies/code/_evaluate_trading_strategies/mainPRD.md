# _evaluate_trading_strategies - Complete PRD Documentation

## Overview
PRDs for nodes in the '_evaluate_trading_strategies' module.

## Table of Contents

- [validate_input_lengths](#validate_input_lengths)

- [validate_input_types](#validate_input_types)

- [evaluate_strategies_from_trends](#evaluate_strategies_from_trends)

- [assess_strategy_risks](#assess_strategy_risks)



---

## validate_input_lengths

### Description
Validates that the length of the predictions list matches the length of the confidence list in the trading strategy evaluation process.

### Conceptual Info

Ensures that the prediction and confidence inputs supplied to downstream evaluation functions have identical lengths, preventing misalignment errors during strategy assessment.

### Docstring

**Summary:** Check that `predictions` and `confidence` lists are of equal length. Returns a confirmation string on success; otherwise raises an exception.

**Parameters:**

- predictions (List[str]): A list of string predictions for market trends.
- confidence (List[float]): A list of confidence scores corresponding to each prediction.
**Returns:** str - A success message such as "Lengths are valid" when the two lists have the same length.

**Raises:**

- ValueError: Raised when the lengths of `predictions` and `confidence` differ.
- TypeError: Raised if either argument is not a list or contains incompatible element types.
**Examples:**

```python
>>> validate_input_lengths(['bull', 'bear'], [0.8, 0.6])
'Lengths are valid'
```

```python
>>> validate_input_lengths(['bull', 'bear', 'neutral'], [0.8, 0.6])
Traceback (most recent call last):\n  ...\nValueError: Length mismatch: predictions has 3 elements while confidence has 2.
```



---

## validate_input_types

### Description
Validate that the predictions list contains strings and the confidence list contains floats of equal length.

### Conceptual Info

This shim ensures the core data passed between market trend analysis and strategy evaluation nodes is correctly typed and structurally consistent, preventing downstream processing errors.

### Docstring

**Summary:** Validate that the inputs `predictions` and `confidence` are lists of the expected types and have matching lengths.

**Parameters:**

- predictions (List[str]): A list of trend predictions, each element should be a string.
- confidence (List[float]): A list of confidence scores corresponding to each prediction, each element should be a float.
**Returns:** str - A message confirming successful validation, e.g., `'Validation successful'`.

**Raises:**

- ValueError: Raised if the lengths of `predictions` and `confidence` differ.
- TypeError: Raised if any element of `predictions` is not a string or any element of `confidence` is not a float.
**Examples:**

```python
>>> output = validate_input_types(predictions=['trend1', 'trend2'], confidence=[0.9, 0.8])
'Validation successful'
```

```python
>>> output = validate_input_types(predictions=['trend1'], confidence=[0.9])
'Validation successful'
```



---

## evaluate_strategies_from_trends

### Description
Evaluates trading strategies from trend predictions and confidence levels, returning a list of strategy evaluation strings.

### Conceptual Info

The shim translates market trend predictions and their confidence scores into actionable evaluations of trading strategies, serving as a bridge between trend analysis and strategy assessment components.

### Docstring

**Summary:** Generate strategy evaluations based on trend predictions and confidence levels.

**Parameters:**

- predictions (List[str]): A list of textual predictions of future market trends (e.g., "bullish", "bearish").
- confidence (List[float]): A list of confidence scores (between 0 and 1) corresponding to each trend prediction.
**Returns:** List[str] - A list of strategy evaluation strings, one per input prediction, summarizing the suitability or risk of each strategy.

**Raises:**

- ValueError: If the lengths of `predictions` and `confidence` differ.
- TypeError: If elements of `predictions` are not strings or elements of `confidence` are not floats or cannot be coerced to floats.
**Examples:**

```python
>>> preds = ['bullish', 'bearish']
>>> conf = [0.85, 0.6]
>>> result = evaluate_strategies_from_trends(predictions=preds, confidence=conf)
>>> print(result)
['High confidence in bullish strategy, consider long positions', 'Moderate confidence in bearish strategy, consider short positions']
```

```python
>>> preds = ['sideways']
>>> conf = [0.4]
>>> print(evaluate_strategies_from_trends(predictions=preds, confidence=conf))
['Low confidence in trend, consider low-risk or hedging strategies']
```



---

## assess_strategy_risks

### Description
Assesses the risk level for each trading strategy based on trend predictions, confidence levels, and strategy evaluations.

### Conceptual Info

This shim takes in trend predictions, confidence levels, and strategy evaluations, validates the inputs, and computes a quantitative risk score for each strategy.

### Docstring

**Summary:** Compute a risk score for each trading strategy based on trend predictions, confidence levels, and strategy evaluations.

**Parameters:**

- predictions (List[str]): Predicted market trends for each strategy.
- confidence (List[float]): Confidence levels corresponding to each trend prediction.
- evaluations (List[str]): Evaluations of each trading strategy derived from the predictions.
**Returns:** List[float] - A list of risk scores, one per strategy, where higher values indicate greater risk.

**Raises:**

- ValueError: Raised when the lengths of predictions, confidence, or evaluations differ.
- TypeError: Raised when inputs are not of the expected types.
**Examples:**

```python
>>> predictions = ['Bullish', 'Bearish', 'Neutral']
>>> confidence = [0.9, 0.6, 0.7]
>>> evaluations = ['Aggressive', 'Conservative', 'Balanced']
>>> risk_scores = assess_strategy_risks(predictions, confidence, evaluations)
[0.1, 0.4, 0.3]
```

```python
>>> predictions = ['Bullish', 'Bearish']
>>> confidence = [0.8, 0.5]
>>> evaluations = ['Aggressive', 'Conservative']
>>> risk_scores = assess_strategy_risks(predictions, confidence, evaluations)
[0.2, 0.5]
```

