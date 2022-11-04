open(FHNDL,">./lrep_d208.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=-2/(5*$pi);$orgdx=$dx=.05;if($oldy>-8.33575&& $oldy<8.33575){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<12;$x+=.05){$y=-2/(5*$pi); if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } };$x=12;$y=-2/(5*$pi); if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
