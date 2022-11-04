open(FHNDL,">./lrep_d207.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=2/(5*$pi)+0.05;$orgdx=$dx=.05;if($oldy>-8.33575&& $oldy<8.33575){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<12;$x+=.05){$y=2/(5*$pi)+0.05; if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } };$x=12;$y=2/(5*$pi)+0.05; if($y>-8.33575&& $y<8.33575){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
