open(FHNDL,">./lrep_d236.dta");
require 'emath.pl';
$x=(0-(0.1)+sqrt(0.1*0.1+1));$y=(($x)+0.1)/(($x)*(1-0.1*($x)));if(abs($x)<0.00001){ printf FHNDL"%f\n",$x; }else{ printf FHNDL"%s\n",$x; } if (abs($y)<0.00001) { printf FHNDL"%f",$y; } else { printf FHNDL"%s",$y; } 
close(FHNDL);
