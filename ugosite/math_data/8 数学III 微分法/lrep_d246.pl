open(FHNDL,">./lrep_d246.dta");
require 'emath.pl';
$y=(cos(0.523598775598298873)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
