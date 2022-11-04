open(FHNDL,">./lrep_d63.dta");
require 'emath.pl';
$oldx=$x=-1.5;$oldy=-1/4;$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1.5;$x<1.5;$x+=.05){$y=-1/4; if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=1.5;$y=-1/4; if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
