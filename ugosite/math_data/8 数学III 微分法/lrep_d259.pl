open(FHNDL,">./lrep_d259.dta");
require 'emath.pl';
$oldx=$x=0.001;$oldy=($x)-1/2*sin(2*($x));$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0.001;$x<1.5;$x+=.05){$y=($x)-1/2*sin(2*($x)); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=1.5;$y=($x)-1/2*sin(2*($x)); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
