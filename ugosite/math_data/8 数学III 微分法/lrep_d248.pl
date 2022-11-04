open(FHNDL,">./lrep_d248.dta");
require 'emath.pl';
$y=(cos(1.047197551196597746)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
