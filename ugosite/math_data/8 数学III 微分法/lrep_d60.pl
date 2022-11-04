open(FHNDL,">./lrep_d60.dta");
require 'emath.pl';
$y=(sin(6.02138591938043704)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
