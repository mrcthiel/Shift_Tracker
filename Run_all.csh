#!/bin/tcsh
#$1 label

set i = 18
set label = $1

while ( $i < 19 ) #18

sshfs mthiel@uerjpowerp100.cern.ch:/storage2/mthiel/trackerShift/ mount/
ls mount/GluGluTo2Jets_M_100_7TeV_exhume_cff_py_GEN_SIM_RECOBEFMIX_DIGI_RECO_${label}_${i}_* > files.txt 
cmsRun Validation/CTPPSValidation/python/validationCTPPSFast_gluglu_cfg.py
mv outValidation_gluglu_LHCT_NoPU.root outValidation_gluglu_LHCT_NoPU_${label}_${i}.root
fusermount -u mount

        @ i++
end



