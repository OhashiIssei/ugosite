open(FHNDL,">./lrep_d250.dta");
require 'emath.pl';
$y=(cos(3.665191429188092111)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
