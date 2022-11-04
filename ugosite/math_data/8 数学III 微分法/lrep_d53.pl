open(FHNDL,">./lrep_d53.dta");
require 'emath.pl';
$oldx=$x=-2;$oldy=2*($x)*($x)+($x)-1;$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-2;$x<2;$x+=.05){$y=2*($x)*($x)+($x)-1; if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=2;$y=2*($x)*($x)+($x)-1; if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
