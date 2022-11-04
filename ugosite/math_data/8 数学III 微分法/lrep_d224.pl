open(FHNDL,">./lrep_d224.dta");
require 'emath.pl';
$oldx=$x=-0.5;$oldy=exp(($x))+1;$orgdx=$dx=.05;if($oldy>-499.97243&& $oldy<499.97243){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-0.5;$x<5;$x+=.05){$y=exp(($x))+1; if($y>-499.97243&& $y<499.97243){ printf FHNDL"(%f,%f)",$x,$y; } };$x=5;$y=exp(($x))+1; if($y>-499.97243&& $y<499.97243){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
