open(FHNDL,">./lrep_d26.dta");
require 'emath.pl';
$oldx=$x=-2;$oldy=-$pi/2*sin(($x))+cos(($x));$orgdx=$dx=.05;if($oldy>-62.49655&& $oldy<62.49655){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-2;$x<4;$x+=.05){$y=-$pi/2*sin(($x))+cos(($x)); if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } };$x=4;$y=-$pi/2*sin(($x))+cos(($x)); if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
