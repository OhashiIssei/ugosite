open(FHNDL,">./lrep_d147.dta");
require 'emath.pl';
$x=($pi/2);$y=0.866025403784438637*($x);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
