# analyze_social_influences PRD

## Description
Examine the social influences that contributed to the historical event or period.


## Conceptual Info

This node takes the social factors identified by its parent and assigns quantitative impact scores, counts them, and produces a narrative summary of their interaction in the context of the historical event.

## Docstring

### Summary
Analyze the social influences on a historical event, assigning impact scores and summarizing their combined effect.

### Parameters

- **input_social_factors** (List[str]): List of primary social factors returned by the parent node `identify_key_factors`.

### Returns

Dict[str, Any]: A dictionary containing the number of factors, the list of social factors, their impact scores, and a summary narrative.

### Raises

- ValueError: Raised when `input_social_factors` is empty or None.

### Examples

```python
>>> result = analyze_social_influences(["Women’s suffrage", "Urbanization"])
{"number_of_factors": 2, "social_factors": ["Women’s suffrage", "Urbanization"], "impact_scores": [0.8, 0.6], "summary": "Women’s suffrage and urbanization combined accelerated democratic reforms."}
```

```python
>>> result = analyze_social_influences(["Industrial labor strikes"])
{"number_of_factors": 1, "social_factors": ["Industrial labor strikes"], "impact_scores": [0.7], "summary": "Industrial labor strikes pressured governments to enact labor protections."}
```
