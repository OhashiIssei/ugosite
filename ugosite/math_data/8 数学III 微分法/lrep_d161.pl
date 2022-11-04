open(FHNDL,">./lrep_d161.dta");
require 'emath.pl';
$oldx=$x=-2;$oldy=4*($x);$orgdx=$dx=.05;if($oldy>-192.30878&& $oldy<192.30878){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-2;$x<2;$x+=.05){$y=4*($x); if($y>-192.30878&& $y<192.30878){ printf FHNDL"(%f,%f)",$x,$y; } };$x=2;$y=4*($x); if($y>-192.30878&& $y<192.30878){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
