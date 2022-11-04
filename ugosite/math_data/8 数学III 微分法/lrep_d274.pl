open(FHNDL,">./lrep_d274.dta");
require 'emath.pl';
$x=(2.7*sqrt(2.7));$y=log(($x))/($x);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
