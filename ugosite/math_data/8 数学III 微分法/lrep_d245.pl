open(FHNDL,">./lrep_d245.dta");
require 'emath.pl';
$x=(0-(0.7)+sqrt(0.7*0.7+1));$y=(($x)+0.7)/(($x)*(1-0.7*($x)));if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
