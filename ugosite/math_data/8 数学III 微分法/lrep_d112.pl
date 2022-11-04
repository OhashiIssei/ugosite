open(FHNDL,">./lrep_d112.dta");
require 'emath.pl';
$oldx=$x=-1;$oldy=sqrt(($x)*($x)*(($x)+1));$orgdx=$dx=.05;if($oldy>-16.67152&& $oldy<16.67152){ printf FHNDL"(%f,%f)",$x,$oldy;} 
for($x=-1;$x<0.8;$x+=.05){$y=sqrt(($x)*($x)*(($x)+1)); if($y>-16.67152&& $y<16.67152){ printf FHNDL"(%f,%f)",$x,$y; } };$x=0.8;$y=sqrt(($x)*($x)*(($x)+1)); if($y>-16.67152&& $y<16.67152){ printf FHNDL"(%f,%f)",$x,$y; } 
close(FHNDL);
