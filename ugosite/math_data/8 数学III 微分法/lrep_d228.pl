open(FHNDL,">./lrep_d228.dta");
require 'emath.pl';
$x=(2.93);$y=exp(2.93)*(($x)-2.93)+exp(2.93)+1;if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
