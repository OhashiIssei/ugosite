open(FHNDL,">./lrep_d220.dta");
require 'emath.pl';
$x=(1-sqrt(2));$y=(($x)*($x)-1)*exp(-($x));if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
