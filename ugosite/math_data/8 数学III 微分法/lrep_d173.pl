open(FHNDL,">./lrep_d173.dta");
require 'emath.pl';
$oldx=$x=0;$oldy=(($x)-2)*(($x)-2)*(($x)-2)/8-(($x)-2)+2;$orgdx=$dx=.05;if($oldy>-166.67194&& $oldy<166.67194){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=0;$x<6;$x+=.05){$y=(($x)-2)*(($x)-2)*(($x)-2)/8-(($x)-2)+2; if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } };$x=6;$y=(($x)-2)*(($x)-2)*(($x)-2)/8-(($x)-2)+2; if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
