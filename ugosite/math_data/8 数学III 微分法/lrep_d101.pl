open(FHNDL,">./lrep_d101.dta");
require 'emath.pl';
$y=(sin(2.356194490192344928)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
