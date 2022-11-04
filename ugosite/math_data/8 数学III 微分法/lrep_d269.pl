open(FHNDL,">./lrep_d269.dta");
require 'emath.pl';
$oldx=$x=-2;$oldy=3.5;$orgdx=$dx=.05;if($oldy>-166.67194&& $oldy<166.67194){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-2;$x<6;$x+=.05){$y=3.5; if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } };$x=6;$y=3.5; if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
