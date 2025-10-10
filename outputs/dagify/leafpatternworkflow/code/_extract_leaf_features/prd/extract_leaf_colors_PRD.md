# extract_leaf_colors PRD

## Description
Extracts colors from leaf images based on their characteristics.


## Conceptual Info

This shim function is designed to extract color information from leaf images based on their provided characteristics. It plays a crucial role in the leaf analysis pipeline by providing color data that can be used for further analysis or classification.

## Docstring

### Summary
Extracts leaf colors from images based on their characteristics.

### Parameters

- **images** (str): A string containing image file names or URLs of leaves, expected to be preprocessed.
- **characteristics** (str): A string containing characteristic descriptions for each leaf, used to guide the color extraction.

### Returns

List[str]: A list of colors observed in the leaves, where each color is represented as a string.

### Raises

- ValueError: If the input images or characteristics are invalid or inconsistent.
- TypeError: If the input types are not as expected (e.g., not strings).

### Examples

```python
>>> extract_leaf_colors(images='leaf_images.jpg', characteristics='green, oval, smooth edges')
['green', 'light green']
```

```python
>>> extract_leaf_colors(images='leaf1.jpg,leaf2.jpg', characteristics='variegated, lobed')
['green, white', 'deep green']
```
