open(FHNDL,">./lrep_d141.dta");
require 'emath.pl';
$oldx=$x=0;$oldy=($x);$orgdx=$dx=.05;if($oldy>-25.0073&& $oldy<25.0073){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0;$x<$pi/2;$x+=.05){$y=($x); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } };$x=$pi/2;$y=($x); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
