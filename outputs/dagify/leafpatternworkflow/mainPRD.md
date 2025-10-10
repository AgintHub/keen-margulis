# leafpatternworkflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'leafpatternworkflow' module.

## Table of Contents

- [analyze_leaf_shapes](#analyze_leaf_shapes)

- [collect_leaf_data](#collect_leaf_data)

- [extract_leaf_features](#extract_leaf_features)

- [generate_leaf_pattern_insights](#generate_leaf_pattern_insights)



---

## analyze_leaf_shapes

### Description
Analyze the shapes of leaves and categorize them

### Conceptual Info

This node analyzes the shapes of leaves based on the data collected by the 'collect_leaf_data' node and categorizes them into different types.

### Docstring

**Summary:** Analyze leaf shapes and categorize them into different types based on the collected leaf data.

**Parameters:**

- leaf_images (List[str]): List of image file names or URLs of leaves collected by the 'collect_leaf_data' node.
- leaf_characteristics (List[str]): List of characteristic descriptions for each leaf collected by the 'collect_leaf_data' node.
**Returns:** Tuple[List[str], List[int]] - A tuple containing a list of shape categories for the leaves and a list of counts of leaves in each shape category.

**Raises:**

- ValueError: If the input lists 'leaf_images' and 'leaf_characteristics' are of different lengths.
**Examples:**

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



---

## collect_leaf_data

### Description
Gather data on various leaf patterns including images and characteristics

### Conceptual Info

The 'collect_leaf_data' node is responsible for gathering images and characteristics of various leaf patterns.

### Docstring

**Summary:** Collects leaf images and their characteristics, returning lists of image file names/URLs and characteristic descriptions.

**Returns:** Tuple[List[str], List[str]] - A tuple containing a list of leaf image file names/URLs and a list of characteristic descriptions for each leaf.

**Raises:**

- Exception: If there's an issue collecting or processing the leaf data.
**Examples:**

```python
>>> leaf_images, leaf_characteristics = collect_leaf_data()
(['leaf1.jpg', 'leaf2.jpg'], ['Ovate with smooth edges', 'Lanceolate with serrated edges'])
```

```python
>>> leaf_data = collect_leaf_data(); print(leaf_data[0]); print(leaf_data[1])
['leaf1.jpg', 'leaf2.jpg']
['Ovate with smooth edges', 'Lanceolate with serrated edges']
```



---

## extract_leaf_features

### Description
Extract features from leaf images such as vein patterns and colors

### Conceptual Info

This node processes leaf images to extract features such as vein patterns and colors, building upon the data collected and shape analysis from previous nodes.

### Docstring

**Summary:** Extracts features from leaf images, including vein patterns and colors, using data from collect_leaf_data and analyze_leaf_shapes.

**Parameters:**

- leaf_images (List[str]): List of image file names or URLs of leaves from collect_leaf_data.
- leaf_characteristics (List[str]): List of characteristic descriptions for each leaf from collect_leaf_data.
- leaf_shape_categories (List[str]): List of shape categories for the leaves from analyze_leaf_shapes.
- shape_category_counts (List[int]): Counts of leaves in each shape category from analyze_leaf_shapes.
**Returns:** Tuple[List[str], List[str]] - A tuple containing a list of descriptions of vein patterns for each leaf and a list of colors observed in the leaves.

**Raises:**

- ValueError: If leaf_images or leaf_characteristics are empty or mismatched in length.
- TypeError: If the input lists are not of the expected types.
**Examples:**

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



---

## generate_leaf_pattern_insights

### Description
Generate insights on leaf patterns based on the extracted features

### Conceptual Info

This node analyzes the features extracted from leaf images to identify common patterns and variations, providing a summary of the insights gained.

### Docstring

**Summary:** Generate insights on leaf patterns based on extracted features such as vein patterns and colors.

**Parameters:**

- leaf_vein_patterns (List[str]): Descriptions of vein patterns for each leaf, extracted by the parent node 'extract_leaf_features'
- leaf_colors (List[str]): List of colors observed in the leaves, extracted by the parent node 'extract_leaf_features'
**Returns:** Tuple[List[str], List[str], str] - A tuple containing a list of common leaf patterns, a list of leaf pattern variations, and a summary of key insights on leaf patterns.

**Raises:**

- ValueError: If the input lists 'leaf_vein_patterns' or 'leaf_colors' are empty or not provided.
**Examples:**

```python
>>> leaf_vein_patterns = ['parallel', 'net-like', 'parallel']
>>> leaf_colors = ['green', 'green', 'yellow']
>>> common_leaf_patterns, leaf_pattern_variations, insights_summary = generate_leaf_pattern_insights(leaf_vein_patterns, leaf_colors)
(['parallel', 'net-like'], ['green', 'yellow'], 'Key insights: Parallel vein patterns are common, with variations in color.')
```

```python
>>> leaf_vein_patterns = ['net-like', 'net-like', 'net-like']
>>> leaf_colors = ['green', 'variegated', 'green']
>>> common_leaf_patterns, leaf_pattern_variations, insights_summary = generate_leaf_pattern_insights(leaf_vein_patterns, leaf_colors)
(['net-like'], ['variegated'], 'Key insights: Net-like vein patterns are predominant, with some variation in leaf color.')
```

