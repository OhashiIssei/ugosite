open(FHNDL,">./lrep_d16.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=(($x)-2)*(($x)-2)*(($x)-2)/32-(($x)-2)/4+2;$orgdx=$dx=.05;if($oldy>-166.67194&& $oldy<166.67194){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<10;$x+=.05){$y=(($x)-2)*(($x)-2)*(($x)-2)/32-(($x)-2)/4+2; if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } };$x=10;$y=(($x)-2)*(($x)-2)*(($x)-2)/32-(($x)-2)/4+2; if($y>-166.67194&& $y<166.67194){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
