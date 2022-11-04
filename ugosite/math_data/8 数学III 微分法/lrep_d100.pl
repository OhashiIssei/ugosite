open(FHNDL,">./lrep_d100.dta");
require 'emath.pl';
$y=(cos(2.356194490192344928)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
