open(FHNDL,">./lrep_d234.dta");
require 'emath.pl';
$oldx=$x=-4;$oldy=(($x)+0.1)/(($x)*(1-0.1*($x)));$orgdx=$dx=.05;if($oldy>-33.34306&& $oldy<33.34306){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-4;$x<-0.01;$x+=.05){$y=(($x)+0.1)/(($x)*(1-0.1*($x))); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } };$x=-0.01;$y=(($x)+0.1)/(($x)*(1-0.1*($x))); if($y>-33.34306&& $y<33.34306){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
