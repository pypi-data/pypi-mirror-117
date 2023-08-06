temporary files, copied over from *sall_aws*. Globally replace within this folder various keys, to change estimation structure and run.

A duplicate of the files here, after successfully finishing running, would best
appear in the results folder to allow for easier duplications etc.

Change from *x* and 5 draws to regular and 100 draws:
1. Changed *20201025x_esr_tstN5_aws* to *20201025_esr_tstN100_aws*
2. Changed *_tinytst_* to *_medtst_*

## Folders

- *sall_aws*: TST5X results hard-coded, not meant to be changed,
- *sall_aws_sandbox*: global replace with current estimation specification
    - template: template, this has placeholder values, see below
    - woroking: copy pasted from template folder, with global replace
    - store: if want to store some particular calls.
- *sall_local*: local VIG and CMD that generate the same results as *sall_aws* fixed.
- *sandbox*: some older files

## e_20201025_esr_tstN100_aws_list_tKap

Generates results in these three folders on AWS and Locally sync:

G:\S3\thaijmp202010\esti_tst

- e_20201025_esr_tstN100_aws_list_tKap
- [e_20201025_esr_tstN100_aws_list_tKap_mlt_ce1a2](https://s3.console.aws.amazon.com/s3/buckets/thaijmp202010?region=us-east-1&prefix=esti_tst/e_20201025_esr_tstN100_aws_list_tKap_mlt_ce1a2/&showversions=false)
- [e_20201025_esr_tstN100_aws_list_tKap_mlt_ne1a2](https://s3.console.aws.amazon.com/s3/buckets/thaijmp202010?region=us-east-1&prefix=esti_tst/e_20201025_esr_tstN100_aws_list_tKap_mlt_ne1a2/&showversions=false)

1. Changed *20201025_esr_CTBCTBCTB* to *20201025_esr_tstN100_aws*
2. Changed *_COMPSIZE_* to *_medtst_*
3. Changed *ng_s_t* to *ng_s_t*

##

1. *20201025_esr_CTBCTBCTB* to *20201025_ITG_esr_tstN100_AWS*
2. Changed *_medtst_* to *_medtst_*
3. Changed *ng_s_t* to *ng_s_t*
