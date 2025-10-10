# validate_input_lengths PRD

## Description
Validates that the lengths of input images and characteristics are consistent.


## Conceptual Info

This shim node validates the consistency of input data lengths for further processing.

## Docstring

### Summary
Validates that the input lists of images and characteristics have the same length.

### Parameters

- **images** (List[str]): List of image file names or URLs.
- **characteristics** (List[str]): List of characteristic descriptions for each image.

### Returns

str: Output message indicating whether the input lengths are valid.

### Raises

- ValueError: When the lengths of images and characteristics do not match.

### Examples

```python
>>> validate_input_lengths(images=['image1.jpg', 'image2.jpg'], characteristics=['char1', 'char2'])
'Input lengths are valid.'
```

```python
>>> validate_input_lengths(images=['image1.jpg'], characteristics=['char1', 'char2'])
ValueError: 'Lengths of images and characteristics do not match.'
```
