open(FHNDL,">./lrep_d226.dta");
require 'emath.pl';
$x=(1.9);$y=exp(1.9)*(($x)-1.9)+exp(1.9)+1;if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
