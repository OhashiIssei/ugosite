open(FHNDL,">./lrep_d180.dta");
require 'emath.pl';
$oldx=$x=-4;$oldy=-2*($x);$orgdx=$dx=.05;if($oldy>-100.0075&& $oldy<100.0075){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-4;$x<4;$x+=.05){$y=-2*($x); if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$x,$y; } };$x=4;$y=-2*($x); if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
