# create_top_performers_summary PRD

## Description
Creates a summary of top performers based on scorers, rebounders, and assisters.


## Conceptual Info

This shim function generates a summary of top performers in a team based on their performance in scoring, rebounding, and assisting.

## Docstring

### Summary
Creates a formatted summary of top performers from the provided lists of scorers, rebounders, and assisters.

### Parameters

- **scorers** (List[str]): List of top scorers in the team.
- **rebounders** (List[str]): List of top rebounders in the team.
- **assisters** (List[str]): List of top assisters in the team.

### Returns

str: A formatted summary including the names and roles of top performers.

### Raises

- TypeError: If any of the input parameters are not lists of strings.
- ValueError: If any of the input lists are empty.

### Examples

```python
>>> create_top_performers_summary(scorers=['Player1', 'Player2'], rebounders=['Player3', 'Player4'], assisters=['Player5', 'Player6'])
'Top scorers: Player1, Player2. Top rebounders: Player3, Player4. Top assisters: Player5, Player6.'
```

```python
>>> create_top_performers_summary(scorers=['John', 'Doe'], rebounders=['Jane', 'Doe'], assisters=['Bob', 'Smith'])
'Top scorers: John, Doe. Top rebounders: Jane, Doe. Top assisters: Bob, Smith.'
```
