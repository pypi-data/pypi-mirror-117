# simugrid Simulate Grid

Simulate grid means to simulate along a grid of parameter values, locally, in sequence
via AWS, each point along the grid is a point along the batch array.

This will be critically important for several things:

1. Simulate Section 3 material again, given estimated Parameters, possibly
2. To compute aggregate welfare change by changing consumption increments along a grid

Following previous structures three invoke alternatives, generated in sequence, for robust testing:

1. VIG
2. CMD
3. AWS

Try to mimic as much as possible the existing ESR call structure, this will be call SG call, for SimuGrid.

There will be some testing files in this folder, eventually should be centralized. Shares the same input structure as esr_parse I think.

1. run_sg.py
2. run_sg.

## Simu Grid 

## Thoughts 

ESR call had 8 steps ESR 1 through 8, does SP need multiple steps? Seems like it does not, seems like it is a one step thing. Should still allow for an Step 1, although nothing conditional on that for now, in case additional steps, procedures are needed.

Actually there should be ESR 1 and 2, because regardless, will need to sync and run local operations, like join columns from various tables together for for matrix to conduct analysis. 

Might even have ESR 2 and ESR 3, where ESR 2 aggregates up the aggregate statistics files, and ESR 3 aggregates up the state-specific statistics. 

## Solution Principles 

The initial idea I had was definitely incorrect, should not be resolving the model. In simple C problem, can algebraically compute, can not do so in the framework here. 

### Random Thoughts

Have to compute directly. 

Suppose just have regular (a,z) dynamic programming problem. There, solve first under the first set of parameters for the policy functions. Then fixing the policy function, iterate over value function until convergence again. Involves eliminating the optimization segement of the code, and inserting in current policy function, and aadding in a incremental c increase parameter. 

The same idea in the frame work here. I already have solved for the policy functions, given some parameter combinations, given that, iterate over N periods, to find Value given policy.

The accurate way, given the lack of convergence that I currently have, is to store optimal policies from all current iterations, 

But I think the first thing, the primary thing is to solve for values along the state-space.

### Value Given Proportional C Increase, Fix Policy

Alternative [opti_value_eachj](https://github.com/FanWangEcon/ThaiJMP/blob/baae5e4c493e20060602f9714970e99b201c0c0c/soluvalue/optimax.py#L13) function that picks optimal value based on existing optimal choice index. 

Alternative [vfi_todayfixed](https://github.com/FanWangEcon/ThaiJMP/blob/baae5e4c493e20060602f9714970e99b201c0c0c/soluvalue/soluvfi.py#L17) is needed that iterate after convergence for the same number of periods, given consumption increase proportion, without changing/updating the policy function. Given what has been learned, don't need to know the C, just need utoday_stack, which is given, multiplied by (1+psi)^(1-gamma). 

Include an additional model parameter which is the proportion of value to increase. 

### Computational Implementation of CEV calculation 

Even though there are multiple alternative policies, but the CEV grid only needs to be computed once. Holding all else the same, get the value at every increment, plus as well as minus, then there is some stored file. Think of each column as a different percentage change, and each row a different state-space element. The values are value at this increment of consumption. Then all alternative policies criss-cross this surface.

### Simulate Models get Vs from Different Exercises for Counterfactual and Decompositions

1. At previous parameters, solve the model, and get the current equilibrium interest rate 
2. At new parameters, solve holding interest rate at the previous parameters
3. At the new parameters, solve using new interest rates. 

Do (2) and (3) a number of different times for different policies under consideration. 

Before putting in real actual parameters, we can do a test to see to what extend this is doable. 

Computationally, this is not too challenging. Solving first 1 GE model, say up to 5 PE models and 5 GE models separately, given estimated/known parameters.


### Visualizations and Graphs 

Visualizing PE vs GE gains and losses. 

In addition to showing the current graphs. Show for the Key overall counterfactual figure, who is losing and who is gaining under PE and GE. 

- x-axis of graph is coh 
- y-axis of graph are gains and losses in CEV units
- different subplot represents different type levels

GE vs PE gain. 

GE vs PE gain show this twice, first for overall actual policy change with three joint policies.
Then show these again separately for each of rhte four one policy at a time shift on the next page. 

Can visualize results evenwithout CEV changes with just VAL differences. 


## Questions

- [ ] speckey second element, does that matter, anything OK, just end with *_simu*?



