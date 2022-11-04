open(FHNDL,">./lrep_d278.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=-0.1;$orgdx=$dx=.05;if($oldy>-8.33575&& $oldy<8.33575){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<20;$x+=.05){$y=-0.1; if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } };$x=20;$y=-0.1; if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
