open(FHNDL,">./lrep_d4.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=(0.15)*($x)+1;$orgdx=$dx=.05;if($oldy>-33.34306&& $oldy<33.34306){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<8;$x+=.05){$y=(0.15)*($x)+1; if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } };$x=8;$y=(0.15)*($x)+1; if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
