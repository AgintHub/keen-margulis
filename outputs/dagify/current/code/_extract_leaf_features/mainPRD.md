# _extract_leaf_features - Complete PRD Documentation

## Overview
PRDs for nodes in the '_extract_leaf_features' module.

## Table of Contents

- [validate_input_consistency](#validate_input_consistency)

- [preprocess_leaf_images](#preprocess_leaf_images)

- [extract_vein_patterns](#extract_vein_patterns)

- [extract_leaf_colors](#extract_leaf_colors)



---

## validate_input_consistency

### Description
Validates the consistency between leaf images and their characteristics.

### Conceptual Info

This shim node ensures that the leaf images and their characteristics are consistent, likely by checking if they have the same number of elements.

### Docstring

**Summary:** Validates the consistency between leaf images and characteristics.

**Parameters:**

- leaf_images (str): List of image file names or URLs of leaves.
- leaf_characteristics (str): List of characteristic descriptions for each leaf.
**Returns:** str - Output indicating whether the input is consistent, potentially returning 'True' or 'False' as a string.

**Raises:**

- ValueError: When the lengths of leaf_images and leaf_characteristics do not match.
- TypeError: When the input types are incorrect, such as non-string or non-list inputs.
**Examples:**

```python
>>> leaf_images = ['image1.jpg', 'image2.jpg']
>>> leaf_characteristics = ['characteristic1', 'characteristic2']
>>> validate_input_consistency(leaf_images=leaf_images, leaf_characteristics=leaf_characteristics)
'True'
```

```python
>>> leaf_images = ['image1.jpg', 'image2.jpg']
>>> leaf_characteristics = ['characteristic1']
>>> validate_input_consistency(leaf_images=leaf_images, leaf_characteristics=leaf_characteristics)
ValueError: 'Lengths of leaf_images and leaf_characteristics do not match.'
```



---

## preprocess_leaf_images

### Description
Preprocesses a list of leaf image file names or URLs for further analysis.

### Conceptual Info

This node preprocesses leaf images by potentially resizing, normalizing, or applying other necessary transformations to prepare them for feature extraction and analysis.

### Docstring

**Summary:** Preprocesses a list of leaf image file names or URLs.

**Parameters:**

- images (str): List of image file names or URLs to be preprocessed, separated by commas or in a list format.
**Returns:** List[str] - List of preprocessed image file names or URLs, potentially transformed for analysis.

**Raises:**

- ValueError: If the input list is empty or contains invalid image file names or URLs.
- TypeError: If the input is not a string or a list of strings.
**Examples:**

```python
>>> preprocess_leaf_images(images='image1.jpg,image2.jpg')
['preprocessed_image1.jpg', 'preprocessed_image2.jpg']
```

```python
>>> preprocess_leaf_images(images=['image1.jpg', 'image2.jpg'])
['preprocessed_image1.jpg', 'preprocessed_image2.jpg']
```



---

## extract_vein_patterns

### Description
Extracts vein patterns from leaf images based on their characteristics and shape categories.

### Conceptual Info

This shim function is designed to extract vein patterns from leaf images by analyzing their characteristics and shape categories. It serves as a placeholder for a more complex image processing and analysis functionality that will be implemented later.

### Docstring

**Summary:** Extracts vein patterns from leaf images based on their characteristics and shape categories.

**Parameters:**

- images (str): A string representing the input leaf images (file names or URLs).
- characteristics (str): A string describing the characteristics of the leaves.
- shape_categories (str): A string indicating the shape categories of the leaves.
**Returns:** List[str] - A list of strings describing the vein patterns extracted from the leaf images.

**Raises:**

- ValueError: If the input images, characteristics, or shape categories are invalid or inconsistent.
- TypeError: If the input types are not as expected (e.g., not strings).
**Examples:**

```python
>>> images = 'leaf_image1.jpg,leaf_image2.jpg'
>>> characteristics = 'green,oval'
>>> shape_categories = 'category1,category2'
>>> extract_vein_patterns(images, characteristics, shape_categories)
['vein_pattern1', 'vein_pattern2']
```

```python
>>> images = 'image1.png,image2.png'
>>> characteristics = 'red,heart-shaped'
>>> shape_categories = 'categoryA,categoryB'
>>> extract_vein_patterns(images, characteristics, shape_categories)
['patternA', 'patternB']
```



---

## extract_leaf_colors

### Description
Extracts colors from leaf images based on their characteristics.

### Conceptual Info

This shim function is designed to extract color information from leaf images based on their provided characteristics. It plays a crucial role in the leaf analysis pipeline by providing color data that can be used for further analysis or classification.

### Docstring

**Summary:** Extracts leaf colors from images based on their characteristics.

**Parameters:**

- images (str): A string containing image file names or URLs of leaves, expected to be preprocessed.
- characteristics (str): A string containing characteristic descriptions for each leaf, used to guide the color extraction.
**Returns:** List[str] - A list of colors observed in the leaves, where each color is represented as a string.

**Raises:**

- ValueError: If the input images or characteristics are invalid or inconsistent.
- TypeError: If the input types are not as expected (e.g., not strings).
**Examples:**

```python
>>> extract_leaf_colors(images='leaf_images.jpg', characteristics='green, oval, smooth edges')
['green', 'light green']
```

```python
>>> extract_leaf_colors(images='leaf1.jpg,leaf2.jpg', characteristics='variegated, lobed')
['green, white', 'deep green']
```

