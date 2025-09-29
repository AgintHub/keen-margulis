# compile_detailed_findings PRD

## Description
Compiles a list of detailed findings based on the provided insights and confidence score.


## Conceptual Info

This shim function compiles detailed findings from the provided insights and confidence score, playing a crucial role in generating a comprehensive sports analysis report.

## Docstring

### Summary
Compiles a list of detailed findings based on the insights and confidence score provided as input.

### Parameters

- **insights** (str): A string containing insights derived from the analysis, expected to be in a format that can be processed by this function.
- **confidence_score** (str): A string representing the confidence score in the recommendations, which will be used to determine the reliability of the insights.

### Returns

List[str]: A list of strings representing the detailed findings compiled from the insights and confidence score.

### Raises

- ValueError: If the insights or confidence score is not in the expected format or is missing required information.
- TypeError: If the input types are not as expected (e.g., insights or confidence_score are not strings).

### Examples

```python
>>> insights = 'Insight 1, Insight 2, Insight 3'
>>> confidence_score = '0.8'
>>> detailed_findings = compile_detailed_findings(insights, confidence_score)
['Detailed Finding 1', 'Detailed Finding 2', 'Detailed Finding 3']
```

```python
>>> insights = 'Another insight, And another one'
>>> confidence_score = '0.9'
>>> detailed_findings = compile_detailed_findings(insights, confidence_score)
['Detailed Finding A', 'Detailed Finding B']
```
