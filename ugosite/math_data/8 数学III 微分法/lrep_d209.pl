open(FHNDL,">./lrep_d209.dta");
require 'emath.pl';
$x=(12);$y=2/(5*$pi)+0.05;if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
