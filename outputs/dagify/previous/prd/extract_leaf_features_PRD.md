# extract_leaf_features PRD

## Description
Extract features from leaf images such as vein patterns and colors


## Conceptual Info

This node processes leaf images to extract features such as vein patterns and colors, building upon the data collected and shape analysis from previous nodes.

## Docstring

### Summary
Extracts features from leaf images, including vein patterns and colors, using data from collect_leaf_data and analyze_leaf_shapes.

### Parameters

- **leaf_images** (List[str]): List of image file names or URLs of leaves from collect_leaf_data.
- **leaf_characteristics** (List[str]): List of characteristic descriptions for each leaf from collect_leaf_data.
- **leaf_shape_categories** (List[str]): List of shape categories for the leaves from analyze_leaf_shapes.
- **shape_category_counts** (List[int]): Counts of leaves in each shape category from analyze_leaf_shapes.

### Returns

Tuple[List[str], List[str]]: A tuple containing a list of descriptions of vein patterns for each leaf and a list of colors observed in the leaves.

### Raises

- ValueError: If leaf_images or leaf_characteristics are empty or mismatched in length.
- TypeError: If the input lists are not of the expected types.

### Examples

```python
>>> leaf_images = ['leaf1.jpg', 'leaf2.jpg']
>>> leaf_characteristics = ['characteristic1', 'characteristic2']
>>> leaf_shape_categories = ['shape1', 'shape2']
>>> shape_category_counts = [1, 2]
>>> result = extract_leaf_features(leaf_images, leaf_characteristics, leaf_shape_categories, shape_category_counts)
(['vein pattern 1', 'vein pattern 2'], ['color1', 'color2'])
```

```python
>>> leaf_images = ['leaf3.jpg']
>>> leaf_characteristics = ['characteristic3']
>>> leaf_shape_categories = ['shape3']
>>> shape_category_counts = [3]
>>> result = extract_leaf_features(leaf_images, leaf_characteristics, leaf_shape_categories, shape_category_counts)
(['vein pattern 3'], ['color3'])
```
