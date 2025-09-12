# extract_release_dates PRD

## Description
Extracts a list of release dates for each album from the provided discography metadata.


## Conceptual Info

This shim parses discography metadata to produce a chronological list of album release dates.

## Docstring

### Summary
Extracts release dates for each album from the provided discography metadata JSON.

### Parameters

- **discography_data** (str): JSON string representing the discography metadata containing album names and release dates.

### Returns

List[str]: A list of album release dates extracted from the input data.

### Raises

- ValueError: Raised when the input JSON is invalid or missing required fields.

### Examples

```python
>>> import json
>>> # Sample discography data
>>> sample_json = json.dumps({
...     "albums": [
...         {"name": "Album1", "release_date": "2020-01-01"},
...         {"name": "Album2", "release_date": "2021-01-01"}
...     ]
>>> })
>>> release_dates = extract_release_dates(sample_json)
>>> print(release_dates)
["2020-01-01", "2021-01-01"]
```
