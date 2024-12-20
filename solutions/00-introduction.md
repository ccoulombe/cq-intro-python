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

# Programming with Python
Thanks to the Carpentries, part of this material was adapted from: http://swcarpentry.github.io/python-novice-inflammation

## Python
- a high-level scripting language.

- designed to be highly readable. It uses English keywords frequently whereas other languages use punctuation, and it has fewer syntactical constructions than other languages.

- interpreted: Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. Grouping of statements is done by indentation instead of beginning and ending brackets (as in C or C++).

- interactive: You can actually sit at a Python prompt and interact with the interpreter directly to write your programs. This notebook is an example of it.

By the way, the language is named after the BBC show “Monty Python’s Flying Circus” and has nothing to do with reptiles.


It is used in a various number of fields but to name a few:
- Scientific Computing and Data Science
- Machine Learning and Artificial Intelligence
- Web Development and Framework

## Jupyter Notebook

The notebook extends the console-based approach to interactive computing in a qualitatively new direction, providing a web-based application suitable for capturing the whole computation process: developing, documenting, and executing code, as well as communicating the results. The Jupyter notebook combines two components:

* A web application: a browser-based tool for interactive authoring of documents which combine explanatory text, mathematics, computations and their rich media output.

* Notebook documents: a representation of all content visible in the web application, including inputs and outputs of the computations, explanatory text, mathematics, images, and rich media representations of objects.

### Main features of the web application
* In-browser editing for code, with automatic syntax highlighting, indentation, and tab completion/introspection.

* The ability to execute code from the browser, with the results of computations attached to the code which generated them.

* Displaying the result of computation using rich media representations, such as HTML, LaTeX, PNG, SVG, etc. For example, publication-quality figures rendered by the [matplotlib](https://matplotlib.org/) library, can be included inline.

* In-browser editing for rich text using the Markdown markup language, which can provide commentary for the code, is not limited to plain text.

* The ability to easily include mathematical notation within markdown cells using LaTeX, and rendered natively by [MathJax](https://www.mathjax.org/).

### Notebook documents
Notebook documents contain the inputs and outputs of an interactive session as well as additional text that accompanies the code but is not meant for execution. In this way, notebook files can serve as a complete computational record of a session, interleaving executable code with explanatory text, mathematics, and rich representations of resulting objects. These documents are internally JSON files and are saved with the `.ipynb` extension. Since JSON is a plain text format, they can be version-controlled and shared with colleagues.

Notebooks may be exported to a range of static formats, including HTML (for example, for blog posts), reStructuredText, LaTeX, PDF, and slide shows, via the nbconvert command.

Furthermore, any `.ipynb` notebook document available from a public URL can be shared via the Jupyter Notebook Viewer (nbviewer). This service loads the notebook document from the URL and renders it as a static web page. The results may thus be shared with a colleague, or as a public blog post, without other users needing to install the Jupyter notebook themselves. In effect, nbviewer is simply nbconvert as a web service, so you can do your own static conversions with nbconvert, without relying on nbviewer.

Source : https://jupyter-notebook.readthedocs.io/en/stable/notebook.html

## How to Use Jupyter

When a cell is in `edit` mode:

  Shortcut  | Description
----------- | -----------
Shift+Enter | Run the cell, and go to the next
Tab         | Indent code or auto-completion
Esc         | Go to command mode

When a cell is in `command` mode:

  Shortcut   | Description
------------ | -----------
Shift+Enter  | Run the cell, and go to the next
Double-click | Go to edit mode
Enter        | Go to edit mode

  Shortcut   | Description
------------ | -----------
A            | Insert a cell above
B            | Insert a cell below
C            | Copy the current cell
V            | Paste the cell below
D D          | Delete the current cell
M            | Change to Markdown cell
Y            | Change to Code cell


## Execution:
The square brackets on the left are the [execution counts](https://jupyter-client.readthedocs.io/en/latest/messaging.html#execution-counter-prompt-number) associated with the cell. The first cell executed gets `[1]`, the second `[2]`, etc. Running a previously executed cell will modify its execution count.

To reset all cells: from the top menu, select `Kernel -> Restart & Clear Output`

***

# Scenario: A Miracle Arthritis Inflammation Cure
The CSV file contains the number of inflammation flare-ups per day for the 60 patients in the initial clinical trial, with the trial lasting 40 days. Each row corresponds to a patient, and each column corresponds to a day in the trial. Once a patient has their first inflammation flare-up they take the medication and wait a few weeks for it to take effect and reduce flare-ups.

To see how effective the treatment is we would like to:
1. Calculate the average inflammation per day across all patients.
2. Plot the result to discuss and share with colleagues.

![image](images/lesson-overview.svg)

## Data format
The data sets are stored in comma-separated values (CSV) format:

* each row holds information for a single patient,
* columns represent successive days.
The first three rows of our first file look like this:
```text
0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
```
Each number represents the number of inflammation bouts that a particular patient experienced on a given day.

For example, value `6` at row `3` column `7` of the data set above means that the third patient was experiencing inflammation six times on the seventh day of the clinical study.

In order to analyze this data and report to our colleagues, we’ll have to learn a little bit about programming.

# A word on Copilot or ChatGPT
While it may seem that using co-pilot or ChatGPT may help, it actually hinder learning by providing part of code that may or may not make sense to you.

It can be useful to write test cases to validate your code, and help think of corner cases, but could also hinder your development.
<div class="alert alert-success">
  <strong>Do not use it while learning programming!</strong>
</div>

**Bottom line** : it is best to understand what these tools suggests, before using them.

![image](images/chatgpt.png)
