# _examine_customer_feedback - Complete PRD Documentation

## Overview
PRDs for nodes in the '_examine_customer_feedback' module.

## Table of Contents

- [parse_feedback_data](#parse_feedback_data)

- [validate_feedback_input](#validate_feedback_input)

- [analyze_sentiment_scores](#analyze_sentiment_scores)

- [calculate_overall_satisfaction](#calculate_overall_satisfaction)

- [filter_negative_feedback](#filter_negative_feedback)

- [filter_positive_feedback](#filter_positive_feedback)

- [extract_common_complaints](#extract_common_complaints)

- [extract_positive_themes](#extract_positive_themes)



---

## parse_feedback_data

### Description
Parses customer feedback data into a list of individual feedback comments.

### Conceptual Info

This shim node is responsible for taking raw customer feedback data as input and parsing it into a list of individual feedback comments, which can then be further analyzed.

### Docstring

**Summary:** Parses raw customer feedback data into a list of individual feedback comments.

**Parameters:**

- feedback_data (str): The raw customer feedback data that needs to be parsed.
**Returns:** List[str] - A list of individual customer feedback comments.

**Raises:**

- ValueError: If the input feedback data is not in the expected format.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> parse_feedback_data(feedback_data='Great service!\nExcellent product.')
['Great service!', 'Excellent product.']
```

```python
>>> parse_feedback_data(feedback_data='Poor service.\nBad product.')
['Poor service.', 'Bad product.']
```



---

## validate_feedback_input

### Description
Validates the input feedback data to ensure it is properly formatted and contains valid information.

### Conceptual Info

This node serves as a validation checkpoint for customer feedback data, ensuring that it meets certain criteria before being processed further in the system.

### Docstring

**Summary:** Validates the input feedback data to ensure it is not empty and contains valid information.

**Parameters:**

- feedback_data (str): The input feedback data to be validated.
**Returns:** str - A message indicating whether the feedback data is valid or not.

**Raises:**

- ValueError: When the input feedback data is empty or contains invalid information.
- TypeError: When the input type is not a string or a list of strings.
**Examples:**

```python
>>> validate_feedback_input(feedback_data='Good service')
'Feedback data is valid'
```

```python
>>> validate_feedback_input(feedback_data='')
ValueError: Feedback data is empty
```



---

## analyze_sentiment_scores

### Description
Analyzes the sentiment scores of a given list of customer feedback comments.

### Conceptual Info

This node analyzes customer feedback comments to determine their sentiment scores, which are then used to assess overall customer satisfaction.

### Docstring

**Summary:** Analyzes the sentiment of customer feedback comments and returns a list of sentiment scores.

**Parameters:**

- feedback_list (List[str]): A list of customer feedback comments to be analyzed.
**Returns:** List[float] - A list of sentiment scores between 0 and 1, where 0 represents very negative sentiment and 1 represents very positive sentiment.

**Raises:**

- ValueError: If the input feedback_list is empty or contains non-string values.
- TypeError: If the input feedback_list is not a list.
**Examples:**

```python
>>> feedback_list = ['I loved the service!', 'The product was okay.', 'Terrible experience.']
>>> sentiment_scores = analyze_sentiment_scores(feedback_list=feedback_list)
[0.9, 0.5, 0.1]
```

```python
>>> feedback_list = ['Great product!', 'Average service.', 'Poor quality.']
>>> sentiment_scores = analyze_sentiment_scores(feedback_list=feedback_list)
[0.8, 0.4, 0.2]
```



---

## calculate_overall_satisfaction

### Description
Calculates the overall customer satisfaction score based on sentiment scores.

### Conceptual Info

This shim node is responsible for computing an overall satisfaction score from a list of sentiment scores derived from customer feedback.

### Docstring

**Summary:** Calculates the overall customer satisfaction score based on the provided sentiment scores.

**Parameters:**

- sentiment_scores (List[float]): A list of sentiment scores derived from customer feedback.
**Returns:** float - The overall customer satisfaction score calculated from the sentiment scores.

**Raises:**

- ValueError: If the input sentiment scores are empty or invalid.
- TypeError: If the input sentiment scores are not a list of floats.
**Examples:**

```python
>>> sentiment_scores = [0.8, 0.9, 0.7]
>>> overall_satisfaction = calculate_overall_satisfaction(sentiment_scores=sentiment_scores)
0.8
```

```python
>>> sentiment_scores = [0.5, 0.6, 0.4]
>>> overall_satisfaction = calculate_overall_satisfaction(sentiment_scores=sentiment_scores)
0.5
```



---

## filter_negative_feedback

### Description
Filters negative customer feedback from a list based on sentiment scores.

### Conceptual Info

This shim function filters negative customer feedback from a list based on sentiment scores, playing a crucial role in analyzing customer satisfaction.

### Docstring

**Summary:** Filters negative customer feedback based on sentiment scores.

**Parameters:**

- feedback_list (str): A string representation of a list of customer feedback comments.
- sentiment_scores (str): A string representation of a list of sentiment scores corresponding to the feedback comments.
**Returns:** List[str] - A list of negative customer feedback comments.

**Raises:**

- ValueError: When the input lists are not of the same length or when the sentiment scores are not valid.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> feedback_list = '["Great product!", "Terrible service.", "Average experience."]'
>>> sentiment_scores = '[0.8, -0.7, 0.1]'
>>> filter_negative_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
["Terrible service."]
```

```python
>>> feedback_list = '["Love the product!", "Hate the service.", "Okay experience."]'
>>> sentiment_scores = '[0.9, -0.8, 0.2]'
>>> filter_negative_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
["Hate the service."]
```



---

## filter_positive_feedback

### Description
Filters customer feedback to identify positive comments based on sentiment scores.

### Conceptual Info

This shim function filters customer feedback to extract positive comments by analyzing the provided sentiment scores, playing a crucial role in understanding customer satisfaction.

### Docstring

**Summary:** Filters customer feedback to identify positive comments based on their sentiment scores.

**Parameters:**

- feedback_list (str): A JSON string representing a list of customer feedback comments.
- sentiment_scores (str): A JSON string representing a list of sentiment scores corresponding to the feedback comments.
**Returns:** List[str] - A list of customer feedback comments that are identified as positive based on their sentiment scores.

**Raises:**

- ValueError: If the input JSON strings are malformed or if the lengths of feedback_list and sentiment_scores do not match.
- TypeError: If the input types are not as expected (e.g., not JSON strings).
**Examples:**

```python
>>> import json
>>> feedback_list = json.dumps(['Great product!', 'Terrible service.', 'Excellent quality!'])
>>> sentiment_scores = json.dumps([0.8, 0.2, 0.9])
>>> filter_positive_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
['Great product!', 'Excellent quality!']
```

```python
>>> import json
>>> feedback_list = json.dumps(['Bad experience.', 'Good product.', 'Average service.'])
>>> sentiment_scores = json.dumps([0.1, 0.7, 0.5])
>>> filter_positive_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
['Good product.']
```



---

## extract_common_complaints

### Description
Extracts common complaints from a list of negative customer feedback.

### Conceptual Info

This node is responsible for analyzing negative customer feedback to identify recurring complaints, which are then used to inform customer satisfaction metrics.

### Docstring

**Summary:** Extracts common complaints from negative customer feedback.

**Parameters:**

- negative_feedback (List[str]): List of negative customer feedback comments.
**Returns:** List[str] - List of common complaints extracted from the negative feedback.

**Raises:**

- ValueError: If the input negative feedback is not a list of strings.
- TypeError: If the input type is not a list.
**Examples:**

```python
>>> negative_feedback = ['The product is too expensive.', 'The service was slow.', 'The product is too expensive.']
>>> complaints = extract_common_complaints(negative_feedback)
['The product is too expensive.']
```

```python
>>> negative_feedback = ['Poor customer support.', 'Product did not meet expectations.', 'Poor customer support.']
>>> complaints = extract_common_complaints(negative_feedback)
['Poor customer support.']
```



---

## extract_positive_themes

### Description
Extracts themes from positive customer feedback.

### Conceptual Info

This shim function is designed to extract and return themes from positive customer feedback, aiding in understanding customer satisfaction.

### Docstring

**Summary:** Extracts themes from the given positive customer feedback.

**Parameters:**

- positive_feedback (str): Positive customer feedback from which themes are to be extracted.
**Returns:** List[str] - A list of themes identified from the positive customer feedback.

**Raises:**

- ValueError: If the input positive feedback is empty or not a string.
- TypeError: If the input is not of type string.
**Examples:**

```python
>>> positive_feedback = 'The customer service was excellent.'
>>> themes = extract_positive_themes(positive_feedback)
>>> print(themes)
['customer service']
```

```python
>>> positive_feedback = 'The product quality was great.'
>>> themes = extract_positive_themes(positive_feedback)
>>> print(themes)
['product quality']
```

