open(FHNDL,">./lrep_d159.dta");
require 'emath.pl';
$oldx=$x=-2;$oldy=2*($x)*($x)*($x)+($x)*($x)-3;$orgdx=$dx=.05;if($oldy>-192.30878&& $oldy<192.30878){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-2;$x<2;$x+=.05){$y=2*($x)*($x)*($x)+($x)*($x)-3; if($y>-192.30878&& $y<192.30878){ printf FHNDL"(%f,%f)",$x,$y; } };$x=2;$y=2*($x)*($x)*($x)+($x)*($x)-3; if($y>-192.30878&& $y<192.30878){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
