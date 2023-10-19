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

# Python Fundamentals
## Objectives
* Assign values to variables.
* Know the existence of different types of data

***

Any Python interpreter can be used as a calculator:
```python
10 + 20
```

```python tags=["empty"]
2 * 3
```

This is great but not very interesting. To do anything useful with data, we need to assign its value to a variable. 

## Variables
Variables are nothing but reserved memory locations to store values. This means that when you create a
variable you reserve some space in memory.

In Python, we can assign a value to a variable, using the equals sign `=`. For example, we can track the weight of a patient who weighs `60` kilograms by assigning the value `60` to a variable named `weight_kg`:

```python tags=["empty"]
weight_kg = 60
```

In Python, variable names:

* can include letters, digits, and underscores
* cannot start with a digit
* are case sensitive.
This means that, for example:

`weight0` is a valid variable name, whereas `0weight` is not
`weight` and `Weight` are different variables
```python tags=["raises-exception"]
weight0 = 0  # valid
0weight = 1  # invalid
```

## Types of data

Python has many types of data. Three common ones are:

* integer numbers (`int`)
* floating point numbers (`float`)
* strings (`str`)

You may also come across:
- None
- List
- Boolean
- Dictionary
- Set
- Tuples

Some types of date are **immutable** objects, meaning that the state of the object cannot be modified after it has been created. The other types are therefore called **mutables** objects. The immutable property improve readability and runtime efficiency.

| Data type       | Immutable  |
|-----------------|------------|
|   list          | ❌         |
|   set           | ❌         |
|   dictionary    | ❌         |
|   None          | ✅         |
|   bool          | ✅         |
|   int           | ✅         |
|   float         | ✅         |
|   complex       | ✅         |
|   strings       | ✅         |
|   tuple         | ✅         |


In the example above, the variable `weight_kg` has an integer value of `60`. If we want to more precisely track the weight of our patient, we can use a floating point value by executing:
```python tags=["empty"]
weight_kg = 60.3
```

To create a string, we add single or double quotes around some text. To identify and track a patient throughout our study, we can assign each person a unique identifier by storing it in a string:
```python
patient_id = '001'
```

## Using Variables in Python
Once we have data stored with variable names, we can make use of it in calculations. We may want to store our patient’s weight in pounds as well as kilograms:
```python tags=["empty"]
weight_lb = 2.2 * weight_kg
```

We might decide to add a prefix to our patient identifier. We can add another string value by concatenating two strings:
```python
patient_id = 'inflam_' + patient_id
```

## Built-in functions
A function is:
> A named group of instructions that is executed when the function’s name is used in the code. Occurrence of a function name in the code is a function call. Functions may process input arguments and return the result back. Functions may also be used for logically grouping together pieces of code. In such cases, they don’t need to return any meaningful value and can be written without the return statement completely. Such functions return a special value `None`, which is a way of saying “nothing”.
[Reference](https://swcarpentry.github.io/python-novice-inflammation/reference.html#function)

Python has several built-in functions. In order to display information to the screen, we can use the `print` function:
```python tags=["empty"]
print(weight_lb)
print(patient_id)
```

When we want to make use of a function, referred to as calling the function, we follow its name by parentheses. The parentheses are important: if you leave them off, the function doesn’t actually run! Sometimes you will include values or variables inside the parentheses for the function to use. In the case of `print`, we use the parentheses to tell the function what value we want to display. We will learn more about how functions work and how to create our own in a later chapter.

We can display multiple things at once using only one print call:
```python
print(patient_id, 'weight in kilograms:', weight_kg)
```

We can also embed another function call, for example if we printed the value's data type:
```python
print(type(60.3))
print(type(patient_id))
```

We can also do arithmetic with variables:
```python
print('weight in pounds:', 2.2 * weight_kg)
```

The value of `weight_kg` was not altered:
```python
print(weight_kg)
```

In order to change the value of the `weight_kg` variable, we have to *assign* a new value:
```python
weight_kg = 65.0
print('weight in kilograms is now:', weight_kg)
```

# Exercices
#### 1. What values do the variables `mass` and `age` have after each of the following statements?
```python
mass = 47.5
age = 122
mass = mass * 2.0
age = age - 20
```

#### 2. What are the data types of the following variables?
```python
planet = 'Earth'
apples = 5
distance = 10.5
```

***
# Key points
* Basic data types in Python include integers, strings, and floating-point numbers.
* Use `variable = value` to assign a value to a variable in order to record it in memory.
* Variables are created on demand whenever a value is assigned to them.
* Use `print(something)` to display the value of `something`.
* Built-in functions are always available to use.
