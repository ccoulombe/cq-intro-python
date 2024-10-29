---
jupytext:
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

# Creating Function
## Objectives
* Define a function that takes parameters.
* Return a value from a function.
* Test and debug a function.
* Set default values for function parameters.
* Explain why we should divide programs into small, single-purpose functions.

***
Functions let us reuse pieces of code frequently used with different parameters.

Let's start by defining a function `fahr_to_celsius` that converts temperatures from Fahrenheit to Celsius:

```{code-cell} ipython3
:tags: [empty]

def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))
```

![image](images/python-function.svg)

The function definition opens with the keyword `def` followed by the name of the function (`fahr_to_celsius`) and a parenthesized list of parameter names (`temp`). The body of the function — the statements that are executed when it runs — is indented below the definition line. The body concludes with a `return` keyword followed by the return value.

When we call the function, the values we pass to it are assigned to those variables so that we can use them inside the function. Inside the function, we use a `return` statement to send a result back to whoever asked for it.

```{code-cell} ipython3
:tags: [empty]

fahr_to_celsius(32)
```

The above call our function with the parameter `temp` set to `32` and then return the function value. We can reuse our function:

```{code-cell} ipython3
print('freezing point of water:', fahr_to_celsius(32), 'C')
print('boiling point of water:', fahr_to_celsius(212), 'C')
```

# Composing Functions
We can also write the function to turn Celsius into Kelvin, now that we've successfully written our `fahr_to_celsius` function.

```{code-cell} ipython3
def celsius_to_kelvin(temp_c):
    return temp_c + 273.15

print('freezing point of water in Kelvin:', celsius_to_kelvin(0.))
```

And let’s not forget about converting Fahrenheit to Kelvin! We can reuse our previous functions to compose a new function:

```{code-cell} ipython3
def fahr_to_kelvin(temp_f):
    temp_c = fahr_to_celsius(temp_f)
    temp_k = celsius_to_kelvin(temp_c)
    return temp_k

print('boiling point of water in Kelvin:', fahr_to_kelvin(212.0))
```

We define basic operations and combine them into functions, and reuse them to create a larger script. Typically, functions will have approximately a dozen lines, so they are simple and easily readable.

# Testing and Documenting
We then need to verify that our functions are behaving correctly. In order to do so, we can run each function and print out the boolean result of an equality test. We can also assert that our function behave correctly by using an [assertion statement](https://docs.python.org/3/reference/simple_stmts.html#assert). An assertion will pass when the statement is `True`, otherwise will raise an exception and the code or function will not be allowed to continue. This is very useful in preventing bugs and ensuring correctness.

We can first print out the boolean value

```{code-cell} ipython3
print(fahr_to_celsius(32) == 0)  # should print True
assert fahr_to_celsius(32) == 0, "32F should be 0 Celsius"
```

```{code-cell} ipython3
assert celsius_to_kelvin(0) == 273.15, "0 Celsius should be 273.15 Kelvin"
```

```{code-cell} ipython3
:tags: [empty]

assert fahr_to_kelvin(32) == 273.15, "32 Fahrenheit should be 273.15 Kelvin"
```

Our functions can contain more than just code. We can document it with `docstring` and comments.
A good coding style is [`numpydoc`](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard).

```{code-cell} ipython3
def fahr_to_celsius(temp):
    """
    Converts Fahrenheit to Celcius.
    
    Parameters:
        temp: Temperature in Fahr.
        
    Example: 
        fahr_to_celsius(32) => 0.0
    """
    # this is a comment
    return ((temp - 32) * (5/9))
```

By documenting and commenting your functions, you help yourself and potential readers.

```{code-cell} ipython3
help(fahr_to_celsius)
```

The `docstring` is printed when using the built-in `help` function, while comments are otherwise ignored.

# Default Values
We can also define default values to the function arguments.

```{code-cell} ipython3
def fahr_to_celsius(temp=32):
    """
    Converts Fahrenheit to Celcius.
    
    Parameters:
        temp: Temperature in Fahr. int, default: 32
        
    Example: 
        fahr_to_celsius(32) => 0.0
    """
    return ((temp - 32) * (5/9))
```

```{code-cell} ipython3
:tags: [empty]

fahr_to_celsius() # No argument given, the default value is used.
```

The arguments can be given by their names (especially interesting when there are many arguments).

```{code-cell} ipython3
:tags: [empty]

fahr_to_celsius(temp=0) 
```

# Exercises
#### 1.
Based on the following function:

```{code-cell} ipython3
def display(a, b, c):
    print('a:', a, 'b:', b, 'c:', c)
```

Redefine the function `display` such as every parameter has a default value of `1`, `2`, `3` respectively.

```{code-cell} ipython3
:tags: [empty]

def display(a=1, b=2, c=3):
    print('a:', a, 'b:', b, 'c:', c)
```

Then execute it :
- without parameters
- with one parameter
- with two parameters
- with the third parameter set to the value `77`
- with providing value to two parameters only (e.g. `b` and `c`)
- with providing value to the parameters ordered as: `c,b,a`

```{code-cell} ipython3
:tags: [empty]

display()
display(55)
display(55, 66)
display(c=77)
display(b=22, c=77)
display(c=9,b=8,a=7)
```

#### 2. Combining Strings
Write a function `wrap` that takes two strings as input and returns the first one wrapped (surrounded) with the second one. The default wrapping string is `*`.

Answer:
```
print(wrap('value'))      => *value*
print(wrap('value', '+')) => +value+
```

Define the function:

```{code-cell} ipython3
:tags: [empty]

def wrap(value, wrapper='*'):
    return wrapper + value + wrapper
```

Assert the function is correct:

```{code-cell} ipython3
:tags: [empty]

# Assert that our function is correct
assert wrap('1') == "*1*"
assert wrap('1', '+') == "+1+"
```

Print the results:

```{code-cell} ipython3
:tags: [empty]

print(wrap('wrapped_value'))
print(wrap('wrapped_value', '+'))
```

#### 3. Variables Inside and Outside Functions
What will the following code print (and why)?

```{code-cell} ipython3
f = 0
k = 0

def f2k(f):
    k = f + 10
    return k

print(f2k(32))

print(k)
```

`k` is `0` because the `k` inside the function `f2k` doesn’t know about the `k` defined outside the function.

+++

***
# Key Points
* Define a function using `def function_name(parameter)`.
* The body of a function must be indented.
* Call a function using `function_name(value)`.
* Numbers are stored as integers or floating-point numbers.
* Variables defined within a function can only be seen and used within the body of the function.
* Variables created outside of any function are called global variables.
* Within a function, we can access global variables.
* Variables created within a function override global variables if their names match.
* Use `help(thing)` to view help for something.
* Put docstrings in functions to provide help for that function.
* Specify default values for parameters when defining a function using `name=value` in the parameter list.
* Parameters can be passed by matching based on name, by position, or by omitting them (in which case the default value is used).
* Put code whose parameters change frequently in a function, then call it with different parameter values to customize its behaviour.
