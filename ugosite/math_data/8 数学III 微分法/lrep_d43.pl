open(FHNDL,">./lrep_d43.dta");
require 'emath.pl';
$x=(1.208712152522080014);$y=(exp(-($x)))*($x);if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
