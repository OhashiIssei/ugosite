open(FHNDL,">./lrep_d150.dta");
require 'emath.pl';
$x=(0.92);$y=-sin(($x))+sqrt(3)/2*($x);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
