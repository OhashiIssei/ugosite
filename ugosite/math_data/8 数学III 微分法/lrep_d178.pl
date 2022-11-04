open(FHNDL,">./lrep_d178.dta");
require 'emath.pl';
$oldx=$x=-5;$oldy=-$pi/2;$orgdx=$dx=.05;if($oldy>-100.0075&& $oldy<100.0075){ printf FHNDL"(%f,%f)",$oldy,$x;} 
for($x=-5;$x<5;$x+=.05){$y=-$pi/2; if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$y,$x; } };$x=5;$y=-$pi/2; if($y>-100.0075&& $y<100.0075){ printf FHNDL"(%f,%f)",$y,$x; } 
close(FHNDL);
