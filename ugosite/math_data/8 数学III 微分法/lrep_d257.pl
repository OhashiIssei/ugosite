open(FHNDL,">./lrep_d257.dta");
require 'emath.pl';
usestrict; my $arg=DegRad(75); my $cosa=(cos($arg)); my $sina=(sin($arg)); my $x=1*((-0.707106781186547)*$cosa-(0.707106781186547)*$sina); my $y=1*((-0.707106781186547)*$sina+(0.707106781186547)*$cosa); if(abs($x)<0.0000001){$x=0;}if(abs($y)<0.0000001){$y=0;}printf FHNDL "(%s,%s)",$x,$y; 
close(FHNDL);
