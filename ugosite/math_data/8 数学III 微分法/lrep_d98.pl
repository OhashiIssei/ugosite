open(FHNDL,">./lrep_d98.dta");
require 'emath.pl';
$y=(cos(3.141592653589793238)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
