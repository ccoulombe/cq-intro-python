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

# Making Choices
## Objectives
* Write conditional statements including `if`, `elif`, and `else` branches.
* Correctly evaluate expressions containing `and` and `or`.

***

# Conditionals
In life we make choices, it is not different in Python. We can express conditions with the `if` statement that, in turn, can be expressed by two values `True` or `False`, which are called `Booleans`.

Documentation: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
```python tags=["empty"]
True
```
```python tags=["empty"]
False
```
We can also construct `Booleans` from other values. For example, `False` and `True` are the equivalent of `0` and `1` respectively. 

By default, objects are considered true, except the following built-in objects:
- `None` and `False`
- zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`
- empty collections and sequences: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`.
```python
print(bool(1)) 
print(bool(0))
print(bool('Hello'))  # Anything other than zero length string is True
```
We can also express conditions with relationnal operators:
```python
print(1 == 1)
print(2 != 1)
print(1 < 0)
print(1 > 2)
print(1 >= 1)
print(1 <= 2)
```

We can also express multiple conditions with the logical operators `and` or `or`. 

- `and` conditions will return `True` when every expression is `True` and will stop evaluating on `False`. 

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

- `or` conditions will return `True` when at least one of the expression is `True`, otherwise `False`

| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

And you can group expressions with `()`.
```python
print(1 == 1 and 1 != 2)
```

What will the following expression returns?
```python tags=["empty"]
True and True
```
```python
True and False and True
```
```python tags=["empty"]
False or True
```
```python
True or False and True
```
```python
(False or False) and True
```

With an `if` statement, we can decide on actions to do based on conditions:
```python tags=["empty"]
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')
```
The above can be visulize with:

![image](../images/python-flowchart-conditional.png)

We can also tests several conditions using an `elif` which means _else if_.
```python tags=["raises-exception"]
num = None
if num > 100:
    print('greater')
elif num is None:
    print('num is None')
else:
    print('not greater')
print('done')
```
As you can see the order of the conditions are very important as some relational operators cannot be used with `None`!
```python
num = None
if num is None:
    print('num is None')
elif num > 100:
    print('greater')
else:
    print('not greater')
print('done')
```

# Exercises
#### 1. Smaller Than
Write the code to print the elements from `0` to `10` that are smaller than `4` using a `for` loop.

Answer:
```
0 
1 
2
3
```
```python tags=["empty"]
for i in range(10):
    if i < 4:
        print(i)
```

#### 2. Buckets
For the list `nums = [1, 111, 2, 3, 5, 8, 13, 2, 34, 55, 89]`, sort the elements into three lists, then print the lists on one line:
- smaller than `5`
- greater than `100`
- others

Answer: `[1, 2, 3, 2] [111] [5, 8, 13, 34, 55, 89]`

```python
nums = [1, 111, 2, 3, 5, 8, 13, 2, 34, 55, 89]
```
```python tags=["empty"]
s = []
g = []
o = []

for n in nums:
    if n < 5:
        s.append(n)
    elif n > 100:
        g.append(n)
    else:
        o.append(n)
print(s,g,o)
```

***
# Key Points
* Use if condition to start a conditional statement, elif condition to provide additional tests, and else to provide a default.
* The bodies of the branches of conditional statements must be indented.
* Use `==` to test for equality.
* X and Y is only true if both X and Y are true.
* X or Y is true if either X or Y, or both, are true.
* Zero, the empty string, and the empty list are considered false; all other numbers, strings, and lists are considered true.
* True and False represent truth values.
