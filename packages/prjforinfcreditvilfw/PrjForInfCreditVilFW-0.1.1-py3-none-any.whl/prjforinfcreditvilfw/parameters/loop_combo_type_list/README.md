
For simulating the effects of model across a grid of parameter values.

For estimating N parameters in N estimation concurrently where each estimation only
estimates one parameter


# combo_type_list

*combo_type_list* is a list with N elements.

Used in [invoke.local_estimate.py](/invoke/local_estimate.py) and [invoke.local_simulate.py](/invoke/local_simulate.py). On AWS, each element of the combo_type_list--each combo_type--starts a separate task or job. This allows for concurrent simulations and estimations.

**Example 1**:

> combo_type_list = \
> [
> 	['a', '20180607_alpk', ['esti_param.alpha_k']],
> 	['a', '20180517_A', ['data_param.A']]
> 	['a', '20180403a', None],
> ]

- the first element of the list will do something involving *alpha_k* parameter in simulation or estimation, the details for that is in file *a*, category *20180607_alpk*. This likely means generating some loop over *alpha_k*, and using *alpha_k* as the sorting parameter eventually when outputting results
- the third element of the list has None in the third position, this means there is no ordering parameter, when None, this means we are simuating at some particular single set of parameter values, not looping over or estimating over a particular parameter in the set.


**Example 2**:

> combo_type_list = \
> [
> 	['a', '20180607_alpk', ['esti_param.alpha_k',
                            'data_param.A']],
> 	['a', '20180517_A', ['data_param.A']],
> 	['a', '20180403a', None],
> ]

- the first element now means inside the file *a*, category *20180607_alpk*, we are operating over two parameters, perhaps it is an estimation where there are two parameters been estimated, or perhaps we are doing simulation looping over two nested parameters.
- the second element still just has one parameter in the 3rd position
- we could have combo_type_list where some element of the list involves multiple parameters, others involving only one parameter...

