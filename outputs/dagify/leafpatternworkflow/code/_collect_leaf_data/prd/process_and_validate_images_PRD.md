# process_and_validate_images PRD

## Description
Processes and validates a list of image file names or URLs.


## Conceptual Info

This shim node is responsible for processing and validating a list of image file names or URLs, ensuring they are in a suitable format for further analysis.

## Docstring

### Summary
Processes and validates image file names or URLs, returning a list of valid images.

### Parameters

- **images** (str): A string containing image file names or URLs to be processed, separated by commas or another delimiter.

### Returns

List[str]: A list of processed and validated image file names or URLs.

### Raises

- ValueError: If the input string is empty or contains invalid image file names or URLs.
- TypeError: If the input is not a string.

### Examples

```python
>>> process_and_validate_images(images='image1.jpg,image2.png')
['image1.jpg', 'image2.png']
```

```python
>>> process_and_validate_images(images='invalid_image')
[]
```
