open(FHNDL,">./lrep_d9.dta");
require 'emath.pl';
$x=(2*$pi);$y=cos(($x))/($x);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
