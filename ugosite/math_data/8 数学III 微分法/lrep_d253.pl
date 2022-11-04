open(FHNDL,">./lrep_d253.dta");
require 'emath.pl';
$y=sqrt((0.366025403784439)**2+(-0.366025403784439)**2); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
