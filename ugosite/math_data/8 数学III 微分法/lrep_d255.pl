open(FHNDL,">./lrep_d255.dta");
require 'emath.pl';
usestrict; my $x=0.5-(0.866025403784439); my $y=0.866025403784439-(0.5); if(abs($x)<0.0000001){$x=0;}if(abs($y)<0.0000001){$y=0;}printf FHNDL "(%s,%s)",$x,$y; 
close(FHNDL);
