open(FHNDL,">./lrep_d227.dta");
require 'emath.pl';
$oldx=$x=-0.5;$oldy=exp(2.93)*(($x)-2.93)+exp(2.93)+1;$orgdx=$dx=.05;if($oldy>-499.97243&& $oldy<499.97243){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-0.5;$x<5;$x+=.05){$y=exp(2.93)*(($x)-2.93)+exp(2.93)+1; if($y>-499.97243&& $y<499.97243){ printf FHNDL"(%f,%f)",$x,$y; } };$x=5;$y=exp(2.93)*(($x)-2.93)+exp(2.93)+1; if($y>-499.97243&& $y<499.97243){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
