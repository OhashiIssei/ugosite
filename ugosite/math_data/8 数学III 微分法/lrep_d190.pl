open(FHNDL,">./lrep_d190.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=(0.15)*($x);$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<8;$x+=.05){$y=(0.15)*($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=8;$y=(0.15)*($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
