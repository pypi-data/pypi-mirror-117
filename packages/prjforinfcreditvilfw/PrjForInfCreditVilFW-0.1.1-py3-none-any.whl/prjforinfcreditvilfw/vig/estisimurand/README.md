# EstiSimuRand ESR Estimation Method

The folders have gotten more confused over time, pay attention to the three core files VIG, CMD and AWS call 
structures below. And later put them somewhere together. 

Want to keep separation between the functions more "hard-coded", rather than these later version that are all based on run_esr_parser.py. 

## Core Files 

*invoke.run_esr_parser.run_esr_arg_generator* based invocation called:

Test calls of three types, with: 

>    dc_it_execute_type = {'model_assumption': 0, 'compute_size': 0,
>                          'esti_size': 0, 'esti_param': 0,
>                          'call_type': 1, 'param_date': 0} 

- VIG: *vig.estisimurand.sall_local.fs_esr_oneparam_lin_esr_parser.main*
- CMD: *vig\estisimurand\sall_local_sandbox\working_cmd\fs_esr_oneparam_lin_cmd_parser.py*
- AWS: 

## Subfolder guide

- *sall_local*: Call ESR steps 1 through 8 locally, can be done by running the vig/script or by using command line. All eight steps done with single script file.
- *sall_aws*: ESR Steps, 1 through 8, (1) submitting tasks to AWS (2) syncing locally with S3 which has AWS outputs (3) Local gather estimation compute based on AWS outputs (4) send local results to S3 (5) do these multiple times for the 8 steps.

## ESR Estimation Routine

1. *Thin estimate*: Simulate at N sets of parameter combinations
2. *Gather*: Polynomial approximation surface based on (1) for each outcome of interest, find best
3. Estimation at N sets of starting points with (2) as objective function
4. Gather results frorm (3), find M best.
5. Simulate (estimate once) at the top M best results from (4) actual model, compare objective to approximated from (3)
6. Gather results from (5), re-rank best of the M best from (4)
7. Estimate at the top M best results from (4) actual model, (4) M best are M best seeds
8. Gather results from (7), re-rank best of the final results from the M best seeds

## Broad Concepts About Parameter Specifications

There are four groups of decisions, with associated parameters:

- Simulation Decisions (SD): Regardless of the estimation structure, at each parameter combination, how should simulation be done.
- Estimation Decisions (ED): Estimation related Specifications and decisions
- Compute Decisions (ED): Computational structure specifications
- Output Decisions (ED): What results to spit how, what to show from estimation/simulation.

There is a Number of different types of parameters to choose pick determine:

1. range of parameter values and other parameter specifications for all the parameters.
2. over which parameters to estimate the model, which parameters are free Parameters
3. how the model should be simulated, GE or not, Integrated or not. Many other decisions related to how the model should be simulated, most related to parameters/model specifications.
4. region and time periods for estimation, allowing which parameters to vary, and to jointly try to match outcomes in several regions and/or time periods.
5. how many points at which to do ESR draws for simulation
6. computational structure, if local, or remote, whether parallel processing should be used, and if using remote the compute requirements
7. where to store results, and what graphs/tables etc to save and to output.

Functions to Rely on:

- ESTIMATION FUNCTION: invoke.run_main.invoke_main
- AGGREGATION FUNCTION: estimation.postprocess.process_main.search_combine_indi_esti

Each of the function needs to be called several times. To facilitate calling them, their parameters are organized
in a dictionary, which is modified for particular invokcations.
