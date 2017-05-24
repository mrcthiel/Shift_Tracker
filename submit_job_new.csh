#!/bin/tcsh
#$1 number of jobs
#$2 label
set PWD = `pwd`
set i = 18
set njobs = $1
set label = $2

while ( $i < 19 ) #18
./submit.csh $i $label $PWD $njobs
	@ i++
end
