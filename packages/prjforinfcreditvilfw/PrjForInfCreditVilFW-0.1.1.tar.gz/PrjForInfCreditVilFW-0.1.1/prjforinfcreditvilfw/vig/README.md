Generate vignette type files, even though this is a private repo, still generate vig so that can understand
each model aspect clearly. The vig files can and should be kind of loosely structured, not as ipynb or rmd files, but just as pythong scripts, that generate readme log outputs to be stored in corresponding folders for vig in some corresponding structure with proper time-stamp, to be tracked by dropbox, to clearly show the outputs from each.

Three things

1. find best estimates from preivous mpoly rounds
2. from local to aws estimate test
3. local simulation full state-space
4. local simulation CEV compute. 

## Estimation Routines 

There is a core function or *run_esr.py*. This function has a set of arguments to be parsed. 

This is the gateway function to operate via AWS and CMD. 

*invoke.run_main.invoke_main* and *estimation.postprocess.process_main.search_combine_indi_esti* are the two functions
that run_esr call. 

They require dictionaries of list of various items, and is a little bit complicated. 

There is a fixed set of parameter invocation types with different parameter combinations for the different arguments
for run_esr. 

There is another function, basically, that parses inputs to generate some default calls to run_esr. 

Why is that needed? Because otherwise the run_esr function would seem complicated, hard to figure out what parameter 
combinations are legal. So useful to have the key default call cases. 

Now the strange thing and confusing thing is that potentially, there is a lot of things that can be specified, and each
could be parsed separately as an input to the parser for inputs for run_esr. However, that would eliminate the point. 

run_esr needs a simple input parse, where under different condition combinations, different sets of parameters are generated.
