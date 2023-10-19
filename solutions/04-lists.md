---
jupyter:
  jupytext:
    formats: ipynb,md
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.9.13
---

# Storing Multiple Values in Lists
## Objectives
* Explain what a list is.
* Create and index lists of simple values.
* Change the values of individual elements
* Append values to an existing list
* Reorder and slice list elements
* Create and manipulate nested lists

***

Python list documentation: https://docs.python.org/3/tutoridatastructures.html#more-on-lists

# Python lists
Unlike numpy arrays, lists are built into the language so we do not have to load a library to use them. We create a list by putting values inside square brackets and separating the values with commas:
```python tags=["empty"]
odds = []         # empty list
odds = [1,3,5,7]  # a list with 4 elements
print(odds)       # a list is represented with []
```

As previously, index `0` represents the first element, and index `3` the fourth element.
```python
print('first element:', odds[0])
print('last element:', odds[3])
print('"-1" element:', odds[-1])
```
Yes, yes we can use negative numbers as indices in Python. When we do so, the index `-1` gives us the last element in the list, `-2` the second to last, and so on. Because of this, `odds[3]` and `odds[-1]` point to the same element here.

Lists as strings (list of characters) can be sliced. It uses the `[from:to:step]` notation where the first number represents the first element to fetch, the second number represents the index of the last element (not taken), and the step is an optional parameter with a default value of 1.
 
Recall that slicing is not an inclusive range: `[from:to[`

|elements| 1  | 3  | 5  | 7  |
|--------|----|----|----|----|
|indexes | 0  | 1  | 2  | 3  |

```python tags=["empty"]
print(odds[0:2])
```
```python
print(odds[1:])
```
```python tags=["empty"]
print(odds[:3])
```
```python
print(odds[::2])
```

We can also start from the end with the negative indexing:

|elements| 1  | 3  | 5  | 7  |
|--------|----|----|----|----|
|indexes | 0  | 1  | 2  | 3  |
|indexes | -4 | -3 | -2 | -1 |


```python tags=["empty"]
print(odds[-1])
```
```python
print(odds[-3:-1])
```
```python
print(odds[:-3])
```
```python tags=["empty"]
print(odds[-4:])
```

Can we print the list in reverse, with two different way?
```python
print(odds[::-1])
```
```python
print(odds[4:-5:-1])
```

There is one very important difference between list and string, we can change the values in a list, but we cannot change individual characters in a string. For example:
```python
names = ['Curie', 'Darwing', 'Turing']  # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin'  # correct the name
print('final value of names:', names)
```
works but the following does not:
```python tags=["raises-exception"]
name = 'Darwin'
name[0] = 'd'
```

We've seen previously that strings are *immutable* and lists are *mutable*.

We also need to be careful when modifying data in-place. What happens if two variables refer to the same list?
```python tags=["empty"]
other = odds # other and odds point the same data in memory
```
Did we really make a copy?
```python
other[0] = 99
print(other)
print(odds)
```
No since both variable from the assignation points to the same data in memory.
In order to effectively copy, we construct another list from the original one:
```python
other = odds.copy() # or list(odds)
odds[0] = 1
print(other)
print(odds)
```

A `list` also has methods. We can use `append` to add an element at the end of the list. Or see `help(list)` to get the list of available methods.
```python
odds.append(9)
print(odds)
```
We can also remove an element from the list.
```python
odds.pop(-1) # Removes the last element
print(odds)
odds.remove(1) # Removes the element `1` (not the first element)
print(odds)
```

The elements of a list can also be sorted. These methods (`append`, `remove`, `sort`, ...) work in-place (modifying directly the object).
```python
odds.sort()
print(odds)
odds.reverse()
print(odds)
```
Or we could use the built-in function `sorted`. In this case, the original data structure is not touched, a copy is returned.
```python
sorted_odds = sorted(odds)
print(sorted_odds)
print(odds)
```

Python lists can contain elements of different types. For example:
```python
chromosomes = ["X", "Y", 2, 3, 4]
name = "Drosophila melanogaster"
```

We've seen that lists are indexed and can be sliced using `[start:end:step]` notation as with strings.
```python
print(name[0:10])
print(name[11:])
print(chromosomes[0:2])
print(chromosomes[-1])
```

We can even add a list as an element:
```python tags=["empty"]
odds.append(chromosomes)
print(odds)
```

And what happens if we addition two lists?
```python
print(odds + chromosomes)
```
Lists can be concatenated together with the `+` operator.

# Exercises

#### 1. Indexing
Given the list `nums = [1, 111, 2, 3, 5, 8, 13, 2, 34, 55, 89]`, print on the same line, the second, sixth and last element.

Answer:`111 8 89`
```python
nums = [1, 111, 2, 3, 5, 8, 13, 2, 34, 55, 89]
```
```python tags=["empty"]
# print second, sixth and last element
print(nums[1], nums[5], nums[-1])
```

# Key Points
* `[value1, value2, value3, ...]` creates a list.
* Lists can contain any Python object, including lists (i.e., list of lists).
* Lists are indexed and sliced with square brackets (e.g., `list[0]` and `list[2:9]`), in the same way as strings and arrays.
* Lists are *mutable* (i.e., their values can be changed in place).
* Strings are *immutable* (i.e., the characters in them cannot be changed).
