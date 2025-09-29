# calculate_report_quality_score PRD

## Description
Calculates the quality score of a report based on confidence score, number of insights, and number of recommendations.


## Conceptual Info

This shim function is designed to assess the quality of a generated report by considering factors like confidence score, the number of insights, and recommendations provided.

## Docstring

### Summary
Calculates the report quality score based on input parameters.

### Parameters

- **confidence_score** (str): The confidence score of the report, expected to be a numerical value represented as a string.
- **num_insights** (str): The number of insights in the report, expected to be a numerical value represented as a string.
- **num_recommendations** (int): The number of recommendations in the report.

### Returns

float: A float value representing the calculated quality score of the report.

### Raises

- ValueError: If the input confidence score or number of insights cannot be converted to a numerical value.
- TypeError: If the input types are not as expected.

### Examples

```python
>>> confidence_score = '0.8'
>>> num_insights = '10'
>>> num_recommendations = 5
>>> report_score = calculate_report_quality_score(confidence_score=confidence_score, num_insights=num_insights, num_recommendations=num_recommendations)
0.85
```

```python
>>> confidence_score = '0.9'
>>> num_insights = '8'
>>> num_recommendations = 6
>>> report_score = calculate_report_quality_score(confidence_score=confidence_score, num_insights=num_insights, num_recommendations=num_recommendations)
0.88
```
