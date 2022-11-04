open(FHNDL,">./lrep_d213.dta");
require 'emath.pl';
$x=(5*$pi/2);$y=(cos(($x))/($x)-sin(($x))+aval*($x))/($x);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
