open(FHNDL,">./lrep_d179.dta");
require 'emath.pl';
$oldx=$x=-4;$oldy=tan(($x));$orgdx=$dx=.05;if($oldy>-100.0075&& $oldy<100.0075){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-4;$x<4;$x+=.05){$y=tan(($x)); if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$x,$y; } };$x=4;$y=tan(($x)); if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
