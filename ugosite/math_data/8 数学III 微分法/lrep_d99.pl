open(FHNDL,">./lrep_d99.dta");
require 'emath.pl';
$y=(sin(3.141592653589793238)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
