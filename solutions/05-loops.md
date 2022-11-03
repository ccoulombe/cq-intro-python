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

# Repeating Actions with Loops
## Objectives
* Explain what a `for` loop does.
* Correctly write `for` loops to repeat simple calculations.
* Trace changes to a loop variable as the loop runs.
* Trace changes to other variables as they are updated by a `for` loop.

***
An example task that we might want to repeat is accessing numbers in a list, which we will do by printing each number on a line of its own.
```python tags=["empty"]
odds = [1, 3, 5, 7]
```
In Python, a list is basically an ordered collection of elements, and every element has a unique number associated with it — its index. This means that we can access elements in a list using their indices. For example, we can get the first number in the list `odds`, by using `odds[0]`. One way to print each number is to use four print statements:
```python
print(odds[0])
print(odds[1])
print(odds[2])
print(odds[3])
```
But if the list changes...
```python tags=["raises-exception"]
odds = [1, 3, 5]
print(odds[0])
print(odds[1])
print(odds[2])
print(odds[3])
```
This is a bad approach for three reasons:

1. **Not scalable.** Imagine you need to print a list that has hundreds of elements. It might be easier to type them in manually.
2. **Difficult to maintain.** If we want to decorate each printed element with an asterisk or any other character, we would have to change four lines of code. While this might not be a problem for small lists, it would definitely be a problem for longer ones.
3. **Fragile.** If we use it with a list that has more elements than what we initially envisioned, it will only display part of the list’s elements. A shorter list, on the other hand, will cause an error because it will be trying to display elements of the list that do not exist.

Using a `for` loop to repeat an operation is a better approach:
```python tags=["empty"]
for num in odds:
    print(num)
```
and more robust, for instance if the list is longer:
```python tags=["empty"]
odds = [1, 3, 5, 7, 9, 11]
for num in odds:
    print(num)
```

The improved version is calling the print fonction for each element of the sequence. The general form of a loop is (note the indentation):
```
for element in sequence:
    do things using element
```

A representation of the example above is:

![image](images/loops_image_num.png)

The variable name can be anything, such as `banana`, but it is preferable to choose meaningful names:
```python
odds = [1, 3, 5, 7, 9, 11]
for banana in odds:
    print(banana)
```

Here’s another loop that repeatedly updates a variable. In this example note the indentation of the `print` statement, indicating that it's outside the loop, therefore excuted after:
```python
length = 0
names = ['Curie', 'Darwin', 'Turing']
for value in names:
    length = length + 1
print('There are', length, 'names in the list.')
```

Note that a loop variable is a variable that is being used to record progress in a loop. It still exists after the loop is over, and we can re-use variables previously defined as loop variables:
```python
name = 'Rosalind'
for name in ['Curie', 'Darwin', 'Turing']:
    print(name)
print('after the loop, name is', name)
```

A common operation is finding the length of an object. Python has a built-in function named `len`:
```python tags=["empty"]
print(len([0, 1, 2, 3]))
```
Another built-in function named `range` can be very useful with `for` loops. This function creates a sequence of integers.
- If one parameter is given, `range` creates a sequence of that length, starting at zero and incrementing by step of 1.
- If two parameters are given, `range` starts at the first and ends just before the second, incrementing by step of 1.
- If range is given 3 parameters, it starts at the first one, ends just before the second one, and increments by the third one.
```python
print(len(range(6)))     # 0,1,2,3,4,5
print(len(range(2,6)))   # 2,3,4,5
print(len(range(3,6,2))) # 3, 5
```

# Exercises
#### 1. Range
Write a `for` loop, using `range` that prints numbers from `3` to `21` with a step of `3`:
```python tags=["empty"]
for i in range(3, 22, 3):
    print(i)
```

#### 2. Summing a list
Write a loop that calculates the sum of elements in a list by adding each element and printing the final value.
`[124, 402, 36]` prints `562`.
```python tags=["empty"]
summed = 0
for num in [124, 402, 36]:
    summed = summed + num
print(summed)
```

***
# Key Points
* Use `for variable in sequence` to process the elements of a sequence one at a time.
* The body of a `for` loop must be indented.
* Use `len(thing)` to determine the length of something that contains other values.
