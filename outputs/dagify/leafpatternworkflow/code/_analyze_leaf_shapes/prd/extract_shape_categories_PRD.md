# extract_shape_categories PRD

## Description
Extracts shape categories from leaf images and their characteristics.


## Conceptual Info

This shim function is designed to extract shape categories from a list of leaf images and their corresponding characteristics. It plays a crucial role in the leaf shape analysis pipeline.

## Docstring

### Summary
Extract shape categories from leaf images and their characteristics.

### Parameters

- **images** (List[str]): List of image file names or URLs of leaves.
- **characteristics** (List[str]): List of characteristic descriptions for each leaf.

### Returns

List[str]: List of shape categories for the leaves.

### Raises

- ValueError: When the lengths of images and characteristics lists do not match.
- TypeError: When the input types are not as expected (e.g., not lists or not strings).

### Examples

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
