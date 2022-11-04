open(FHNDL,">./lrep_d38.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=(exp(-($x)))*($x);$orgdx=$dx=.05;if($oldy>-49.99289&& $oldy<49.99289){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<10;$x+=.05){$y=(exp(-($x)))*($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } };$x=10;$y=(exp(-($x)))*($x); if($y>-49.99289&& $y<49.99289){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
