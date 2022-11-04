open(FHNDL,">./lrep_d58.dta");
require 'emath.pl';
$y=(sin(3.403392041388942674)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
