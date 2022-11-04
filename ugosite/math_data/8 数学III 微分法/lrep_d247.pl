open(FHNDL,">./lrep_d247.dta");
require 'emath.pl';
$y=(sin(0.523598775598298873)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
