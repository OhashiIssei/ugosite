open(FHNDL,">./lrep_d277.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=1/5;$orgdx=$dx=.05;if($oldy>-8.33575&& $oldy<8.33575){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<20;$x+=.05){$y=1/5; if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } };$x=20;$y=1/5; if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
