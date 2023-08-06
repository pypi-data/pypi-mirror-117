
Why not put compute_specs and esti_specs along with other parameters?

They are needed generally throughout estimation and solution process, starting
at the very beginning. The parameters that are only contained in param_combo are
generally loaded in later. 

For example, parallel or not, and memory requirement, that is not a model specification
that is an environment specification, which might be associated with different model
specifications, but still is just an environment specification. 