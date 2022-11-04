open(FHNDL,">./lrep_d206.dta");
require 'emath.pl';
$oldx=$x=0.01;$oldy=(cos(($x))/($x)-sin(($x))+aval*($x))/($x);$orgdx=$dx=.05;if($oldy>-8.33575&& $oldy<8.33575){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0.01;$x<12;$x+=.05){$y=(cos(($x))/($x)-sin(($x))+aval*($x))/($x); if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } };$x=12;$y=(cos(($x))/($x)-sin(($x))+aval*($x))/($x); if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
