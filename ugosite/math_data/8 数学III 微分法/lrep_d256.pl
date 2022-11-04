open(FHNDL,">./lrep_d256.dta");
require 'emath.pl';
$UVa=sqrt((-0.366025403784439)**2+(0.366025403784439)**2);printf FHNDL "(%s,%s)",-0.366025403784439/$UVa,0.366025403784439/$UVa;
close(FHNDL);
