open(FHNDL,">./lrep_d188.dta");
require 'emath.pl';
$oldx=$x=0.01;$oldy=1/($x);$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0.01;$x<8;$x+=.05){$y=1/($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=8;$y=1/($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
