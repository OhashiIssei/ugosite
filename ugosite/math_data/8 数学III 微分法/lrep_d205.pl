open(FHNDL,">./lrep_d205.dta");
require 'emath.pl';
$x=(5.7);$y=(($x)-2)*(($x)-2)*(($x)-2)/8-(($x)-2)+2;if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
