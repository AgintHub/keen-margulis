# _collect_leaf_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_collect_leaf_data' module.

## Table of Contents

- [identify_leaf_data_sources](#identify_leaf_data_sources)

- [gather_raw_leaf_data](#gather_raw_leaf_data)

- [extract_leaf_images](#extract_leaf_images)

- [process_and_validate_images](#process_and_validate_images)

- [extract_leaf_characteristics](#extract_leaf_characteristics)

- [validate_characteristics](#validate_characteristics)



---

## identify_leaf_data_sources

### Description
This shim identifies leaf data sources from a given input context and returns them as a list of strings.

### Conceptual Info

This shim plays a crucial role in the leaf data collection pipeline by identifying relevant data sources based on the provided input context.

### Docstring

**Summary:** Identifies leaf data sources from a given input context.

**Parameters:**

- input_context (str): The input context that contains information necessary for identifying leaf data sources.
**Returns:** List[str] - A list of strings representing the paths or identifiers of the identified leaf data sources.

**Raises:**

- ValueError: If the input context is empty or does not contain valid information for identifying data sources.
- TypeError: If the input context is not a string.
**Examples:**

```python
>>> identify_leaf_data_sources(input_context='leaf_data_folder')
['leaf_data_folder/image1.jpg', 'leaf_data_folder/image2.jpg']
```

```python
>>> identify_leaf_data_sources(input_context='https://example.com/leaf_data')
['https://example.com/leaf_data/image1.jpg', 'https://example.com/leaf_data/image2.jpg']
```



---

## gather_raw_leaf_data

### Description
A shim function that collects raw leaf data from specified sources.

### Conceptual Info

This shim function serves as a placeholder for collecting raw leaf data from various sources. It is part of a larger system that processes leaf images and characteristics.

### Docstring

**Summary:** Collects raw leaf data from the specified sources and returns it as a list of dictionaries.

**Parameters:**

- sources (str): A string representing the data sources from which to gather raw leaf data.
**Returns:** List[dict] - A list of dictionaries where each dictionary contains raw data for a leaf.

**Raises:**

- ValueError: If the input 'sources' is not a valid string or is empty.
- TypeError: If the input 'sources' is not of type string.
**Examples:**

```python
>>> raw_leaf_data = gather_raw_leaf_data(sources='leaf_data_sources')
>>> print(raw_leaf_data)
[{'leaf_id': 1, 'image_url': 'url1', 'characteristics': 'desc1'}, {'leaf_id': 2, 'image_url': 'url2', 'characteristics': 'desc2'}]
```

```python
>>> try:
...     gather_raw_leaf_data(sources='')
>>> except ValueError as e:
...     print(e)
Input 'sources' cannot be empty.
```



---

## extract_leaf_images

### Description
Extracts image file names or URLs from raw leaf data.

### Conceptual Info

This shim function is responsible for extracting image file names or URLs from the raw leaf data provided as input.

### Docstring

**Summary:** Extracts image file names or URLs from raw leaf data.

**Parameters:**

- raw_data (str): Raw data containing leaf information in a string format, potentially JSON encoded.
**Returns:** List[str] - List of image file names or URLs extracted from the raw data.

**Raises:**

- ValueError: If the raw_data is not a valid string or if it's not properly formatted.
- TypeError: If the input raw_data is not of type str.
**Examples:**

```python
>>> raw_data = '[{"image": "leaf1.jpg"}, {"image": "leaf2.jpg"}]'
>>> extract_leaf_images(raw_data=raw_data)
['leaf1.jpg', 'leaf2.jpg']
```

```python
>>> raw_data = '[{"other": "data"}, {"image": "leaf3.jpg"}]'
>>> extract_leaf_images(raw_data=raw_data)
['leaf3.jpg']
```



---

## process_and_validate_images

### Description
Processes and validates a list of image file names or URLs.

### Conceptual Info

This shim node is responsible for processing and validating a list of image file names or URLs, ensuring they are in a suitable format for further analysis.

### Docstring

**Summary:** Processes and validates image file names or URLs, returning a list of valid images.

**Parameters:**

- images (str): A string containing image file names or URLs to be processed, separated by commas or another delimiter.
**Returns:** List[str] - A list of processed and validated image file names or URLs.

**Raises:**

- ValueError: If the input string is empty or contains invalid image file names or URLs.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> process_and_validate_images(images='image1.jpg,image2.png')
['image1.jpg', 'image2.png']
```

```python
>>> process_and_validate_images(images='invalid_image')
[]
```



---

## extract_leaf_characteristics

### Description
Extracts characteristic descriptions from raw leaf data.

### Conceptual Info

This shim extracts characteristic information from raw leaf data, serving as an intermediary step in leaf data processing.

### Docstring

**Summary:** Extracts characteristic descriptions from raw leaf data.

**Parameters:**

- raw_data (str): Raw data containing leaf information in a string format.
**Returns:** List[str] - List of characteristic descriptions for each leaf.

**Raises:**

- ValueError: When the input raw data is not in the expected format.
- TypeError: When the input type is not a string.
**Examples:**

```python
>>> extract_leaf_characteristics(raw_data='{"leaf1": "green", "leaf2": "yellow"}')
['green', 'yellow']
```

```python
>>> extract_leaf_characteristics(raw_data='{"leaf1": "oval", "leaf2": "heart-shaped"}')
['oval', 'heart-shaped']
```



---

## validate_characteristics

### Description
Validates the characteristics of leaf data extracted from raw leaf information.

### Conceptual Info

This shim node is responsible for validating the characteristics extracted from raw leaf data, ensuring they meet specific criteria or standards.

### Docstring

**Summary:** Validates a list of characteristic descriptions for leaves based on predefined criteria.

**Parameters:**

- characteristics (str): A string containing characteristic data to be validated, potentially in a serialized or encoded format.
**Returns:** List[str] - A list of validated characteristic descriptions.

**Raises:**

- ValueError: When the input characteristic data is malformed or cannot be validated.
- TypeError: When the input type is not a string or cannot be processed.
**Examples:**

```python
>>> characteristics_data = 'shape:oval,color:green,size:large'
>>> validated_characteristics = validate_characteristics(characteristics=characteristics_data)
['shape:oval', 'color:green', 'size:large']
```

```python
>>> characteristics_data = 'shape:invalid,color:green,size:large'
>>> validated_characteristics = validate_characteristics(characteristics=characteristics_data)
['color:green', 'size:large']  # Assuming 'shape:invalid' is filtered out during validation
```

