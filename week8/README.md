## Summary

This week we revisted pandas_intro.ipynb from week6 to take a closer look at the `apply` function in pandas.  Specifically we covered how the argument passed to our custom function when using `apply` is determined based on the pandas object that we are calling the apply method through.

1.  Series.apply will pass each element indvidually of the series object.
2.  DataFrame.apply will pass each column (axis=0) or each row (axis=1) of the DataFrame
3.  DataFrameGroupBy will pass each DataFrame.

After this in depth review of the apply function, we created a new variable for our roster dataframe that determine whether an individual was in the top 50 percentile of their respective group (red or blue).

We also started a new file `pandas_advanced.ipynd`.  We read in a csv file via URL and demonstrated a handful of commands to get a birds eye view of a the data.  We then created a custom function to create a new variable that would represent the fundemental value of an asset in a given market and round of a fictional data set from an experiment.
