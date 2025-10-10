# calculate_impact_strength PRD

## Description
Computes a numeric impact strength (0–1) for an economic factor based on its textual impact analysis.


## Conceptual Info

This shim evaluates the intensity of an economic factor's influence by converting qualitative analysis into a quantitative score.

## Docstring

### Summary
Calculate a numeric strength rating (0–1) for an economic factor based on its impact analysis.

### Parameters

- **factor_name** (str): Name of the economic factor to evaluate.
- **impact_analysis** (str): Textual description of how the factor impacted the historical context.

### Returns

float: A float between 0 and 1 representing the strength of the factor's impact.

### Raises

- ValueError: If either input is an empty string or missing.
- TypeError: If inputs are not of type str.

### Examples

```python
>>> strength = calculate_impact_strength(
...     factor_name='Inflation',
...     impact_analysis='High inflation led to widespread unemployment.'
>>> )
0.85
```

```python
>>> strength = calculate_impact_strength(
...     factor_name='Reform',
...     impact_analysis='Policy reform stabilized the economy.'
>>> )
0.6
```
