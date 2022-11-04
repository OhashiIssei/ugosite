open(FHNDL,">./lrep_d25.dta");
require 'emath.pl';
$oldx=$x=-2;$oldy=-$pi/2*sin(($x))+cos(($x));$orgdx=$dx=.05;if($oldy>-62.49655&& $oldy<62.49655){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-2;$x<$pi/2;$x+=.05){$y=-$pi/2*sin(($x))+cos(($x)); if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } };$x=$pi/2;$y=-$pi/2*sin(($x))+cos(($x)); if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
