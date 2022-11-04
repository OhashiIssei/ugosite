open(FHNDL,">./lrep_d56.dta");
require 'emath.pl';
$x=(-1/4);$y=2*($x)*($x)+($x)-1;if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
