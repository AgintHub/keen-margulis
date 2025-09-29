# _invokeprayer - Complete PRD Documentation

## Overview
PRDs for nodes in the '_invokeprayer' module.

## Table of Contents

- [prepare_intention_text](#prepare_intention_text)

- [generate_prayer_invocation](#generate_prayer_invocation)

- [assess_prayer_connection](#assess_prayer_connection)



---

## prepare_intention_text

### Description
This shim node prepares the intention text for prayer by processing the given intention string.

### Conceptual Info

The prepare_intention_text shim plays a crucial role in the prayer invocation process by transforming the raw intention into a formatted text suitable for prayer.

### Docstring

**Summary:** Processes the given intention string to produce a formatted intention text for prayer.

**Parameters:**

- intention (str): The raw intention string that needs to be processed for prayer.
**Returns:** str - The processed intention text that is ready for use in prayer.

**Raises:**

- ValueError: If the input intention is empty or cannot be processed.
- TypeError: If the input intention is not a string.
**Examples:**

```python
>>> prepare_intention_text('peace and harmony')
'May our hearts be filled with peace and harmony.'
```

```python
>>> prepare_intention_text('guidance for our journey')
'May we receive guidance for our journey.'
```



---

## generate_prayer_invocation

### Description
Generates a prayer invocation based on a given intention.

### Conceptual Info

This shim generates the actual words or invocation used in a prayer based on a prepared intention.

### Docstring

**Summary:** Generates a prayer invocation text based on the given intention.

**Parameters:**

- intention (str): The prepared intention or focus for the prayer.
**Returns:** str - The generated prayer invocation text.

**Raises:**

- ValueError: If the input intention is empty or not a string.
- TypeError: If the input intention is not of type string.
**Examples:**

```python
>>> generate_prayer_invocation(intention='peace and harmony')
'May we be blessed with peace and harmony.'
```

```python
>>> generate_prayer_invocation(intention='strength in times of need')
'May we find strength in times of need.'
```



---

## assess_prayer_connection

### Description
Evaluates the connection status or feeling during a prayer based on the invocation and readiness.

### Conceptual Info

This shim node assesses the connection status or feeling during a prayer based on the invocation and the readiness state of the person praying.

### Docstring

**Summary:** Assesses the connection status during a prayer based on the invocation and readiness state.

**Parameters:**

- invocation (str): The actual words or invocation used during the prayer.
- readiness (str): The readiness state of the person to pray, represented as a string ('True' or 'False').
**Returns:** str - The assessed connection status or feeling during the prayer, represented as a descriptive string.

**Raises:**

- ValueError: If the readiness state is not 'True' or 'False'.
- TypeError: If the invocation is not a string or if the readiness is not a boolean value represented as a string.
**Examples:**

```python
>>> assess_prayer_connection(invocation='Dear God, guide us.', readiness='True')
'A deep sense of connection.'
```

```python
>>> assess_prayer_connection(invocation='Hello, world!', readiness='False')
'No connection felt.'
```

