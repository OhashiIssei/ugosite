open(FHNDL,">./lrep_d68.dta");
require 'emath.pl';
$x=(-3);$y=-1-sin(($x))+cos(2*($x));if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
