# _produce_sports_analysis_report - Complete PRD Documentation

## Overview
PRDs for nodes in the '_produce_sports_analysis_report' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [generate_executive_summary](#generate_executive_summary)

- [compile_detailed_findings](#compile_detailed_findings)

- [format_actionable_recommendations](#format_actionable_recommendations)

- [calculate_report_quality_score](#calculate_report_quality_score)



---

## validate_input_data

### Description
Validates the input data for type and structure conformity.

### Conceptual Info

This shim node is responsible for validating the input data received from the generate_insights_and_recommendations node to ensure it conforms to the expected structure and types before being processed further.

### Docstring

**Summary:** Validates the input data for type and structure conformity, returning a dictionary if valid.

**Parameters:**

- input_data (str): The input data to be validated, expected to be of type GenerateInsightsAndRecommendationsOutput.
**Returns:** str - A dictionary representation of the validated input data.

**Raises:**

- ValueError: When the input data fails validation checks.
- TypeError: When the input data type is not as expected.
**Examples:**

```python
>>> from pydantic import BaseModel, Field
>>> from typing import List
>>> class GenerateInsightsAndRecommendationsOutput(BaseModel):
...     insights: List[str] = Field(..., description='List of insights derived from the analysis')
...     recommendations: List[str] = Field(..., description='List of recommendations for improvement')
...     confidence_score: float = Field(..., description='Score indicating confidence in the recommendations')
>>> input_data = GenerateInsightsAndRecommendationsOutput(insights=['insight1'], recommendations=['rec1'], confidence_score=0.8)
>>> validate_input_data(input_data=input_data.json())
{'insights': ['insight1'], 'recommendations': ['rec1'], 'confidence_score': 0.8}
```



---

## generate_executive_summary

### Description
Generates a concise executive summary based on provided insights, recommendations, and confidence score.

### Conceptual Info

This shim node is responsible for condensing complex analysis results into a brief executive summary that highlights key findings and recommendations.

### Docstring

**Summary:** Generates an executive summary based on insights, recommendations, and a confidence score.

**Parameters:**

- insights (str): A string representation of insights derived from the analysis.
- recommendations (str): A string representation of recommendations for improvement.
- confidence_score (str): A string representation of the confidence score in the recommendations.
**Returns:** str - A concise executive summary that encapsulates key findings and recommendations.

**Raises:**

- ValueError: If the input parameters are empty or malformed.
- TypeError: If the input parameters are not of the expected type.
**Examples:**

```python
>>> generate_executive_summary(insights='The team needs improvement in strategy.', recommendations='Adopt a new game plan.', confidence_score='0.8')
'The analysis shows that the team needs improvement in strategy with high confidence. It is recommended to adopt a new game plan.'
```

```python
>>> generate_executive_summary(insights='Player performance is below average.', recommendations='Enhance training programs.', confidence_score='0.7')
'The analysis indicates that player performance is below average. It is recommended to enhance training programs with moderate confidence.'
```



---

## compile_detailed_findings

### Description
Compiles a list of detailed findings based on the provided insights and confidence score.

### Conceptual Info

This shim function compiles detailed findings from the provided insights and confidence score, playing a crucial role in generating a comprehensive sports analysis report.

### Docstring

**Summary:** Compiles a list of detailed findings based on the insights and confidence score provided as input.

**Parameters:**

- insights (str): A string containing insights derived from the analysis, expected to be in a format that can be processed by this function.
- confidence_score (str): A string representing the confidence score in the recommendations, which will be used to determine the reliability of the insights.
**Returns:** List[str] - A list of strings representing the detailed findings compiled from the insights and confidence score.

**Raises:**

- ValueError: If the insights or confidence score is not in the expected format or is missing required information.
- TypeError: If the input types are not as expected (e.g., insights or confidence_score are not strings).
**Examples:**

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



---

## format_actionable_recommendations

### Description
Formats the given recommendations into a list of actionable recommendations.

### Conceptual Info

This shim function is responsible for taking a string of recommendations and formatting them into a list of actionable steps, which can be used in a sports analysis report.

### Docstring

**Summary:** Formats the input recommendations into a list of actionable recommendations.

**Parameters:**

- recommendations (str): A string containing recommendations that need to be formatted into actionable steps.
**Returns:** List[str] - A list of strings where each string is an actionable recommendation.

**Raises:**

- ValueError: If the input recommendations are empty or not a string.
- TypeError: If the input is not of type string.
**Examples:**

```python
>>> format_actionable_recommendations('Improve team communication,Increase training sessions')
['Improve team communication', 'Increase training sessions']
```

```python
>>> format_actionable_recommendations('Enhance player fitness')
['Enhance player fitness']
```



---

## calculate_report_quality_score

### Description
Calculates the quality score of a report based on confidence score, number of insights, and number of recommendations.

### Conceptual Info

This shim function is designed to assess the quality of a generated report by considering factors like confidence score, the number of insights, and recommendations provided.

### Docstring

**Summary:** Calculates the report quality score based on input parameters.

**Parameters:**

- confidence_score (str): The confidence score of the report, expected to be a numerical value represented as a string.
- num_insights (str): The number of insights in the report, expected to be a numerical value represented as a string.
- num_recommendations (int): The number of recommendations in the report.
**Returns:** float - A float value representing the calculated quality score of the report.

**Raises:**

- ValueError: If the input confidence score or number of insights cannot be converted to a numerical value.
- TypeError: If the input types are not as expected.
**Examples:**

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

