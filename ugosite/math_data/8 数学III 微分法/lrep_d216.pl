open(FHNDL,">./lrep_d216.dta");
require 'emath.pl';
$oldx=$x=-1.5;$oldy=(($x)*($x)-1)*exp(-($x));$orgdx=$dx=.05;if($oldy>-33.34306&& $oldy<33.34306){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1.5;$x<3;$x+=.05){$y=(($x)*($x)-1)*exp(-($x)); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } };$x=3;$y=(($x)*($x)-1)*exp(-($x)); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
