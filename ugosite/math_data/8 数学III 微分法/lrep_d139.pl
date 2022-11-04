open(FHNDL,">./lrep_d139.dta");
require 'emath.pl';
$oldx=$x=0;$oldy=sin(($x));$orgdx=$dx=.05;if($oldy>-25.0073&& $oldy<25.0073){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0;$x<$pi/2;$x+=.05){$y=sin(($x)); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } };$x=$pi/2;$y=sin(($x)); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
