open(FHNDL,">./lrep_d24.dta");
require 'emath.pl';
$oldx=$x=-2;$oldy=-($x);$orgdx=$dx=.05;if($oldy>-62.49655&& $oldy<62.49655){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-2;$x<4;$x+=.05){$y=-($x); if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } };$x=4;$y=-($x); if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
