open(FHNDL,">./lrep_d94.dta");
require 'emath.pl';
$x=(7*$pi/2);$y=sin(($x));if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
