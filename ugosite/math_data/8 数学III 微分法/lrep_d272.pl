open(FHNDL,">./lrep_d272.dta");
require 'emath.pl';
$oldx=$x=0.1;$oldy=log(($x))/($x);$orgdx=$dx=.05;if($oldy>-8.33575&& $oldy<8.33575){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0.1;$x<20;$x+=.05){$y=log(($x))/($x); if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } };$x=20;$y=log(($x))/($x); if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
