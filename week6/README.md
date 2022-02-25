## Week 6

This week we finished our `readwrite.ipynb` file on reading and writing data using only native python modules, the complete file is available in the [week5 folder](https://github.com/seidelj/python-course/edit/main/week5/).

We also began our introduction to working with packages that are not included in the default installation of Python, namely `pandas` and `numpy`.  Numpy is a dependency of pandas and provides arrays and matrix structures useful to scientific computing in Python.  We began replicating our readwrite.ipynb example, but using pandas.  We began the file `pandas_intro.ipynd`.


### Installing packages
In order to install `pandas` and its dependencies, you should have [pip](https://pypi.org/project/pip/), the package installer for Python.  You can confirm that `pip` is available to your Python environment by using the following commmand in your terminal or anaconda PowerShell prompt.

```
conda install pip
```

To install the pandas packages, along with its dependencies (numpy will automatically be included in the install of pandas) run the command
```
pip install pandas
```

Once you have installed the package, you can use it in your code using the `import` keyword.

```
import pandas as pd
import numpy as np
```

### Resources for using pandas
* Getting started [tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html) for pandas.

* pandas [User guide](https://pandas.pydata.org/docs/user_guide/index.html)
