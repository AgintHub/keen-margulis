# save_images_to_storage PRD

## Description
Saves image data to specified storage location with given file format.


## Conceptual Info

This shim function is responsible for taking image data and saving it to a specified directory in a given file format. It acts as a bridge between image capture and storage systems.

## Docstring

### Summary
Saves image data to storage, returning a list of saved file paths.

### Parameters

- **image_data** (str): The image data to be saved, expected to be in bytes format but passed as str
- **output_directory** (str): The directory path where images will be saved
- **file_format** (str): The file format for the images (e.g., 'jpg', 'png')

### Returns

List[str]: A list of file paths where the images were saved

### Raises

- ValueError: If the output directory is invalid or inaccessible
- TypeError: If image_data is not of type str or if output_directory or file_format are not strings

### Examples

```python
>>> save_images_to_storage(image_data='image1_bytes', output_directory='/tmp/images', file_format='jpg')
>>> save_images_to_storage(image_data='image2_bytes', output_directory='/tmp/images', file_format='png')
['/tmp/images/image1.jpg', '/tmp/images/image2.png']
```

```python
>>> save_images_to_storage(image_data=['image_bytes1', 'image_bytes2'], output_directory='/tmp/images', file_format='jpg')
['/tmp/images/image1.jpg', '/tmp/images/image2.jpg']
```
