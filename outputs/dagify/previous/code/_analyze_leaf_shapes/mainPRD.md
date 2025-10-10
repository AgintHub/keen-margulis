# _analyze_leaf_shapes - Complete PRD Documentation

## Overview
PRDs for nodes in the '_analyze_leaf_shapes' module.

## Table of Contents

- [validate_input_lengths](#validate_input_lengths)

- [preprocess_leaf_images](#preprocess_leaf_images)

- [normalize_characteristics](#normalize_characteristics)

- [extract_shape_categories](#extract_shape_categories)

- [count_shape_categories](#count_shape_categories)



---

## validate_input_lengths

### Description
Validates that the lengths of input images and characteristics are consistent.

### Conceptual Info

This shim node validates the consistency of input data lengths for further processing.

### Docstring

**Summary:** Validates that the input lists of images and characteristics have the same length.

**Parameters:**

- images (List[str]): List of image file names or URLs.
- characteristics (List[str]): List of characteristic descriptions for each image.
**Returns:** str - Output message indicating whether the input lengths are valid.

**Raises:**

- ValueError: When the lengths of images and characteristics do not match.
**Examples:**

```python
>>> validate_input_lengths(images=['image1.jpg', 'image2.jpg'], characteristics=['char1', 'char2'])
'Input lengths are valid.'
```

```python
>>> validate_input_lengths(images=['image1.jpg'], characteristics=['char1', 'char2'])
ValueError: 'Lengths of images and characteristics do not match.'
```



---

## preprocess_leaf_images

### Description
A shim function to preprocess leaf images for further analysis.

### Conceptual Info

This shim function preprocesses leaf images, preparing them for analysis by potentially resizing, normalizing, or applying other necessary transformations.

### Docstring

**Summary:** Preprocesses a list of leaf images represented as file names or URLs.

**Parameters:**

- images (str): A string representing a list of image file names or URLs to be preprocessed.
**Returns:** List[str] - A list of strings representing the preprocessed image file names or URLs.

**Raises:**

- ValueError: If the input string is not a valid representation of a list of image file names or URLs.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> preprocess_leaf_images(images='["image1.jpg", "image2.jpg"]')
['preprocessed_image1.jpg', 'preprocessed_image2.jpg']
```

```python
>>> preprocess_leaf_images(images='["leaf1.png", "leaf2.png"]')
['preprocessed_leaf1.png', 'preprocessed_leaf2.png']
```



---

## normalize_characteristics

### Description
Normalizes a list of leaf characteristics into a standardized format.

### Conceptual Info

This shim function takes a string of leaf characteristics, normalizes it, and returns a list of normalized characteristic descriptions.

### Docstring

**Summary:** Normalizes a string of leaf characteristics into a list of standardized format.

**Parameters:**

- characteristics (str): Input string containing leaf characteristics to be normalized
**Returns:** List[str] - List of normalized characteristic descriptions for each leaf

**Raises:**

- ValueError: When the input string is empty or contains invalid characters
- TypeError: When the input is not a string
**Examples:**

```python
>>> normalize_characteristics(characteristics='large, green, oval-shaped')
>>> normalize_characteristics(characteristics='small, yellow, heart-shaped')
['large', 'green', 'oval-shaped']
['small', 'yellow', 'heart-shaped']
```

```python
>>> normalize_characteristics(characteristics='')
[]
```



---

## extract_shape_categories

### Description
Extracts shape categories from leaf images and their characteristics.

### Conceptual Info

This shim function is designed to extract shape categories from a list of leaf images and their corresponding characteristics. It plays a crucial role in the leaf shape analysis pipeline.

### Docstring

**Summary:** Extract shape categories from leaf images and their characteristics.

**Parameters:**

- images (List[str]): List of image file names or URLs of leaves.
- characteristics (List[str]): List of characteristic descriptions for each leaf.
**Returns:** List[str] - List of shape categories for the leaves.

**Raises:**

- ValueError: When the lengths of images and characteristics lists do not match.
- TypeError: When the input types are not as expected (e.g., not lists or not strings).
**Examples:**

```python
>>> images = ['leaf1.jpg', 'leaf2.jpg']
>>> characteristics = ['oval', 'lanceolate']
>>> shape_categories = extract_shape_categories(images, characteristics)
['oval', 'lanceolate']
```

```python
>>> images = ['leaf3.jpg']
>>> characteristics = ['heart-shaped']
>>> shape_categories = extract_shape_categories(images, characteristics)
['heart-shaped']
```



---

## count_shape_categories

### Description
Counts the occurrences of each shape category in the given list of categories.

### Conceptual Info

This shim node is responsible for counting the occurrences of each shape category in a given list, playing a crucial role in analyzing leaf shapes.

### Docstring

**Summary:** Counts the occurrences of each shape category in the given list of categories.

**Parameters:**

- categories (str): A string representing the shape categories, expected to be a list or a string that can be parsed into a list of categories.
**Returns:** List[int] - A list of integers where each integer represents the count of a unique shape category in the input.

**Raises:**

- ValueError: If the input categories are not in an expected format or if there's an issue parsing the categories.
- TypeError: If the input categories are not of type str or if the parsed categories are not as expected.
**Examples:**

```python
>>> count_shape_categories(categories='category1,category2,category1')
[2, 1]
```

```python
>>> count_shape_categories(categories='oval, lance, oval, round')
[2, 1, 1]
```

