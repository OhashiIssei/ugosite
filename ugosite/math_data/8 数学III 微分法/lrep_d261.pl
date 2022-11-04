open(FHNDL,">./lrep_d261.dta");
require 'emath.pl';
$oldx=$x=0.001;$oldy=tan(($x))/($x);$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0.001;$x<1.5;$x+=.05){$y=tan(($x))/($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=1.5;$y=tan(($x))/($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
