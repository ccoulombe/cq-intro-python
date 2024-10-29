---
jupytext:
  cell_metadata_filter: autoscroll,scrolled,tags
  formats: ipynb,md:myst
  notebook_metadata_filter: all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
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

# Analyzing Patient Data
## Objectives
* Explain what a library is and what libraries are used for.
* Import a Python library and use the functions it contains.
* Read tabular data from a file into a program.
* Select individual values and subsections from data.
* Perform operations on arrays of data.
***

Numpy documentation: https://numpy.org/doc/stable/reference/index.html

# Loading data into Python

In order to load data, we need to access (import in Python terminology) a library named [`numpy`](https://numpy.org/doc/stable/). We first need to import it:

```{code-cell} ipython3
:tags: [empty]

import numpy
```

Importing a library makes its functionalities available for us to use.

Once we’ve imported the library, we can ask the library to read our data file for us:

```{code-cell} ipython3
numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
```

Our call to `numpy.loadtxt` read our file but didn’t save the data in memory. The result is returned and outputted to the screen.
In order to save the data in memory, we need to assign the returned data to a variable, like we assigned a value to a variable:

```{code-cell} ipython3
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
```

If we want to have a look at the data, we can print the variable's value:

```{code-cell} ipython3
:tags: [empty]

print(data)
```

We can now manipulate it. Let's look at its type:

```{code-cell} ipython3
print(type(data))
```

We can also find out the type of the data contained in the array:

```{code-cell} ipython3
:tags: [empty]

print(data.dtype)
```

Or we can see the array's shape:

```{code-cell} ipython3
:tags: [empty]

print(data.shape)
```

To print one element from the array, we must provide an index in square brackets (`[]`) after the variable name.
The inflammation data has two dimensions, so we will need to use two indices to refer to one specific value:

```{code-cell} ipython3
:tags: [empty]

print('middle value in data:', data[30, 20])
```

The expression `data[30, 20]` accesses the element at row `30` and column `20`.

+++

And what would be the indices for the first element?:

```{code-cell} ipython3
print('first value in data:', data[0, 0])
```

Programming languages like Fortran, MATLAB and R start counting at 1 because that’s what human beings have done for thousands of years. Languages in the C family (including C++, Java, Perl, and Python) count from 0 because it represents an offset from the first value in the array (the second value is offset by one index from the first value). As a result, if we have an M×N array in Python, its indices go from 0 to M-1 on the first axis and 0 to N-1 on the second.
![image](images/python-zero-index.svg)

# Slicing data
Above we selected a single element, but we can select whole sections or slice. For instance, we can select the first ten days (columns) for the first four patients (rows) with:

```{code-cell} ipython3
:tags: [empty]

print(data[0:4, 0:10])
```

The slicing is not an inclusive range: `[from:to[`, for example:

|elements| 1  | 2  | 3  | 4  |
|--------|----|----|----|----|
|indexes | 0  | 1  | 2  | 3  |

+++

We don’t have to start slices at 0:

```{code-cell} ipython3
print(data[5:10, 0:10])
```

We can also omit the upper or lower boundary of the slice:

```{code-cell} ipython3
small = data[:3, 36:]
print('small is:')
print(small)
```

# Analyzing data
Numpy library contains several useful functions to work with arrays. For example, we can calculate `data`'s [mean](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html) value:

```{code-cell} ipython3
:tags: [empty]

print(numpy.mean(data))
```

We could also calculate the [maximum](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html), [minimal](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html) and [standard deviation](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.std.html) of the data:

```{code-cell} ipython3
:tags: [empty]

print('maximum inflammation:', numpy.max(data))
print('minimum inflammation:', numpy.min(data))
print('standard deviation:', numpy.std(data))
```

At any given point, we can learn more about a function by using some help magic 🪄 or tab completion.
For instance, we could look the documentation for the `std` function:

```{code-cell} ipython3
:scrolled: true

help(numpy.std)
```

When analyzing data we often want to look at variations in statistical values, such as the maximum inflammation per patient or the average inflammation per day. One way to do this is to create a new temporary array of the data we want, then ask it to do the calculation. 
How would we assign the data of the first patient to a variable `patient_0`?:

```{code-cell} ipython3
:tags: [empty]

patient_0 = data[0, :] # 0 on the first axis (rows), everything on the second (columns)
```

Then calculate the maximum inflammation for this patient:

```{code-cell} ipython3
print(numpy.max(patient_0))
```

We don’t actually need to store the row in a variable of its own. We can call the function directly:

```{code-cell} ipython3
print('maximum inflammation for patient 3:', numpy.max(data[2, :]))
```

Operations can be done on rows or columns, which we call _axis_.
![image](images/python-operations-across-axes.png)

With _axis_, we can get the maximum inflammation for each patient over all days (left) or the average for each day (right).

For instance, calculate the average for each day. To which graphic does this correspond?

```{code-cell} ipython3
:tags: [empty]

print(numpy.mean(data, axis=0))
```

When we look at the shape of our array, we get:

```{code-cell} ipython3
print(numpy.mean(data, axis=0).shape)
```

`(40,)` which means we have a 1 dimension vector (`Nx1`) of 40 elements. This is the average inflammation per day for all patients.
And if we'd calculate the average inflammation per patient accross all days?:

```{code-cell} ipython3
print(numpy.mean(data, axis=1))
```

# Exercices
#### 1. Slicing

```{code-cell} ipython3
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
```

Print the first patient, first inflammation value:

```{code-cell} ipython3
:tags: [empty]

print(data[0,0])
```

Print the second patient, 5th inflammation value:

```{code-cell} ipython3
:tags: [empty]

print(data[1,4])
```

Print the first three patients, their first four inflammation values:

```{code-cell} ipython3
:tags: [empty]

data[0:3, 0:4]
```

***
# Key points

* Import a library into a program using `import libraryname`.
* Use the `numpy` library to work with arrays in Python.
* The expression `array.shape` gives the shape of an array.
* Use `array[x, y]` to select a single element from a 2D numpy array.
* Array indices start at `0`, not `1`.
* Use `low:high` to specify a slice that includes the indices from `low` to `high-1`.
* Use `# some kind of explanation to add comments to programs.
* Use `numpy.mean(array)`, `numpy.max(array)`, and `numpy.min(array)` to calculate simple statistics.
* Use `numpy.mean(array, axis=0)` or `numpy.mean(array, axis=1)` to calculate statistics across the specified axis.
