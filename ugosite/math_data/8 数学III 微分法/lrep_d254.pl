open(FHNDL,">./lrep_d254.dta");
require 'emath.pl';
my @val=(0.517638090205042/(2*sin($pi/(12))),(12-2)*180/(2*(12))); foreach (@val){ my $y=$_; if ($y!=0 && abs($y)<0.0001) {$y=sprintf("%f",$y);} printf FHNDL "%s\n",$y; } 
close(FHNDL);
