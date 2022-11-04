open(FHNDL,">./lrep_d140.dta");
require 'emath.pl';
$oldx=$x=0;$oldy=0.866025403784438637*($x);$orgdx=$dx=.05;if($oldy>-25.0073&& $oldy<25.0073){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0;$x<$pi/2;$x+=.05){$y=0.866025403784438637*($x); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } };$x=$pi/2;$y=0.866025403784438637*($x); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
