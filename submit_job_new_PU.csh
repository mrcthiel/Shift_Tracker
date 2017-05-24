#!/bin/tcsh
#$1 number of jobs
#$2 label
set PWD = `pwd`
set i = 0
set njobs = $1
set label = $2

while ( $i < 19 ) #18
./submit_PU.csh $i $label $PWD $njobs
	@ i++
end
