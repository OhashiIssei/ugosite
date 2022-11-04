open(FHNDL,">./lrep_d103.dta");
require 'emath.pl';
$y=(sin(0)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
