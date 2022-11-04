open(FHNDL,">./lrep_d70.dta");
require 'emath.pl';
$oldx=$x=-5;$oldy=0-sin(($x))+cos(2*($x));$orgdx=$dx=.05;if($oldy>-166.67194&& $oldy<166.67194){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-5;$x<5;$x+=.05){$y=0-sin(($x))+cos(2*($x)); if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } };$x=5;$y=0-sin(($x))+cos(2*($x)); if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
