open(FHNDL,">./lrep_d249.dta");
require 'emath.pl';
$y=(sin(1.047197551196597746)); if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; 
close(FHNDL);
