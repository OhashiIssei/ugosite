open(FHNDL,">./lrep_d54.dta");
require 'emath.pl';
$x=(1);$y=2*($x)*($x)+($x)-1;if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
