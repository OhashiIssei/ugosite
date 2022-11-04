open(FHNDL,">./lrep_d251.dta");
require 'emath.pl';
$y=(sin(3.665191429188092111)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
