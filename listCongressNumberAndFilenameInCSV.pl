#!/usr/bin/perl

use strict;
use warnings; 

#grab the congress number from records. and output a csv of congress number and file name 

my $myPDF = $ARGV[0] or die "file input not selected!\n";
my $endString = "The case is submitted.";
my @mainFileArray;
my $outFile = "list.csv"; 

open('FILE',"< $myPDF") or die "error creating output file" ; #open the fd or die
open('OFILE',"> $outFile") or die "error creating output file" ; #open the fd or die
my $string = "";

my $counter = 0; 
my $indexLoc = 0; 
while(<FILE>)
{
	
	$string = `head -n20 $_ `;
	#~ $string = `$string|grep PROCEEDINGS`; 
	
	$indexLoc = index($string,"PROCEEDINGS");
	#~ print $indexLoc . "\n"; 
	$string =  substr($string, ($indexLoc - 3), 3); 
	print OFILE $string . ',' . $_ . "\n"; 
	
	
	
	
}



close(OFILE); 
close(FILE); 


