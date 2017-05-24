#!/bin/csh

set i = $1
set label = $2
set PWD = $3
set njobs = $4
set n = 0


while ( $n < $njobs )
 bsub -q1nh<<EOF
#!/bin/csh
cd $PWD
cmsenv
cd -
cmsRun $PWD/GluGluTo2Jets_M_100_7TeV_exhume_cff_py_GEN_SIM_RECOBEFMIX_DIGI_RECO.py LabelShift=$label shift_n=$i job=$n
scp *.root mthiel@uerjpowerp100.cern.ch:/storage2/mthiel/trackerShift/GluGluTo2Jets_M_100_7TeV_exhume_cff_py_GEN_SIM_RECOBEFMIX_DIGI_RECO_${label}_${i}_${n}.root
EOF
    @ n++
end

