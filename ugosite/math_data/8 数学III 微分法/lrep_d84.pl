open(FHNDL,">./lrep_d84.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=-exp(-($x)/4);$orgdx=$dx=.05;if($oldy>-25.0073&& $oldy<25.0073){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<13;$x+=.05){$y=-exp(-($x)/4); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } };$x=13;$y=-exp(-($x)/4); if($y>-25.0073&& $y<25.0073){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
