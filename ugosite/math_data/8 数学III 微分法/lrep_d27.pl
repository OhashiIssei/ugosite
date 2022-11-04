open(FHNDL,">./lrep_d27.dta");
require 'emath.pl';
$oldx=$x=$pi/2;$oldy=($x)-$pi;$orgdx=$dx=.05;if($oldy>-62.49655&& $oldy<62.49655){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=$pi/2;$x<4;$x+=.05){$y=($x)-$pi; if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } };$x=4;$y=($x)-$pi; if($y>-62.49655&& $y<62.49655){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
