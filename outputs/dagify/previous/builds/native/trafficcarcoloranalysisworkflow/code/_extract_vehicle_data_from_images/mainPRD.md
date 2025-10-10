# _extract_vehicle_data_from_images - Complete PRD Documentation

## Overview
PRDs for nodes in the '_extract_vehicle_data_from_images' module.

## Table of Contents

- [validate_input_lists](#validate_input_lists)

- [verify_image_files_exist](#verify_image_files_exist)

- [load_and_validate_image](#load_and_validate_image)

- [detect_vehicles_in_image](#detect_vehicles_in_image)

- [extract_colors_from_vehicles](#extract_colors_from_vehicles)

- [get_color_names](#get_color_names)

- [get_confidence_values](#get_confidence_values)



---

## validate_input_lists

### Description
Validates that the input lists for image paths and timestamps are correctly formatted and consistent.

### Conceptual Info

This shim node validates the input lists for image paths and timestamps to ensure they are correctly formatted and consistent, which is crucial for downstream processing.

### Docstring

**Summary:** Validates input lists for image paths and timestamps, checking for consistency and correct formatting.

**Parameters:**

- image_paths (str): A list of file paths to captured traffic images, expected to be in a string format that can be parsed into a list.
- image_timestamps (str): A list of timestamps for when each image was captured, expected to be in a string format that can be parsed into a list and in the same order as image_paths.
**Returns:** str - A message indicating whether the input lists are valid. Returns 'valid' if both lists are of the same length and correctly formatted, otherwise returns an error message.

**Raises:**

- ValueError: When the input lists are not of the same length or are not correctly formatted.
- TypeError: When the input types are not as expected (e.g., not strings that can be parsed into lists).
**Examples:**

```python
>>> validate_input_lists(image_paths='["path1", "path2"]', image_timestamps='["timestamp1", "timestamp2"]')
'valid'
```

```python
>>> validate_input_lists(image_paths='["path1", "path2"]', image_timestamps='["timestamp1"]')
'Error: Input lists are not of the same length.'
```



---

## verify_image_files_exist

### Description
Verifies that the specified image files exist.

### Conceptual Info

This shim function is designed to validate the existence of image files specified by their paths. It serves as a critical step in ensuring data integrity before further processing.

### Docstring

**Summary:** Verifies the existence of image files based on provided paths.

**Parameters:**

- image_paths (str): A string containing the paths to the image files to be verified, potentially comma-separated or in a specific format.
**Returns:** str - A string indicating the result of the verification process. The exact format may vary based on implementation requirements.

**Raises:**

- FileNotFoundError: When one or more of the specified image files do not exist.
- TypeError: If the input is not a string or does not contain valid file paths.
**Examples:**

```python
>>> verify_image_files_exist(image_paths='/path/to/image1.jpg,/path/to/image2.jpg')
'All image files exist.'
```

```python
>>> verify_image_files_exist(image_paths='/path/to/nonexistent.jpg')
'Error: One or more image files do not exist.'
```



---

## load_and_validate_image

### Description
Loads an image from a given file path and validates its integrity.

### Conceptual Info

This shim node is responsible for loading an image from a specified file path and validating its integrity before it is processed further in the pipeline.

### Docstring

**Summary:** Loads an image from a file path and validates it.

**Parameters:**

- image_path (str): The file path to the image that needs to be loaded and validated.
**Returns:** str - A string representation of the loaded and validated image data.

**Raises:**

- FileNotFoundError: If the image file at the specified path does not exist.
- ValueError: If the image file is corrupted or cannot be validated.
- TypeError: If the image_path is not a string.
**Examples:**

```python
>>> image_data = load_and_validate_image(image_path='path/to/valid/image.jpg')
'image_data_string'
```

```python
>>> load_and_validate_image(image_path='path/to/nonexistent/image.jpg')
FileNotFoundError: Image file not found at path/to/nonexistent/image.jpg
```



---

## detect_vehicles_in_image

### Description
Detects vehicles within a given image and returns the detection results.

### Conceptual Info

This shim function is designed to detect vehicles within an image. It takes image data as input and returns the detection results as a string.

### Docstring

**Summary:** Detects vehicles in the given image data and returns the results.

**Parameters:**

- image_data (str): The input image data as a string.
**Returns:** str - A string representation of the detected vehicles.

**Raises:**

- ValueError: If the input image data is invalid or corrupted.
- TypeError: If the input image data is not of type string.
**Examples:**

```python
>>> detect_vehicles_in_image(image_data='base64encodedimage')
'Detected 5 vehicles'
```

```python
>>> detect_vehicles_in_image(image_data='invalidimage')
ValueError: Invalid image data
```



---

## extract_colors_from_vehicles

### Description
Extracts colors from detected vehicles in an image.

### Conceptual Info

This shim node is responsible for extracting color information from detected vehicles in images, playing a crucial role in the vehicle's data extraction pipeline.

### Docstring

**Summary:** Extracts colors and their confidence scores from detected vehicles.

**Parameters:**

- detected_vehicles (str): A string representation of detected vehicles, potentially containing their image data or detection results.
**Returns:** str - A string containing the extracted colors and their confidence scores, formatted as a list or dictionary.

**Raises:**

- ValueError: If the input string is not properly formatted or if vehicle detection data is invalid.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> extract_colors_from_vehicles(detected_vehicles='vehicle_data')
'colors_and_scores'
```

```python
>>> extract_colors_from_vehicles(detected_vehicles='invalid_data')
ValueError: Invalid vehicle detection data format.
```



---

## get_color_names

### Description
Extracts color names from the provided color information and confidence scores.

### Conceptual Info

This shim node is responsible for taking color information and confidence scores as input and returning a list of color names.

### Docstring

**Summary:** Extracts color names from the provided color information and confidence scores.

**Parameters:**

- colors_and_scores (str): A string containing color information and confidence scores, formatted appropriately for processing.
**Returns:** List[str] - A list of color names extracted from the input color information.

**Raises:**

- ValueError: If the input string is not properly formatted or contains invalid color information.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> get_color_names(colors_and_scores='red:0.8,blue:0.2')
['red', 'blue']
```

```python
>>> get_color_names(colors_and_scores='green:0.9,yellow:0.1')
['green', 'yellow']
```



---

## get_confidence_values

### Description
Extracts confidence scores from a string containing color information and confidence scores.

### Conceptual Info

This shim function is designed to extract confidence scores from a given string that contains color information along with their corresponding confidence scores. It plays a crucial role in the vehicle data extraction pipeline by processing the output of the color extraction step.

### Docstring

**Summary:** Extracts confidence scores from a string containing color and confidence information.

**Parameters:**

- colors_and_scores (str): Input string containing color information along with their confidence scores, formatted in a way that can be parsed to extract confidence scores.
**Returns:** List[float] - A list of floating-point numbers representing the confidence scores for the detected colors.

**Raises:**

- ValueError: If the input string is not in the expected format or if confidence scores cannot be extracted.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> colors_and_scores = 'red:0.8,blue:0.9,green:0.7'
>>> confidence_scores = get_confidence_values(colors_and_scores)
[0.8, 0.9, 0.7]
```

```python
>>> colors_and_scores = 'yellow:0.95,black:0.85'
>>> confidence_scores = get_confidence_values(colors_and_scores)
[0.95, 0.85]
```

