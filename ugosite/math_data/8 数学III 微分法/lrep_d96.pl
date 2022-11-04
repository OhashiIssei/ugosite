open(FHNDL,">./lrep_d96.dta");
require 'emath.pl';
$x=(0);$y=exp(-($x)/4);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
