# gather_wcfb_data PRD

## Description
Gather data necessary for WCFB analysis


## Conceptual Info

This node gathers relevant data for WCFB analysis from various sources.

## Docstring

### Summary
Gathers data necessary for WCFB analysis from business operations, customer feedback, and market trends.

### Returns

Tuple[str, List[str], List[float]]: A tuple containing business operations data, customer feedback data, and market trends data.

### Raises

- DataCollectionError: If there's an issue collecting data from any of the sources.

### Examples

```python
>>> gather_wcfb_data()
('Business operations data', ['Customer feedback 1', 'Customer feedback 2'], [1.2, 3.4, 5.6])
```

```python
>>> business_ops_data, customer_feedback, market_trends = gather_wcfb_data()
business_ops_data: 'Business operations data'
customer_feedback: ['Customer feedback 1', 'Customer feedback 2']
market_trends: [1.2, 3.4, 5.6]
```
