

loop over estimating parameters, draw N graphs for them. x-axis is time, y is current parameter values. Separate the graphing issue from the estimation issues

## Estimation Moment Matching

- Solution has json dict
- Estimation provides a json dict with identical keys to match subset of parameters up to solution json dict Results

**Moments_a**
- *Moments_a _b, etc...* contains data for estimation, subtype modifies Data
- stored in esti_spec['moments_type']

**Momsets_a**
- *Momsets_a _b, etc...* contains requirement about which parameters are to be included in current estimation, and the weight.
- stored in esti_spec['momsets_type']

## Moment Matching Graphing

- Using the same key names as in estimation, graphing out M by N grid of graphs, where each graph is for a particular combination of data vs model solution moments.
- The current available data moments might not include what we want to graph out, if that is the case, still graph out, just no line/figure for where the data is.
- Note these graphs do not have to be a single key each graph, each graph could include a combination of keys, added up, differenced out, depending on whatever formula is specified under the graphing rules. Note again, these graphing adding up, subtracting rules etc have nothing to do with estimation. Estimation just cares about which moments are included and the weight on moments.

## Objective
def objective({x_colnames, d, p, w}, data_mat)
  return wgt1*(x1 - d1)^(pow1) + wgt2*(x2 - d2)^(pow2) + etc
