# identify_tradable_assets PRD

## Description
Determine the specific assets or instruments to be traded for the selected strategy.


## Conceptual Info

The node takes the list of asset classes proposed by the chosen trading strategy and verifies/filters them to produce the final tradable assets list and a count. It ensures that the strategy’s asset classes are valid and prepares the data for downstream execution planning.

## Docstring

### Summary
Identify the tradable assets for a chosen trading strategy.

### Parameters

- **asset_classes** (List[str]): Asset classes or instruments suggested by the chosen trading strategy.

### Returns

Dict[str, Any]: A dictionary containing `tradable_assets` (List[str]) and `asset_count` (int).

### Raises

- ValueError: If `asset_classes` is empty or not provided.

### Examples

```python
>>> def identify_tradable_assets(asset_classes: List[str]) -> Dict[str, Any]:
...     if not asset_classes:
...         raise ValueError("No asset classes provided.")
...     return {"tradable_assets": asset_classes, "asset_count": len(asset_classes)}
>>> # Example 1
>>> result = identify_tradable_assets(["Equities", "Forex", "Futures"])
>>> print(result)
{'tradable_assets': ['Equities', 'Forex', 'Futures'], 'asset_count': 3}
```

```python
>>> # Example 2
>>> result = identify_tradable_assets(["Commodities"])
>>> print(result)
{'tradable_assets': ['Commodities'], 'asset_count': 1}
```
