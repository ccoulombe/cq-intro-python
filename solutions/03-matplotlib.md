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

# Visualizing Tabular Data
## Objectives
* Plot simple graphs from data.
* Plot multiple graphs in a single figure.

***

Matplotlib documentation: https://matplotlib.org/stable/

# Visualizing data

In order to visualize data, we first need to import the library:
```python tags=["empty"]
import matplotlib.pyplot
```

We also need to load the data in this notebook:
```python
import numpy
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
```

We can now plot our data:
```python
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
```
Each row in the heat map corresponds to a patient in the clinical trial dataset, and each column corresponds to a day in the dataset. Blue pixels in this heat map represent low values, while yellow pixels represent high values. As we can see, the general number of inflammation flare-ups for the patients rises and falls over a 40-day period.

We can plot other kinds of graphs, for instance the average inflammation per day across all patients:
```python
ave_inflammation = numpy.mean(data, axis=0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()
```

Can we have a look at the maximum and minimum?
```python
inflam_min = numpy.min(data, axis=0)
inflam_max = numpy.max(data, axis=0)

matplotlib.pyplot.plot(inflam_min)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(inflam_max)
matplotlib.pyplot.show()
```

# Grouping plots
We can group similar plots in a single figure using subplots. Here's a complete example:
```python
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()

matplotlib.pyplot.savefig('inflammation.png')
matplotlib.pyplot.show()
```

***
# Key Points
* Use the `pyplot` module from the `matplotlib` library for creating simple visualizations.
