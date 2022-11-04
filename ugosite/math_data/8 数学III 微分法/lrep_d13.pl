open(FHNDL,">./lrep_d13.dta");
require 'emath.pl';
$x=(4.5);$y=(($x)-2)*(($x)-2)*(($x)-2)/32-(($x)-2)/4+2;if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
