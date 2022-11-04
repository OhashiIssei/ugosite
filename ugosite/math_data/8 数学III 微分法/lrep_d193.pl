open(FHNDL,">./lrep_d193.dta");
require 'emath.pl';
$oldx=$x=0.01;$oldy=cos(($x))/($x);$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0.01;$x<8;$x+=.05){$y=cos(($x))/($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=8;$y=cos(($x))/($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
