open(FHNDL,">./lrep_d167.dta");
require 'emath.pl';
$oldx=$x=-3;$oldy=5;$orgdx=$dx=.05;if($oldy>-100.0075&& $oldy<100.0075){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-3;$x<3;$x+=.05){$y=5; if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$x,$y; } };$x=3;$y=5; if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
