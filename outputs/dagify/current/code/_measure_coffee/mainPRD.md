# _measure_coffee - Complete PRD Documentation

## Overview
PRDs for nodes in the '_measure_coffee' module.

## Table of Contents

- [extract_cup_count_from_input](#extract_cup_count_from_input)

- [extract_grounds_type_from_input](#extract_grounds_type_from_input)

- [validate_cup_count](#validate_cup_count)

- [validate_grounds_type](#validate_grounds_type)

- [calculate_grounds_amount](#calculate_grounds_amount)

- [verify_measurement_accuracy](#verify_measurement_accuracy)



---

## extract_cup_count_from_input

### Description
Extracts the desired cup count from a general input string or keyword arguments for coffee brewing.

### Conceptual Info

This shim isolates the logic for parsing a coffee cup count from free‑form input or keyword arguments, ensuring consistent downstream consumption of the desired number of cups.

### Docstring

**Summary:** Parse an integer cup count from a general input string or optional keyword arguments for coffee brewing.

**Parameters:**

- general_input (str): Free‑form string that may contain a numeric cup count, e.g., "Please brew 2 cups".
- kwargs (dict): Optional keyword arguments; if a key named 'cup_count' is present, its value is used directly.
**Returns:** int - The integer number of cups extracted from the input.

**Raises:**

- ValueError: Raised when no numeric cup count can be found in the input and no valid 'cup_count' is supplied in kwargs.
- TypeError: Raised when 'general_input' is not a string or 'kwargs' values are not convertible to int.
**Examples:**

```python
>>> extract_cup_count_from_input('Please brew 2 cups')
2
```

```python
>>> extract_cup_count_from_input('Just 5 cups', cup_count=5)
5
```



---

## extract_grounds_type_from_input

### Description
Extracts the coffee grounds type from the input string and optional kwargs.

### Conceptual Info

This shim isolates the logic needed to determine the coffee grounds type from user‑provided text or keyword arguments, enabling the coffee measurement workflow to use a consistent and validated grounds type value.

### Docstring

**Summary:** Extracts the coffee grounds type from a general input string and optional keyword arguments.

**Parameters:**

- general_input (str): Free‑form text containing information about the desired coffee grounds and cup count.
- kwargs (str): Optional JSON or key/value string that may directly specify the grounds_type.
**Returns:** str - A lowercase string identifying the coffee grounds type (e.g., "medium grind" or "dark roast").

**Raises:**

- ValueError: Raised when no recognizable grounds type can be extracted from either `kwargs` or `general_input`.
- TypeError: Raised if either `general_input` or `kwargs` is not of type `str`.
**Examples:**

```python
>>> extract_grounds_type_from_input("I need 2 cups with medium grind", "")
"medium grind"
```

```python
>>> extract_grounds_type_from_input("Use dark roast for 3 cups", "grounds_type=dark roast")
"dark roast"
```



---

## validate_cup_count

### Description
Validates that the desired cup count is a positive integer and returns a confirmation message.

### Conceptual Info

This shim ensures the cup count provided for brewing coffee is valid, preventing downstream errors in the measurement process.

### Docstring

**Summary:** Checks that the desired cup count is a positive integer and returns a confirmation string.

**Parameters:**

- desired_cup_count (int): Number of coffee cups intended to brew. Must be a positive integer.
**Returns:** str - A confirmation message indicating the cup count is valid.

**Raises:**

- ValueError: If desired_cup_count is less than or equal to zero.
- TypeError: If desired_cup_count is not an integer.
**Examples:**

```python
>>> validate_cup_count(5)
'Cup count 5 validated successfully.'
```

```python
>>> validate_cup_count(-3)
ValueError: Cup count must be a positive integer.
```



---

## validate_grounds_type

### Description
Validates the provided coffee grounds type string against a predefined set of allowed ground types, returning a confirmation string or raising an error if invalid.

### Conceptual Info

This shim function ensures that the grounds_type supplied by the user or previous node is among the supported coffee ground types. It serves as a guardrail before any calculations that depend on the ground type are performed.

### Docstring

**Summary:** Checks whether the supplied grounds_type string is one of the accepted coffee ground types and returns a confirmation message or raises an error.

**Parameters:**

- grounds_type (str): The coffee grounds type to be validated (e.g., 'medium grind', 'dark roast').
**Returns:** str - A string confirming the validity of the grounds_type, e.g., "medium grind is valid."

**Raises:**

- ValueError: Raised when the grounds_type is not among the supported types.
- TypeError: Raised when the grounds_type argument is not a string.
**Examples:**

```python
>>> validate_grounds_type('medium grind')
"medium grind is valid."
```

```python
>>> validate_grounds_type('super fine')
"ValueError: Unsupported grounds type 'super fine'"
```



---

## calculate_grounds_amount

### Description
Calculates the required amount of coffee grounds in grams based on desired cup count and grounds type.

### Conceptual Info

This shim computes the precise quantity of coffee grounds required for a specified number of cups and grounds type, enabling downstream processes such as measuring and validation to operate with accurate data.

### Docstring

**Summary:** Compute the grams of coffee grounds needed for a given cup count and grounds type.

**Parameters:**

- desired_cup_count (int): Number of cups to brew; must be a positive integer.
- grounds_type (str): Coffee grounds type (e.g., 'medium', 'dark', 'light') that determines the grams-per-cup ratio.
**Returns:** float - Total grams of coffee grounds required.

**Raises:**

- ValueError: Raised when desired_cup_count is not a positive integer or grounds_type is unsupported.
- TypeError: Raised when inputs are of incorrect types.
**Examples:**

```python
>>> calculate_grounds_amount(desired_cup_count=4, grounds_type='medium')
10.0
```

```python
>>> calculate_grounds_amount(desired_cup_count=2, grounds_type='dark')
6.0
```



---

## verify_measurement_accuracy

### Description
Verifies that the measured amount of coffee grounds matches the desired cup count within acceptable tolerance.

### Conceptual Info

This shim function is responsible for determining if the amount of coffee grounds measured in grams is suitable for brewing the requested number of cups. It applies a tolerance rule to allow for small variations in measurement and returns a boolean flag that the calling workflow uses to confirm the validity of the measurement step.

### Docstring

**Summary:** Verifies that the measured coffee grounds amount aligns with the desired number of cups, allowing for a predefined tolerance.

**Parameters:**

- ground_amount_grams (float): The measured weight of coffee grounds in grams.
- desired_cup_count (int): The number of coffee cups the user intends to brew.
**Returns:** bool - True if the measured amount is within the acceptable tolerance for the desired cup count; otherwise False.

**Raises:**

- ValueError: If either ground_amount_grams or desired_cup_count is non‑positive.
- TypeError: If the input types do not match the expected float and int signatures.
**Examples:**

```python
>>> verify_measurement_accuracy(ground_amount_grams=12.0, desired_cup_count=2)
True
```

```python
>>> verify_measurement_accuracy(ground_amount_grams=10.0, desired_cup_count=2)
False
```

