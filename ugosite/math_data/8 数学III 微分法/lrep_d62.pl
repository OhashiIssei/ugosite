open(FHNDL,">./lrep_d62.dta");
require 'emath.pl';
$y=(sin(0.261799387799149436)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
