open(FHNDL,">./lrep_d260.dta");
require 'emath.pl';
$x=(1);$y=($x)-1/2*sin(2*($x));if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
