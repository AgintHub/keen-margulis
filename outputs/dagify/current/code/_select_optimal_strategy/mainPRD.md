# _select_optimal_strategy - Complete PRD Documentation

## Overview
PRDs for nodes in the '_select_optimal_strategy' module.

## Table of Contents

- [validate_input_lengths](#validate_input_lengths)

- [calculate_strategy_scores](#calculate_strategy_scores)

- [find_optimal_strategy_index](#find_optimal_strategy_index)

- [calculate_confidence_level](#calculate_confidence_level)



---

## validate_input_lengths

### Description
Validates that the evaluations and risks lists have equal length and correct types before strategy selection.

### Conceptual Info

This shim ensures data integrity by checking that the number of strategy evaluations matches the number of associated risk assessments before any downstream calculations are performed.

### Docstring

**Summary:** Checks that the provided evaluations and risks lists are of equal length and contain appropriate element types.

**Parameters:**

- evaluations (List[str]): A list of evaluation strings for each trading strategy.
- risks (List[float]): A list of risk scores corresponding to each evaluation.
**Returns:** str - A confirmation string "Input lengths validated" when inputs are correct.

**Raises:**

- ValueError: Raised when the lengths of evaluations and risks differ.
- TypeError: Raised when evaluations is not a list of strings or risks is not a list of floats.
**Examples:**

```python
>>> validate_input_lengths(evaluations=['win', 'draw', 'loss'], risks=[0.1, 0.2, 0.3])
"Input lengths validated"
```

```python
>>> validate_input_lengths(evaluations=['win', 'draw'], risks=[0.1, 0.2, 0.3])
ValueError: evaluations and risks must have the same length
```



---

## calculate_strategy_scores

### Description
Calculates a numeric score for each trading strategy based on its evaluation text and associated risk value.

### Conceptual Info

This shim computes a quantitative score for each trading strategy by combining the textual evaluation of the strategy with its associated risk level, enabling downstream selection of the optimal strategy.

### Docstring

**Summary:** Compute strategy scores from evaluation texts and risk values.

**Parameters:**

- evaluations (List[str]): A list of textual evaluations for each trading strategy.
- risks (List[float]): A list of risk values (between 0 and 1) corresponding to each strategy.
**Returns:** List[float] - A list of float scores, one for each strategy.

**Raises:**

- ValueError: Raised if evaluations and risks lists have different lengths.
- TypeError: Raised if evaluations is not a list of strings or risks is not a list of floats.
**Examples:**

```python
>>> calculate_strategy_scores(['Buy', 'Sell'], [0.1, 0.3])
[0.9, 0.7]
```

```python
>>> calculate_strategy_scores(['Long', 'Short', 'Hold'], [0.05, 0.2, 0.15])
[0.95, 0.8, 0.85]
```



---

## find_optimal_strategy_index

### Description
Returns the index of the highest score in a list of strategy scores.

### Conceptual Info

Determines which strategy has the highest score among a list of computed strategy scores.

### Docstring

**Summary:** Return the index of the maximum score in a list of strategy scores, with error handling for invalid input.

**Parameters:**

- scores (List[float]): A non-empty list of numerical scores for each strategy.
**Returns:** int - The zero-based index of the strategy with the highest score.

**Raises:**

- ValueError: If the scores list is empty.
- TypeError: If the scores parameter is not a list or contains non-numeric elements.
**Examples:**

```python
>>> find_optimal_strategy_index([0.5, 1.2, 0.9])
1
```

```python
>>> find_optimal_strategy_index([10, 20, 30])
2
```



---

## calculate_confidence_level

### Description
Calculates a confidence level for the selected strategy based on its score relative to the total score of all strategies.

### Conceptual Info

This shim provides a quantitative confidence estimate for the chosen trading strategy by normalising its score against the aggregate scores of all evaluated strategies, enabling downstream decision-making modules to assess the reliability of the selection.

### Docstring

**Summary:** Calculate the confidence level for a selected trading strategy.

**Parameters:**

- scores (List[float]): A list of numeric scores, each corresponding to a strategy evaluation.
- optimal_index (int): The index of the strategy identified as optimal within the `scores` list.
**Returns:** float - A confidence level between 0 and 1, computed as the score at `optimal_index` divided by the sum of all scores.

**Raises:**

- ValueError: If `scores` is empty or `optimal_index` is out of bounds.
- TypeError: If `scores` is not a list of floats or `optimal_index` is not an integer.
**Examples:**

```python
>>> scores = [0.8, 0.5, 0.7]
>>> conf = calculate_confidence_level(scores, 0)
>>> print(conf)
0.4
```

```python
>>> scores = [0.3, 0.6]
>>> conf = calculate_confidence_level(scores, 1)
>>> print(conf)
0.6666666666666666
```

