open(FHNDL,">./lrep_d52.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=2*($x)*($x)+($x)-1;$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<1;$x+=.05){$y=2*($x)*($x)+($x)-1; if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=1;$y=2*($x)*($x)+($x)-1; if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
