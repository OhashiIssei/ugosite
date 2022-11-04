open(FHNDL,">./lrep_d7.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=sin(($x))+(0.15)*($x);$orgdx=$dx=.05;if($oldy>-33.34306&& $oldy<33.34306){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<8;$x+=.05){$y=sin(($x))+(0.15)*($x); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } };$x=8;$y=sin(($x))+(0.15)*($x); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
