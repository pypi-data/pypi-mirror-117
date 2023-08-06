# fs_esr_oneParam_lin.py

The VIG local testing function, no command line. Specify parameters directly and simulate with all direct 
specifications. 

This does not call run_esr, but invoke_main, whcih run_esr calls

# fs_esr_oneParam_lin_esr_parser.py

This is to call the esr_run f
 

# One Parameter Estimate/Calibrate Locally

1. Thin estimate (len=1) many starting points. Simulation results in excel, each file multiple region/periods.
2. Gather individual folder CSVs together, aggregate Excel with all simulations
3. Grab out region/time specific integrated rows, and generate mpoly estimates matrix (also spit out simulation top guesses)
4. Mpoly estimate (len large) same starting points as (1), fully estimate with mpoly approximation
5. Repeat (1) with Mpoly best results, these are starting point estimates
6. Estimate from these top points see what happens.
