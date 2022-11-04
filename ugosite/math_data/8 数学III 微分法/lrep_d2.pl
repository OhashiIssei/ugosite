open(FHNDL,">./lrep_d2.dta");
require 'emath.pl';
$oldx=$x=0.01;$oldy=-1/($x);$orgdx=$dx=.05;if($oldy>-33.34306&& $oldy<33.34306){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0.01;$x<8;$x+=.05){$y=-1/($x); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } };$x=8;$y=-1/($x); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
