# Overall CEV PE and GE strategy

2021-01-09 20:42

Two sets of exercises. Exercise A here

## Exercise A

Two prices, pre and post interest rates.
Also two sets of estimates parameters.

Simulate three times (with three different JSON files):

a. PE old rate and parameters
b. PE old rate and new Parameters
c. PE new rate and new Parameters
d. Simulate CEV grid around (1) N times.

So above exercise involes 3 + N simulations.

Objective is to generate a surface based on (d) and (a):

1. x-axis, different CEV changes
2. y-axis, different COH levels
3. cell-value, EV in levels.
4. "sub-figures", different A levels

Draw lines on this these A-specific surfaces:

1. From (b), for each COH level, find the EV on the (d) surface that is the closest
2. From (c), same.

Coding required:

1. run (a), (b), (c), (d) using existing routines
2. (d) surface combine results from individual cev files, select specific columns from many csv files, combine to a single file, with different column names.
3. Similar to (2), get columns from different files, combine to single file, use (2) code
4. For each column of (3), use (2) surface, find closest points.

Implement (2), (3) and (4) inside R with dplyr
