#!/usr/bin/perl

use strict;
use warnings; 

#grab the congress number from records. and output a csv of congress number and file name 
# This tool was used to fix congress numbers not being in csv file
my $myPDF = $ARGV[0] or die "file input not selected!\n"; #input argument, bulk text file from pdf
my $endString = "The case is submitted."; #when to stop inside of congressional record parsing
my @mainFileArray; #main array
my $outFile = "list.csv";  #output file name

open('FILE',"< $myPDF") or die "error creating output file" ; #open the fd or die
open('OFILE',"> $outFile") or die "error creating output file" ; #open the fd or die
my $string = "";

my $counter = 0; #counter for whuile loop
my $indexLoc = 0; #location of where to pick numbers 
while(<FILE>)
{
	
	$string = `head -n20 $_ `; #using unix command line to get the first 20 lines of file
	#~ $string = `$string|grep PROCEEDINGS`; 
	
	$indexLoc = index($string,"PROCEEDINGS"); #find the index of where the congressional record should be
	#~ print $indexLoc . "\n"; 
	$string =  substr($string, ($indexLoc - 3), 3); #substring it
	print OFILE $string . ',' . $_ . "\n"; #out put the csv file
	
	
	
	
}



#close the file handles below
close(OFILE); 
close(FILE); 


