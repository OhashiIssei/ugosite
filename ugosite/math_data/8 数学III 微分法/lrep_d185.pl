open(FHNDL,">./lrep_d185.dta");
require 'emath.pl';
$x=($pi/2*1.15);$y=-2*($x);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
