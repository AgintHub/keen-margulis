# analyze_leaf_shapes PRD

## Description
Analyze the shapes of leaves and categorize them


## Conceptual Info

This node analyzes the shapes of leaves based on the data collected by the 'collect_leaf_data' node and categorizes them into different types.

## Docstring

### Summary
Analyze leaf shapes and categorize them into different types based on the collected leaf data.

### Parameters

- **leaf_images** (List[str]): List of image file names or URLs of leaves collected by the 'collect_leaf_data' node.
- **leaf_characteristics** (List[str]): List of characteristic descriptions for each leaf collected by the 'collect_leaf_data' node.

### Returns

Tuple[List[str], List[int]]: A tuple containing a list of shape categories for the leaves and a list of counts of leaves in each shape category.

### Raises

- ValueError: If the input lists 'leaf_images' and 'leaf_characteristics' are of different lengths.

### Examples

```python
>>> leaf_images = ['leaf1.jpg', 'leaf2.jpg', 'leaf3.jpg']
>>> leaf_characteristics = ['oval', 'lanceolate', 'cordate']
>>> leaf_shape_categories, shape_category_counts = analyze_leaf_shapes(leaf_images, leaf_characteristics)
(['oval', 'lanceolate', 'cordate'], [1, 1, 1])
```

```python
>>> leaf_images = ['leaf4.jpg', 'leaf5.jpg']
>>> leaf_characteristics = ['elliptical', 'lanceolate']
>>> leaf_shape_categories, shape_category_counts = analyze_leaf_shapes(leaf_images, leaf_characteristics)
(['elliptical', 'lanceolate'], [1, 1])
```
