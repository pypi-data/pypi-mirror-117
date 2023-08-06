Requirements:
- Estimate individual or set of Parameters
- Start estimation
  + at predetermined initial estimate points for all parameters
  + at random initial estimate points within some bounds
  + at single set of points, or multiple sets of starting values.
  + some parameters start at fixed number, some parameters start at random position within some interval
- Estimation can have bound restriction on some variables and not others
  + bound restrictions should be something that can be specified like esti, data, model and other parameters, with some default values and then could change as well based on requirements.

Guiding Principle:
- combo_type_list third element controls which paramters will be jointly and separately estimated, but it does not control what is the parameter estimation bound, does not control how many times parameters are to be randomly drawn from within bounds, if some are random and others are fixed. does not control those things at all.
- Given combo_type_list parameters to be estimated from 3rd element, the 1st and 2nd element, *file_name*, *file_sub_type*, just like in simulation, controls the actual parameter range.
